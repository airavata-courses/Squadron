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
	mappings []handlerMappings
}

type handlerMappings struct {
	pattern *regexp.Regexp
	handler http.HandlerFunc
	params []string
}

func (router *Router) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	for _, m := range router.mappings {
		matches := m.pattern.FindStringSubmatch(r.URL.Path)
		if len(matches) == 0 {
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

func (router *Router) HandleFunc(path string, handler http.HandlerFunc) {
	var params []string
	for {
		idx := urlPattern.FindStringIndex(path)
		if idx == nil {
			break
		}
		params = append(params, path[idx[0]+1:idx[1]-1])
		path = fmt.Sprintf("%s([^/]+)%s", path[:idx[0]], path[idx[1]:])
	}
	router.mappings = append(router.mappings, handlerMappings{
		pattern: regexp.MustCompile(path),
		handler: handler,
		params:  params,
	})
}

func Params(r *http.Request) map[string]string {
	p, ok :=  r.Context().Value(ctxKey).(map[string]string)
	if !ok {
		return make(map[string]string)
	}
	return p
}