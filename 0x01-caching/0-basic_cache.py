#!/usr/bin/env python3
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """cache class"""

    def __init__(self):
        """constructor"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """store data"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get data"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
