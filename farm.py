#!/usr/bin/env python3


class Farm:
    '''
    Single farm record
    '''

    def __init__(self, id_, **kwargs):
        self.id = id_
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

    def create(self, id, **kwargs):
        self.all_farms[id] = Farm(id, **kwargs)

    def get(self, id):
        return self.all_farms.get(id, None)

    def update(self, id, **kwargs):
        self.all_farms[id].update(**kwargs)

    def delete(self, id):
        del self.all_farms[id]

