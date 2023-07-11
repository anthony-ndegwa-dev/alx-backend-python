#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write a
measure_runtime coroutine that executes async_comprehension four times
in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import time
import asyncio
from importlib import import_module as v


async_comprehension = v('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 times, measures the total runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
