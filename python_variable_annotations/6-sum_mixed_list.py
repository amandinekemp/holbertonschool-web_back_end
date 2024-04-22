#!/usr/bin/env python3
"""sum_mixed_list"""

from typing import List, Union


def sum_mix_list(input_list: List[Union[int, float]]) -> Union[int, float]:
    """Sums a list of floats and ints

    Args:
                                    input_list (List[Union[int, float]]):
                                    List of floats and ints to sum

    Returns:
                                    Union[int, float]: Sum of the input_list
    """
    return sum(input_list)
