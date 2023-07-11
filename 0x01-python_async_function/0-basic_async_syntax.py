#!/usr/bin/env python3
"""Asynchronous coroutine takes in an integer argument
(max_delay, with default value of 10) named wait_random that waits for
random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.

Use the random module.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random delay between 0 and max_delay"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
