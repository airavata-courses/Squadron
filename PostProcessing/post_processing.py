import json
from kafka import KafkaConsumer, KafkaProducer
import os


def process_data():
    consumer = KafkaConsumer('modelExecutionResult', bootstrap_servers=os.getenv('KAFKA'))
    producer = KafkaProducer(bootstrap_servers=os.getenv('KAFKA'))
    print("Post processing service started consuming!!")
    while True:
        for msg in consumer:
            d = bytes.decode(msg.value())
            result = compute(json.loads(d))
            print("Post processing service started producing!!")
            producer.send("postProcessingResult", result)
            producer.flush()


def compute(d):
    # Assuming 4 members per family consuming 50 gallons per month

    d["post_processed"] = total_cost(d["modelResult"])
    d["status"] = "COMPLETED"
    print(d)
    return bytes(d)


def total_cost(water):
    cost = 35*water
    return cost


if  __name__ == "__main__":
    process_data()




