#!/usr/bin/env python3
"""This module measures the total execution time of the wait_n coroutine."""

import time
import asyncio

wait_n = __import__("2-measure_runtime.py").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay).

    Args:
            n (int): The number of times to spawn wait_random.
            max_delay (int): The maximum delay.

    Returns:
            float: The total execution time.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
