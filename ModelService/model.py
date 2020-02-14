import json
from kafka import KafkaConsumer, KafkaProducer
import os
import logging
import sys

logger = logging.getLogger("Main")
logger.setLevel(logging.INFO)


def process_data():
    consumer = KafkaConsumer('rainResults', bootstrap_servers=os.getenv('KAFKA'))
    producer = KafkaProducer(bootstrap_servers=os.getenv('KAFKA'))
    print("Model execution service started consuming!!")
    sys.stdout.flush()
    sys.stderr.flush()
    while True:
        for msg in consumer:
            d = bytes.decode(msg.value)
            d = json.loads(d)
            print("model got this :", d)
            if d['Status'] == 'fail':
                print("Failed to process the request because data retrieval failed")
                d['status'] = "FAILED"
                print("Model execution service started producing!!")
                print("model sent this:", d)
                producer.send("modelExecutionResult", json.dumps(d).encode())
                sys.stdout.flush()
                sys.stderr.flush()
                producer.flush()
                continue
        
            result = compute(d)
            print("Model execution service started producing!!")
            print("Produced by model service: ", result)
            producer.send("modelExecutionResult", result)
            sys.stdout.flush()
            sys.stderr.flush()
            producer.flush()


def compute(d):
    # Assuming 4 members per family consuming 50 gallons per month

    rain_total = sum_rain(d)
    area = d["house_area"]
    water_save = water(area, rain_total)
    d["model_result"] = water_save
    print(d)
    return json.dumps(d).encode()


# Takes sum of rain fall from all the months
def sum_rain(input_data):
    k = input_data["Data"]
    rain_sum = 0
    for i in range(len(k)):
        rain_sum = rain_sum+k[i]["Rain"]
    return rain_sum


def water(area, rain_fall):
    water_store = 0.56*area*rain_fall
    return water_store


if __name__ == "__main__":
    print("started model service!!")
    process_data()




