package main

import (
	"DataRetrieval/handlers"
	"DataRetrieval/router"
	"net/http"
)

func main() {
	r := &router.Router{}
	r.HandleFunc("api/v1/request/rain/{requestId}", handlers.RetrieveRainData).Methods(http.MethodPost)
	http.ListenAndServe(":8081", r)
}
