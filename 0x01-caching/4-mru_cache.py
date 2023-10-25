#!/usr/bin/env python3
"""
    Create a class MRUCache that inherits from BaseCaching
    and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):  # type: ignore
    """Represents a MRUCache caching system."""
    def __init__(self):
        """Initializes the caching system."""
        super().__init__()
        self.frame = []

    def put(self, key, item):
        """Assigns a value to a key."""
        if key is not None and item is not None:
            if key in self.cache_data:
                lru_key = self.frame.remove(key)
            elif len(self.cache_data) >= MRUCache.MAX_ITEMS:
                lru_key = self.frame.pop(MRUCache.MAX_ITEMS - 1)
                self.cache_data.pop(lru_key)
                print('DISCARD: {}'.format(lru_key))

            self.frame.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with a key."""
        if key in self.frame:
            self.frame.remove(key)
            self.frame.append(key)
        return self.cache_data.get(key, None)
