#!/usr/bin/env python3
"""element_length"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing the input list elements
    and their lengths

    Args:
                input_list (Sequence[Iterable]):
                List of iterables to process

    Returns:
                List[Tuple[Iterable, int]]: List of tuples containing
                the input list elements and their lengths
    """
    return [(element, len(element)) for element in lst]
