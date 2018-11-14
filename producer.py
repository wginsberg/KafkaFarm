#!/usr/bin/env python3

from kafka import KafkaProducer
import json

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send("farm", {"f": "create", "a": {"id": 1, "name": "farm1"}})
producer.send("farm", {"f": "get", "a": {"id": 1}})
producer.send("farm", {"f": "update", "a": {"id": 1, "name": "Farm1", "address": "123", "latitude": 100, "longitude": 200}})
producer.send("farm", {"f": "get", "a": {"id": 1}})
producer.send("farm", {"f": "delete", "a": {"id": 1}})
producer.send("farm", {"f": "get", "a": {"id": 1}})
producer.flush()
