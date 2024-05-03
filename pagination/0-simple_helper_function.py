#!/usr/bin/env python3
"""Calculate the range of indexes for pagination parameters"""


def index_range(page, page_size):
    """
    Calculate the range of indexes for pagination parameters.

    Parameters:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and end index.
    """
    # Calculate the start index based on the page number and page size
    start = (page - 1) * page_size
    # Calculate the end index based on the page number and page size
    end = page * page_size
    # Return a tuple containing the start index and end index
    return start, end
