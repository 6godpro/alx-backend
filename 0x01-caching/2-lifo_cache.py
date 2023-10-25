#!/usr/bin/env python3
"""
    Create a class LIFOCache that inherits from BaseCaching
    and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):  # type: ignore
    """Represents a LIFOCache caching system."""
    def __init__(self):
        """Initializes the caching system."""
        self.count = 0
        self.last_insert = ''
        super().__init__()

    def put(self, key, item):
        """Assigns a value to a key."""
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.count += 1

            if self.count > LIFOCache.MAX_ITEMS:
                self.cache_data.pop(self.last_insert)
                print('DISCARD: {}'.format(self.last_insert))
                self.count -= 1

            self.cache_data[key] = item
            self.last_insert = key

    def get(self, key):
        """Return the value associated with a key."""
        return self.cache_data.get(key, None)
