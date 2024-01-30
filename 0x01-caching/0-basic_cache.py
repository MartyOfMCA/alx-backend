#!/usr/bin/env python3
"""
Define a class that implements basic caching.
"""
from base_caching import BaseCaching


class BasicCache (BaseCaching):
    """
    An implementation of the basic caching
    system.
    """

    def put(self, key, value):
        """
        Add a value identified by the given
        key to the cache.

        Parameters:
            key : string
            The key to identify an item
            from the cache.

            value : string
            The value stored in the cache.
        """
        if (key and value):
            self.cache_data[key] = value

    def get(self, key):
        """
        Retrieves the value with the given
        key from the cache.

        Parameters:
            key : string
            The identifier used to fetch a
            value from the cache.

        Returns:
            The value bearing the given key.
            Otherwsie None is returned.
        """
        return (self.cache_data.get(key))
