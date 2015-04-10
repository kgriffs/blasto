# Copyright 2015 by Kurt Griffiths

import falcon
import uuid

api = falcon.API()


class Ship(object):
    def on_get(self, ship_id):
        pass

    def on_put(self, ship_id):
        pass


class ShipCollection(object):
    def on_post(self):
        pass


ship = Ship()
ship_collection = ShipCollection()


api.add_route('/ships/{ship_id}', ship)
api.add_route('/ships', ship_collection)
