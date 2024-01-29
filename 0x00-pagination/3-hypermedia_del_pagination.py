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

        assert isinstance(index, int)
        assert index >= 0
        assert index <= len(dataset) - page_size

        end_index = index + page_size
        data = []
        i = index

        # Scan items in dataset
        while (i < end_index):
            # Seek the next row if there's no record
            if (not dataset.get(i)):
                # Extend the end index when a row has no record
                end_index += 1
            else:
                data.append(dataset.get(i))
            i += 1

        return ({
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": end_index
        })
