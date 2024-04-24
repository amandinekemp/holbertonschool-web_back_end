#!/usr/bin/env python3
"""This module creates an asyncio.task from the wait_random coroutine."""

import asyncio
import time

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task from the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay.

    Returns:
        asyncio.Task: The created asyncio.Task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
