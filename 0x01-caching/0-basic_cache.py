#!/usr/bin/env python3
"""
    Create a class BasicCache that inherits from BaseCaching
    and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):  # type: ignore
    """Represents a BasicCache caching system."""
    def put(self, key, item):
        """Assigns a value to a key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with a key."""
        return self.cache_data.get(key, None)
