while ! $(nc -z -w 2 kafka1 9092); do
    echo "waiting for kafka..."
    sleep 0.1
done
echo "Kafka connected."

while ! $(nc -z -w 2 mongo 27017); do
    echo "waiting for mongo..."
    sleep 0.1
done
echo "Mongo connected."

echo "compiling code..."
mvn compile

echo "Starting server"
mvn exec:java@Server &

echo "Starting Kafka Consumer"
mvn exec:java@KafkaConsumer
