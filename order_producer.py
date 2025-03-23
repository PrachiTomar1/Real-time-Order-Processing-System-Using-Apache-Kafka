from kafka import KafkaProducer
import json
import time

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample orders
orders = [
    {"order_id": 1, "product": "Laptop", "price": 1200},
    {"order_id": 2, "product": "Phone", "price": 800},
    {"order_id": 3, "product": "Headphones", "price": 150}
]

# Send each order to Kafka
for order in orders:
    producer.send('orders', order)
    print(f"✅ Order Sent: {order}")
    time.sleep(2)

producer.close()
