package utils

import (
	"os"
	"strings"
)

var Configs = getConfig()

type config struct {
	KafkaBrokers []string
	ServicePort  string
	ServiceHost  string
}

func getConfig() config {
	return config{
		KafkaBrokers: strings.Split(os.Getenv("KAFKA"), ","),
		ServiceHost: os.Getenv("HOST"),
		ServicePort: os.Getenv("PORT"),
	}
}
