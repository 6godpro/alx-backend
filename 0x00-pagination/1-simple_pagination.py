#!/usr/bin/env python3
"""
    This module contains a class called Server.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the indexes corresponding to the pagination parameters."""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if not Server.ranges(start, end, len(dataset)):
            return []
        return dataset[start:end]

    @staticmethod
    def ranges(start: int, end: int, range: int) -> bool:
        """Checks to see if start and end are within range."""
        if start < range and end <= range:
            return True
        return False
