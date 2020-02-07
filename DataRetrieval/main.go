package main

import (
	"DataRetrieval/handlers"
	"DataRetrieval/router"
	"DataRetrieval/utils"
	"github.com/Shopify/sarama"
	"log"
	"net/http"
)

func testKafkaConsumer(){
	consumer, err := sarama.NewConsumer(utils.Configs.KafkaBrokers, sarama.NewConfig())
	if err != nil {
		log.Fatal("Failed to start consumer!!", err)
	}
	partConsumer, err := consumer.ConsumePartition("rainResults", 0, 0)
	if err!= nil {
		log.Fatal("Failed to listen to Topic!!", err)
	}
	for m := range partConsumer.Messages() {
		log.Println("Message: ", string(m.Value))
	}
}

func main() {
	r := &router.Router{}
	r.HandleFunc("api/v1/request/rain/{requestId}", handlers.RetrieveRainData).Methods(http.MethodPost)
	go testKafkaConsumer()
	http.ListenAndServe(utils.Configs.ServiceHost+":"+utils.Configs.ServicePort, r)
}
