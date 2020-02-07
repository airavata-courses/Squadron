## Team Squadron

Team members: Aarushi Bisht Shivam Rastogi Akhil Nagulavancha

### STEPS TO START THE DATA RETRIEVAL SERVICE

* Set the following enviroment variables: KafkaBrokers = localhost: 9092, host: localhost, port: 8081

* Open main.go and run the main function

### DataRetrieval sample API

curl -v -X POST http://localhost:8081/api/v1/request/rain/{requestId} --data '{"HouseArea": 2, "PinCode": 4, "Months": [10]}'

DataRetrieval microservice will populate kafka topic "rainResults".

### Sample kafka output

{"HouseArea":2,"PinCode":47408,"Months":[1,3],"RequestId":"1221","Data":[{"MonthName":"January","HighTemp":36.5,"AvgTemp":27.9,"LowTemp":19.3,"Cdd":0,"Hdd":1151,"Rain":2.66,"Zip":"47408","MonthNumber":1},{"MonthName":"March","HighTemp":52.4,"AvgTemp":42,"LowTemp":31.6,"Cdd":0,"Hdd":713,"Rain":3.66,"Zip":"47408","MonthNumber":3}],"Status":"ok"}
