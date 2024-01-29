#!/usr/bin/env python3
"""
Define a class that implements pagination.
"""
import csv
from math import ceil
from typing import (
        List,
        Tuple,
        Dict
        )


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
    return ((page - 1) * page_size, page * page_size)


class Server:
    """
    Server class to paginate a database of
    popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Fetches pages or rows in a particular range.

        Parameters:
            page : int, optional
            The page to retrieve information from.
            By default page 1 is queried.

            page_size : int, optional
            The total number of records or rows
            found on the given page.
            By default, a page has 10 records.

        Returns:
            A list of list containing the pages
            found in the matching range.
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0

        start_index, end_index = index_range(page, page_size)
        rows: List[int] = []

        self.dataset()

        if (start_index > len(self.__dataset) or
                (end_index > len(self.__dataset))):
            return ([])

        return ([self.__dataset[index] for index
                in range(start_index, end_index)])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Fetches pages or rows in a particular range.

        Parameters:
            page : int, optional
            The page to retrieve information from.
            By default page 1 is queried.

            page_size : int, optional
            The total number of records or rows
            found on the given page.
            By default, a page has 10 records.

        Returns:
            A dictionary containing the pages
            found in the matching range.
        """
        dataset = self.get_page(page, page_size)
        return ({
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": (page + 1) if (page <= len(dataset)) else None,
            "prev_page": (page - 1) if page > 1 else None,
            "total_pages": ceil(len(self.__dataset) / page_size)
        })
