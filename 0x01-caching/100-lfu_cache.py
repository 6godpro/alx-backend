#!/usr/bin/env python3
"""
    Create a class LFUCache that inherits from BaseCaching
    and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):  # type: ignore
    """Represents a LFUCache caching system."""
    def __init__(self):
        """Initializes the caching system."""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Assigns a value to a key."""
        if key is not None and item is not None:
            if key in self.cache_data:
                freq = self.frequency.pop(key)
                self.cache_data.pop(key)
                self.frequency[key] = freq + 1
            else:
                if len(self.cache_data) >= LFUCache.MAX_ITEMS:
                    lfu_key = min(self.frequency, key=self.frequency.get)
                    self.frequency.pop(lfu_key)
                    self.cache_data.pop(lfu_key)
                    print('DISCARD: {}'.format(lfu_key))
                self.frequency[key] = 1

            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with a key."""
        if key in self.frequency:
            freq = self.frequency.pop(key)
            self.frequency[key] = freq + 1
        return self.cache_data.get(key, None)
