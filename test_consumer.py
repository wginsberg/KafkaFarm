#!/usr/bin/env python3

import unittest
from consumer import consume
import json

class TestConsumer(unittest.TestCase):

    def test_create(self):
        value = {"f": "create", "a": {"id": "123"}}
        result = consume(value)

    def test_get(self):
        value1 = {"f": "create", "a": {"id": "123"}}
        consume(value1)
        value2 = {"f": "get", "a": {"id": "123"}}
        result = consume(value2)
        self.assertEqual(json.loads(result)["id"], "123")

    def test_update(self):
        value1 = {"f": "create", "a": {"id": "123"}}
        consume(value1)
        value2 = {"f": "update", "a": {"id": "123", "name": "test"}}
        consume(value2)
        value3 = {"f": "get", "a": {"id": "123"}}
        result = consume(value3)
        self.assertEqual(json.loads(result)["name"], "test")

    def test_delete(self):
        value1 = {"f": "create", "a": {"id": "123"}}
        consume(value1)
        value2 = {"f": "delete", "a": {"id": "123"}}
        consume(value2)
        value3 = {"f": "get", "a": {"id": "123"}}
        result = consume(value3)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()

