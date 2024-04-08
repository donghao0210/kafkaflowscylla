from confluent_kafka import KafkaError
from utils.kafka_utils import SubscribeTopic
from utils.debug_utils import debug_print

def KafkaConsumer(topics, queue):
    debug_print("Getting Messages From: ", topics)

    # Subscribe to Kafka topics
    consumer = SubscribeTopic(topics)

    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for new messages
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            else:
                topic = msg.topic()
                message = msg.value().decode('utf-8')
                queue.put((topic, message))  # Put (topic, message) tuple in the queue
                # debug_print("Got message from: ",topic)
    finally:
        consumer.close()  # Close the Kafka consumer connection
