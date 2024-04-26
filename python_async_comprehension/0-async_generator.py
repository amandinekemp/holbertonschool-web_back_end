#!/usr/bin/env python3
"""This module contains a coroutine that generates random numbers
after an asynchronous wait."""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None, None]:
    """Asynchronously wait 1 second, then yield a random number
    between 0 and 10.

    Yields:
        float: The random number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
