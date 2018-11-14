#!/usr/bin/env python3

import uuid

class Farm:
    '''
    Single farm record
    '''

    def __init__(self, idx=None, **kwargs):
        self.id = idx
        self.update(**kwargs)

    def update(self, name=None, address=None, latitude=None, longitude=None):
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

class Farms:
    '''
    Farm collection
    '''

    def __init__(self):
        self.all_farms = {}

    def create(self, **kwargs):
        idx = str(uuid.uuid4())
        self.all_farms[idx] = Farm(**kwargs)
        return idx

    def get(self, idx):
        return self.all_farms.get(idx, None)

    def update(self, idx, **kwargs):
        self.all_farms[idx].update(**kwargs)

    def delete(self, idx):
        del self.all_farms[idx]

