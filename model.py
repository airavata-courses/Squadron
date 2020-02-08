import json 

from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

#Takes sum of rain fall from all the months 

def sum_rain(input_data): 
  k=input_data["Data"]
  rain_sum=0
  for i in range(len(k)):
    rain_sum=rain_sum+k[i]["Rain"]
  return rain_sum

def water(Area,rain_fall):
  water_store = 0.56*Area*rain_fall;
  return water_store 

def total_cost (water):
    cost = 35*water
    return cost 
#Assuming 4 members per family consuming 50 gallons per month  


c = AvroConsumer({
    'bootstrap.servers': 'mybroker,mybroker2',
    'group.id': 'groupid',
    'schema.registry.url': 'http://0.0.0.0:9092'})

c.subscribe(['rainResults'])

while True:
    try:
        msg = c.poll(10)

    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break

    if msg is None:
        continue

    if msg.error():
        print("AvroConsumer error: {}".format(msg.error()))
        continue

    print(msg.value())
    msg = msg.value
c.close()

rain_total=sum_rain(msg)
area = msg["HouseArea"]
water_save = water(area,rain_total)
total_save = total_cost(water_save)




 