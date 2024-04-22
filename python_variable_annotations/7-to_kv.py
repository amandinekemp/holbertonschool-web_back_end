#!/usr/bin/env python3
"""to_kv"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple from a string and the square of a number

    Args:
        k (str): The string to include in the tuple
        v (Union[int, float]): The number to square and include in the tuple

    Returns:
        Tuple[str, float]: A tuple containing the string and the square
        of the number
    """
    return (k, v**2)
