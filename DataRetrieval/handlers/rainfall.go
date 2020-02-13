package handlers

import (
	"DataRetrieval/connections"
	"DataRetrieval/router"
	"encoding/json"
	"fmt"
	"github.com/Shopify/sarama"
	"net/http"
)

type rainFallRequest struct {
	HouseArea float64 `json:"house_area"`
	PinCode   int `json:"pincode"`
	Months    []int`json:"months"`
	RequestId string `json:"request_id"`
}

type resultPacket struct {
	rainFallRequest
	RainFallData []rainFallData `json:"Data"`
	Status       string
	ErrorMsg     string `json:"Error,omitempty"`
}

type rainFallData struct {
	MonthName   string
	HighTemp    float32
	AvgTemp     float32
	LowTemp     float32
	Cdd         float32
	Hdd         int
	Rain        float32
	Zip         string
	MonthNumber int
}

type DataRetrievalErrorResponse struct {
	msg string
}

func RetrieveRainData(w http.ResponseWriter, r *http.Request) {
	params := router.Params(r)
	decoder := json.NewDecoder(r.Body)
	userRequest := rainFallRequest{}
	err := decoder.Decode(&userRequest)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
	}
	userRequest.RequestId = params["request_id"]
	go RetrieveAndSendData(userRequest)
	w.WriteHeader(http.StatusOK)
}

func RetrieveAndSendData(userRequest rainFallRequest) {
	packet := resultPacket{rainFallRequest: userRequest}
	response, err := getRainData(userRequest.PinCode)
	if err != nil {
		packet.Status = "fail"
		packet.ErrorMsg = err.Error()
	} else {
		var data []rainFallData
		for _, i := range response {
			for _, m := range userRequest.Months {
				if i.MonthNumber == m {
					data = append(data, i)
					break
				}
			}
		}
		packet.Status = "ok"
		packet.RainFallData = data
		fmt.Println(packet)
	}

	packetJson, _ := json.Marshal(packet)
	connections.KafkaAsync.Input() <- &sarama.ProducerMessage{
		Topic:     "rainResults",
		Key:       nil,
		Value:     sarama.StringEncoder(packetJson),
	}
}

func getRainData(pincode int) (resp [12]rainFallData, err error) {
	// make request to https://www.melissa.com/v2/lookups/zipclimate/zipcode/?zipcode=47404&fmt=json
	url := fmt.Sprintf("https://www.melissa.com/v2/lookups/zipclimate/zipcode/?zipcode=%d&fmt=json", pincode)
	response, err := http.Get(url)
	if err != nil {
		return
	}
	err = json.NewDecoder(response.Body).Decode(&resp)
	if err != nil {
		return
	}
	return
}
