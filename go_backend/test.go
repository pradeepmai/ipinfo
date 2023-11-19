package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"net/http"
	"time"
)

func generateRandomString() string {
	rand.Seed(time.Now().UnixNano())
	const characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	b := make([]byte, 10)
	for i := range b {
		b[i] = characters[rand.Intn(len(characters))]
	}
	return string(b)
}

func generateJSON(w http.ResponseWriter, r *http.Request) {
	randomStrings := make([]string, 1000)
	for i := 0; i < 1000; i++ {
		randomStrings[i] = generateRandomString()
	}
	responseData := map[string][]string{"random_strings": randomStrings}
	jsonData, err := json.Marshal(responseData)
	if err != nil {
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonData)
}

func main() {
	http.HandleFunc("/test", generateJSON)
	port := 5000
	fmt.Printf("Server is running on :%d...\n", port)
	err := http.ListenAndServe(fmt.Sprintf(":%d", port), nil)
	if err != nil {
		fmt.Println(err)
	}
}

