#!/usr/bin/env python3
"""
    Create a class FIFOCache that inherits from BaseCaching
    and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):  # type: ignore
    """Represents a FIFOCache caching system."""
    def __init__(self):
        """Initializes the caching system."""
        self.count = 0
        super().__init__()

    def put(self, key, item):
        """Assigns a value to a key."""
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.count += 1

            if self.count > FIFOCache.MAX_ITEMS:
                first_key = list(self.cache_data)[0]
                self.cache_data.pop(first_key)
                print('DISCARD: {}'.format(first_key))
                self.count -= 1
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with a key."""
        return self.cache_data.get(key, None)
