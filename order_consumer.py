from kafka import KafkaConsumer
import json

# Connect to Kafka
consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("👀 Listening for new orders...")

# Process incoming orders
for message in consumer:
    order = message.value
    print(f"✅ Processing Order: {order}")
