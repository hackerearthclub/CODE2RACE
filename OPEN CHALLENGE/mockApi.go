package main

import (
	"encoding/json"
	"log"
	"net/http"
)

func writeCORS(w http.ResponseWriter) http.ResponseWriter {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	return w
}

// Use this to serve json file
func fileServer(filename string) func(w http.ResponseWriter, r *http.Request) {
	return func(w http.ResponseWriter, r *http.Request) {
		w = writeCORS(w)
		http.ServeFile(w, r, filename)
	}
}

type Message struct {
	Name string
	Body string
	Time int64
}

// Use this to return json represantation of an object
func jsonServer(v interface{}) func(w http.ResponseWriter, r *http.Request) {
	return func(w http.ResponseWriter, r *http.Request) {
		w = writeCORS(w)
		json, _ := json.Marshal(v)
		w.Write(json)
	}
}

// Put hellothere.json next to executable/script
func main() {
	http.HandleFunc("/hello-there", fileServer("hellothere.json"))
	http.HandleFunc("/message", jsonServer(Message{"Alice", "Hello", 1294706395881547000}))

	err := http.ListenAndServe(":8081", nil)
	if err != nil {
		log.Fatal("Something went wrong: ", err)
	}
}
