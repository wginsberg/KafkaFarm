#!/usr/bin/env python3

from kafka import KafkaConsumer
import json
from farm import Farm, Farms

consumer = KafkaConsumer('farm',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

fs = Farms()

def consume(value):
    method = getattr(fs, value['f'], None)
    args = value.get('a', {})
    result = method(**args) if method else "No such method {}".format(value['f'])
    if isinstance(result, Farm):
        result = json.dumps(result.__dict__)
    return result

if __name__ == "__main__":
    for msg in consumer:
        print("message: {}".format(msg.value))
        print("result: {}".format(consume(msg.value)))

