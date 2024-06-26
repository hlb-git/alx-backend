#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache class """
    def __init__(self):
        """ Constructor method """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[0]))
                del self.cache_data[self.usage[0]]
                del self.usage[0]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
