# Real-time-Order-Processing-System-Using-Apache-Kafka
# Objective
To implement a simple real-time order processing system using Apache Kafka. This project will simulate an e-commerce order system, where:
1. Orders are placed by customers and sent to a Kafka topic (orders).
2. A consumer service processes the orders and logs the details.
# #Technologies Used
1. Apache Kafka
2. Python (for producer & consumer)
3. Docker (to set up Kafka broker)
   
Steps to follow to write and run the Apache-Kafka:
# #Step 1: Set Up Kafka Using Docker
1. Create a docker-compose.yml file to run Kafka and Zookeeper.
2. Run Kafka using:
   bash: docker-compose up -d

# #Step 2: Install Dependencies
Ensure Python and Kafka dependencies are installed: 
   bash: pip install kafka-python

# #Step 3: Create Kafka Producer (Order Producer)
A simple Python producer script (order_producer.py) to send new orders to Kafka.

# #Step 4: Create Kafka Consumer (Order Processor)
A simple Python consumer script (order_consumer.py) that listens for new orders.

# #Step 5: Running the Project
1. Start Kafka (if not running):
   bash: docker-compose up -d
2. Start the consumer (in one terminal):
   bash:python order_consumer.py
3. Run the producer (in another terminal):
   bash:python order_producer.py
   
# #Expected Output
1. The producer sends orders to the Kafka topic (orders).
2. The consumer reads and processes orders in real-time.
