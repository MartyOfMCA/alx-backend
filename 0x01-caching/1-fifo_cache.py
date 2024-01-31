#!/usr/bin/env python3
"""
Define a class that implements Caching using
FIFO policy.
"""
from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """
    An implementation of the FIFO replacement
    policy cache.
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
        _data = self.cache_data

        # Proceed if the key and value are provided
        if (key and value):
            self.cache_data[key] = value

            # Is the cache overflowing
            if (len(_data) > BaseCaching.MAX_ITEMS):
                # Fetch first item before deletion
                __first_key = list(_data.keys())[0]
                print(f"DISCARD: {__first_key}")
                del _data[__first_key]

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
