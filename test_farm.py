#!/usr/bin/env python3

import unittest
from farm import Farm, Farms

class TestCRUD(unittest.TestCase):

    fs = None

    def setUp(self):
        self.fs = Farms()

    def test_create(self):
        ret = self.fs.create("123")

    def test_get(self):
        self.fs.create("123")
        ret = self.fs.get("123")
        self.assertIsInstance(ret, Farm)

    def test_update(self):
        self.fs.create("123")
        self.fs.update("123", name="test", address="456", latitude=1, longitude=2)
        ret = self.fs.get("123")
        self.assertEqual(ret.name, "test")
        self.assertEqual(ret.address, "456")
        self.assertEqual(ret.latitude, 1)
        self.assertEqual(ret.longitude, 2)

    def test_delete(self):
        self.fs.create("123")
        self.fs.delete("123")
        self.assertEqual(self.fs.get("123"), None)

if __name__ == '__main__':
    unittest.main()

