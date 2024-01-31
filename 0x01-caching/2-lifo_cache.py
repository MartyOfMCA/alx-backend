#!/usr/bin/env python3
"""
Define a class that implements Caching using
LIFO policy.
"""
from base_caching import BaseCaching


class LIFOCache (BaseCaching):
    """
    An implementation of the LIFO replacement
    policy cache.
    """

    def __init__(self):
        """ Object constructor. """
        super().__init__()
        # Track the last item modified in dataset
        self._last_modified = None

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
            # Track dataset modifications.
            # Modified items already exists
            if (key in _data.keys()):
                self._last_modified = key

            self.cache_data[key] = value

            # Is the cache overflowing
            if (len(_data) > BaseCaching.MAX_ITEMS):
                # Fetch last item modified (if any)
                # or item last added before deletion.
                __last_key = (self._last_modified
                              if self._last_modified
                              else list(_data.keys())[-2])

                print(f"DISCARD: {__last_key}")
                del _data[__last_key]
                # Reset last key modified after its
                # used to remove an item. So
                # subsequent requests can seek for
                # new modifications
                if (self._last_modified and
                        self._last_modified == __last_key):
                    self._last_modified = None

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
