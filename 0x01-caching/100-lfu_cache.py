#!/usr/bin/env python3
"""
Define a class that implements Caching
using Least Frequently Used replacement
policy.
"""
from base_caching import BaseCaching


class LFUCache (BaseCaching):
    """
    An implementation of the Least
    Frequently Used replacement (LFU)
    policy
    """

    def __init__(self):
        """ Object constructor. """
        super().__init__()
        # Track the number of times a key
        # is referenced
        self._reference_count = {}

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
        # Do nothing when either the key
        # or value is not provided.
        if (not key or not value):
            return

        _data = self.cache_data
        _ref_count = self._reference_count

        # If the cache is full remove item
        # with lfu
        _len_of_data = len(_data)
        if (_len_of_data == BaseCaching.MAX_ITEMS and key not in _data):
            # Fetch lfu.
            # Consider first item in reference
            # count as the lfu.
            __keys = list(_ref_count)
            __first_key = __keys[0]
            __lfu_value = _ref_count.get(__first_key)
            __lfu = __keys[0]

            # Find the exact lfu
            for increment in range(1, len(__keys)):
                ___current_key = __keys[increment]
                ___current_lfu_value = _ref_count.get(___current_key)
                if (___current_lfu_value < __lfu_value):
                    __lfu_value = ___current_lfu_value
                    __lfu = ___current_key

            print(f"DISCARD: {__lfu}")
            del _data[__lfu]
            del _ref_count[__lfu]

        _data[key] = value
        # Update the reference count of a
        # item. New items will have a value
        # of 0.
        _ref_count[key] = (_ref_count.get(key, -1) + 1)

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
        # Update reference count of the
        # item that is accessed
        if (key in self._reference_count):
            self._reference_count[key] = self._reference_count[key] + 1

        return (self.cache_data.get(key))
