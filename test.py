#!/usr/bin/env python3

import unittest
from farm import Farm, Farms

class TestCRUD(unittest.TestCase):

    fs = None

    def setUp(self):
        self.fs = Farms()

    def test_create(self):
        ret = self.fs.create()
        self.assertIsInstance(ret, str)

    def test_get(self):
        idx = self.fs.create()
        ret = self.fs.get(idx)
        self.assertIsInstance(ret, Farm)

    def test_update(self):
        idx = self.fs.create()
        self.fs.update(idx, name="test", address="123", latitude=1, longitude=2)
        ret = self.fs.get(idx)
        self.assertEqual(ret.name, "test")
        self.assertEqual(ret.address, "123")
        self.assertEqual(ret.latitude, 1)
        self.assertEqual(ret.longitude, 2)

    def test_delete(self):
        idx = self.fs.create()
        self.fs.delete(idx)
        self.assertEqual(self.fs.get(idx), None)

if __name__ == '__main__':
    unittest.main()

