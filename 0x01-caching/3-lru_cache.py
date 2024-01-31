#!/usr/bin/env python3
"""
Define a class that implements Caching using
LRU replacement policy.
"""
from base_caching import BaseCaching


class LRUCache (BaseCaching):
    """
    An implementation of the Least Recently
    Used (LRU) replacement policy cache.
    """

    def __init__(self):
        """ Object constructor. """
        super().__init__()
        # Track how items are access or used.
        self._lru_history = {}
        self._added_at = -1

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
        if (not key or not value):
            return

        _data = self.cache_data

        # Add the new item. Update existing
        # item.
        _data[key] = value

        # Update the least recently used value.
        self._added_at += 1
        # Update lru history. The item added
        # or updated will take the new lru.
        self._lru_history[key] = self._added_at

        # Is cache overflowing.
        if (len(_data) > BaseCaching.MAX_ITEMS):
            _keys = list(self._lru_history)
            # Remove least recently used item
            # Lru has the least added at value
            # in the lru history.

            # Assume the first item in lru
            # history has least item.
            # First key is lru
            _first_key = _keys[0]
            _lru = self._lru_history[_first_key]
            _lru_key = _first_key

            # Find the item with the lru from
            # the history
            for increment in range(1, len(_keys)):
                # Track the current key.
                __current_key = _keys[increment]
                # Fetch the lru for the current item.
                __item_lru = self._lru_history[__current_key]
                if (__item_lru < _lru):
                    # Update the lru.
                    _lru_key = _keys[increment]
                    _lru = self._lru_history[_lru_key]

            print(f"DISCARD: {_lru_key}")
            del self._lru_history[_lru_key]
            del _data[_lru_key]

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
        if (key in self.cache_data):
            # Increase the lru history for the
            # given key.
            self._added_at += 1
            self._lru_history[key] = self._added_at

        return (self.cache_data.get(key))
