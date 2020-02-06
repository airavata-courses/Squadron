package handlers

import (
	"DataRetrieval/router"
	"fmt"
	"net/http"
)

func Test(w http.ResponseWriter, r *http.Request) {
	params := router.Params(r)
	fmt.Fprint(w, "Hello Request ID ", params["requestId"])
}
