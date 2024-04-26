#!/usr/bin/env python3
"""This module measures the total execution time of running the
'async_comprehension' coroutine four times in parallel."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel
    and measure the total runtime.

    Returns:
        float: The total runtime.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time
