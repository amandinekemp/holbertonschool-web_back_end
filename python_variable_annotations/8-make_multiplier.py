#!/usr/bin/env python3
"""make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a float by a multiplier

    Args:
            multiplier (float): The number to multiply by

    Returns:
            Callable[[float], float]: A function that multiplies a float by
            multiplier
    """

    def multiply_func(n: float) -> float:
        return n * multiplier

    return multiply_func
