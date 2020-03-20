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
            d = json.loads(d)
            print("post processing got this", d)
            if d['Status'] == "fail":
                print("Passing failed process")
                print("Post processing sending this: ", d)
                producer.send("postProcessingResult", json.dumps(d).encode())
                sys.stdout.flush()
                sys.stderr.flush()
                continue
            result = compute(d)
            print("Post processing producing this: ", result)
            producer.send("postProcessingResult", result)
            producer.flush()
            sys.stdout.flush()
            sys.stderr.flush()


def compute(d):
    # Assuming 4 members per family consuming 50 gallons per month

    d["post_processed_result"] = total_cost(d["model_result"])
    print("Post processing setting status as Completed for the request")
    d["status"] = "COMPLETED"
    sys.stdout.flush()
    sys.stderr.flush()
    return json.dumps(d).encode()


def total_cost(water):
    cost = 35*water
    return cost


if  __name__ == "__main__":
    print("started post processing service!!")
    process_data()




