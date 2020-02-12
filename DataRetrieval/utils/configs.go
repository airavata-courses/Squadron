package utils

var Configs = getConfig()

type config struct {
	KafkaBrokers []string
	ServicePort  string
	ServiceHost  string
}

func getConfig() config {
	return config{
		//KafkaBrokers: strings.Split(os.Getenv("KafkaBrokers"), ","),
		//ServiceHost: os.Getenv("host"),
		//ServicePort: os.Getenv("port"),

		KafkaBrokers: []string{"kafka1:9092"},
		ServiceHost: "0.0.0.0",
		ServicePort: "9093",
	}
}
