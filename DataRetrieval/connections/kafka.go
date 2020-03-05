package connections

import (
	"DataRetrieval/utils"
	"github.com/Shopify/sarama"
	"log"
	"time"
)

func CreateAsyncProducer() sarama.AsyncProducer {
	p, err := sarama.NewAsyncProducer(utils.Configs.KafkaBrokers, getConfig())
	if err != nil {
		panic("Unable to create kafka producer, err: " + err.Error())
	}
	go func() {
		for err := range p.Errors() {
			log.Println("Failed to write access log entry:", err)
		}
	}()
	return p
}

func getConfig() *sarama.Config {
	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.WaitForLocal       // Only wait for the leader to ack
	config.Producer.Compression = sarama.CompressionSnappy   // Compress messages
	config.Producer.Flush.Frequency = 500 * time.Millisecond // Flush batches every 500ms
	return config
}
