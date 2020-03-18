package router

import (
	"context"
	"fmt"
	"net/http"
	"regexp"
)

var urlPattern = regexp.MustCompile(`{[^/]+}`)
const ctxKey = "_router_url_params_"

type Router struct {
	mappings []*handlerMappings
}

type handlerMappings struct {
	pattern *regexp.Regexp
	handler http.Handler
	methods []string
	params []string
}

func (mapping *handlerMappings) Methods(methods ...string) {
	mapping.methods = methods
}

func (router *Router) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	for _, m := range router.mappings {
		matches := m.pattern.FindStringSubmatch(r.URL.Path)
		if len(matches) == 0 {
			continue
		}
		methodAllowed := false
		for _, i := range m.methods {
			if i == r.Method {
				methodAllowed = true
				break
			}
		}
		if !methodAllowed {
			continue
		}
		params := make(map[string]string)
		for i, k := range m.params {
			params[k] = matches[i+1]
		}
		r = r.WithContext(context.WithValue(r.Context(), ctxKey, params))
		m.handler.ServeHTTP(w, r)
		return
	}
	w.WriteHeader(http.StatusNotFound)
}

func (router *Router) Handle(path string, handler http.Handler) *handlerMappings {
	var params []string
	for {
		idx := urlPattern.FindStringIndex(path)
		if idx == nil {
			break
		}
		params = append(params, path[idx[0]+1:idx[1]-1])
		path = fmt.Sprintf("%s([^/]+)%s", path[:idx[0]], path[idx[1]:])
	}
	mapping := &handlerMappings{
		pattern: regexp.MustCompile(path),
		handler: handler,
		params:  params,
	}
	router.mappings = append(router.mappings, mapping)
	return mapping
}

func Params(r *http.Request) map[string]string {
	p, ok :=  r.Context().Value(ctxKey).(map[string]string)
	if !ok {
		return make(map[string]string)
	}
	return p
}