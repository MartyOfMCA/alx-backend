#!/usr/bin/env python3
"""
Define a class that implements Caching
using Most recently used replacement
policy.
"""
from base_caching import BaseCaching


class MRUCache (BaseCaching):
    """
    An implementation of the Most
    Recently Used (MRU) replacement
    policy.
    """

    def __init__(self):
        """ Object constructor. """
        super().__init__()
        self._mru = None

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

        # Do nothing if either there's no
        # key or no value provided.
        if (not key or not value):
            return

        _size = len(_data)

        # Remove mru if new item is added to
        # an overflowing cache.
        if (_size == BaseCaching.MAX_ITEMS and key not in _data):
            print(f"DISCARD: {self._mru}")
            del _data[self._mru]

        _data[key] = value
        # Track the most recently used key
        self._mru = key

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
        # Update the mru when an existing item
        # is accessed.
        if (key in self.cache_data):
            self._mru = key

        return (self.cache_data.get(key))
