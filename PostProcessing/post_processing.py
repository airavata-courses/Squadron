import json
from kafka import KafkaConsumer, KafkaProducer
import os
import sys

def process_data():
    consumer = KafkaConsumer('modelExecutionResult', bootstrap_servers=os.getenv('KAFKA'))
    producer = KafkaProducer(bootstrap_servers=os.getenv('KAFKA'))
    print("Post processing service started consuming!!")
    sys.stdout.flush()
    sys.stderr.flush()
    while True:
        for msg in consumer:
            d = bytes.decode(msg.value)
            result = compute(json.loads(d))
            print("Post processing service started producing!!")
            producer.send("postProcessingResult", result)
            producer.flush()
            sys.stdout.flush()
            sys.stderr.flush()


def compute(d):
    # Assuming 4 members per family consuming 50 gallons per month
    d["post_processed"] = total_cost(d["modelResult"])
    d["status"] = "COMPLETED"
    print(d)
    return json.dumps(d).encode()


def total_cost(water):
    cost = 35*water
    return cost


if  __name__ == "__main__":
    print("started post processing service!!")
    process_data()




