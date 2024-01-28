#!/usr/bin/env python3
"""
Define a function that returns a tuple
containing a range of numbers.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Determine the range of pages for the
    given `page` amd `page_size`.

    Parameters:
        page: int
        The current page to retrieve.

        page_size : int
        The size for each page.

    Returns:
        A tuple containing the start and
        end indexes used as the range of
        indexes to retrieve rows.
    """
    # End index -> page * size of items on page
    # Start index -> index away from end index
    # (moving up not downwards)

    # End index is always the last item on a page.
    # When on page 5, if page size is 10, then the
    # last item index is 5 * 10 -> 50 and start index
    # is index 41. From index 41 we can reach the
    # last item on the page
    return ((page - 1) * page_size, page * page_size)
