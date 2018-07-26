import threading
import logging
import time
import json

from kafka import KafkaProducer

class Client(object):
    """Simple client for kafka

    """
    def __init__(self):
        super(Client, self).__init__()

    def run(self, args):
        producer = KafkaProducer(bootstrap_servers='kafka-1:19092',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        while True:
            producer.send('my-topic', {"dataObjectID": "test1"})
            producer.send('my-topic', {"dataObjectID": "test2"})
            time.sleep(1)
