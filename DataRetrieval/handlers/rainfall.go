package handlers

import (
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
	Username string `json:"username"`
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

type RainDataHandler struct{
	KafkaAsyncProducer sarama.AsyncProducer
}

func (rdh *RainDataHandler) ServeHTTP (w http.ResponseWriter, r *http.Request) {

	decoder := json.NewDecoder(r.Body)
	userRequest := rainFallRequest{}
	err := decoder.Decode(&userRequest)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
	}
	go RetrieveAndSendData(rdh.KafkaAsyncProducer, userRequest)
	w.WriteHeader(http.StatusOK)
}
func PreparePacket(userRequest rainFallRequest) resultPacket{
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
	return packet
}
func RetrieveAndSendData(kafkaAsyncProducer sarama.AsyncProducer, userRequest rainFallRequest) {

	packet := PreparePacket(userRequest)
	packetJson, _ := json.Marshal(packet)
	kafkaAsyncProducer.Input() <- &sarama.ProducerMessage{
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
