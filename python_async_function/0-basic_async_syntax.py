#!/usr/bin/env python3
"""The module contains a `wait_random` coroutine which takes an optional
`max_delay` argument (integer, default value 10). It expects a random
delay between 0 and `max_delay` seconds, then returns this delay."""

import asyncio
import random
from typing import Optional


async def wait_random(max_delay: Optional[int] = 10) -> float:
    """Wait for a random delay and return it

    Args:
        max_delay (Optional[int], optional): Maximum delay. Defaults to 10.

    Returns:
        float: The actual delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
