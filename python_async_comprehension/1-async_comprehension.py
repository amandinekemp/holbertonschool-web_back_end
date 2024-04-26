#!/usr/bin/env python3
"""Collects 10 random numbers using asynchronous understanding
on async_generator"""

import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_generator():
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Returns:
        list: A list of 10 random numbers.
    """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
