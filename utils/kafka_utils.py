import yaml
# from debug_utils import debug_print
from confluent_kafka import Consumer

    
def ConnectToKafka():
    config = yaml.safe_load(open("config.yml"))
    kafka_connection_config = config["kafka_config"]
    consumer = Consumer(kafka_connection_config)

    return consumer

def SubscribeTopic(topics):
    consumer = ConnectToKafka()
    consumer.subscribe(topics)
    
    return consumer



