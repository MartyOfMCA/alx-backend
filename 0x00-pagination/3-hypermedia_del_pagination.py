#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
import math
from typing import (
        List,
        Dict,
        Union,
        Any
        )


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset. """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Union[int, Any] = None,
                        page_size: int = 10) -> Dict:
        """
        Fetch a number of `page_size` pages
        starting from the given `index`.

        Parameters:
            index : int, optional
            The start index of the
            return page. Has a default
            value of None.

            page_size : int, optional
            The total number of records on a
            current page The current page's
            size. By default, a page has 10
            records.
        """
        dataset = self.indexed_dataset()

        assert index < len(dataset)

        data = [dataset.get(i) for i in range(index, index + page_size)]

        return ({
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": (index + page_size)
        })
