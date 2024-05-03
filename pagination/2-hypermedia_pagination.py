#!/usr/bin/env python3
"""
This module implements hypermedia pagination
for a database of popular baby names.
It provides a Server class with a get_hyper method that returns a dictionary
containing pagination information.
"""

import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> tuple:
    """Calculate the range of indexes for pagination parameters."""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""

    # Data file
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # Initialize the dataset to None
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        # If the dataset is not yet loaded
        if self.__dataset is None:
            # Open the data file
            with open(self.DATA_FILE) as f:
                # Read the CSV file
                reader = csv.reader(f)
                # Create a list of all rows
                dataset = [row for row in reader]
            # Save the dataset excluding the header
            self.__dataset = dataset[1:]
        # Return the dataset
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset."""
        # Verify that page and page size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the start and end indices for pagination
        start, end = index_range(page, page_size)
        # Return the appropriate page of the dataset
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Function hypermedia pagination

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            Dict: Dictionnary of data and all information
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
