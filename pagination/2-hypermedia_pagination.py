#!/usr/bin/env python3
"""
pagination - 2. Hypermedia pagination
"""
import csv
import math
from typing import List, Dict
from typing import Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self._data = []

    def dataset(self) -> List[List]:
        """Returns a cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of pages

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The size of the page. Defaults to 10.

        Returns:
            List[List]: A list of pages
        """
        assert (
            isinstance(page, int) and page > 0
        ), "Page must be an integer greater than 0"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be an integer greater than 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset) or start_index < 0:
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary of data and all information for hypermedia
        pagination

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The size of the page. Defaults to 10.

        Returns:
            Dict: A dictionary of data and all information
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of start and end index for pagination parameters

    Args:
        page (int): The page number
        page_size (int): The size of the page

    Returns:
        tuple[int, int]: A tuple of start and end index
    """
    # Calculate the start index
    start_index = (page - 1) * page_size
    # Calculate the end index
    end_index = start_index + page_size
    return (start_index, end_index)
