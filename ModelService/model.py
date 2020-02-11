import json
from kafka import KafkaConsumer, KafkaProducer
import os


def process_data():
    consumer = KafkaConsumer(os.getenv("DATA_RETRIEVAL_TOPIC", 'rainResults'), bootstrap_servers=os.getenv('KAFKA', "localhost:9092"))
    producer = KafkaProducer(bootstrap_servers=os.getenv('KAFKA', "localhost:9092"))
    print("Model execution service started consuming!!")
    while True:
        for msg in consumer:
            d = bytes.decode(msg.value())
            result = compute(json.loads(d))
            print("Model execution service started producing!!")
            producer.send(os.getenv("MODEL_RESULT_TOPIC", "modelExecutionResult"), result)
            producer.flush()


def compute(d):
    # Assuming 4 members per family consuming 50 gallons per month
    rain_total = sum_rain(d)
    area = d["HouseArea"]
    water_save = water(area, rain_total)
    d["modelResult"] = total_cost(water_save)
    d["status"] = "COMPLETED"
    print(d)
    return bytes(d)


# Takes sum of rain fall from all the months
def sum_rain(input_data):
    k=input_data["Data"]
    rain_sum=0
    for i in range(len(k)):
        rain_sum=rain_sum+k[i]["Rain"]
    return rain_sum


def water(area, rain_fall):
    water_store = 0.56*area*rain_fall;
    return water_store


def total_cost(water):
    cost = 35*water
    return cost


if  __name__ == "__main__":
    process_data()




