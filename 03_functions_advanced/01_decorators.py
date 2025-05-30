#!/usr/bin/env python3
"""
Advanced Python Decorators Examples
This module demonstrates various uses of decorators in Python.
"""

import functools
import time
from typing import Callable, Any

def timer_decorator(func: Callable) -> Callable:
    """
    A decorator that measures the execution time of a function.
    
    Args:
        func: The function to be decorated
        
    Returns:
        Callable: The wrapped function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

def retry_decorator(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """
    A decorator that retries a function if it fails.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between retries in seconds
        
    Returns:
        Callable: The decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    print(f"Attempt {attempts} failed. Retrying in {delay} seconds...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def memoize_decorator(func: Callable) -> Callable:
    """
    A decorator that caches function results based on arguments.
    
    Args:
        func: The function to be decorated
        
    Returns:
        Callable: The wrapped function with caching
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key from both args and kwargs
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# Example usage of decorators
@timer_decorator
def slow_function(n: int) -> list:
    """A deliberately slow function to demonstrate the timer decorator."""
    return [i ** 2 for i in range(n)]

@retry_decorator(max_attempts=3, delay=0.1)
def unreliable_function(success_rate: float = 0.5) -> str:
    """A function that sometimes fails to demonstrate the retry decorator."""
    import random
    if random.random() > success_rate:
        raise ValueError("Random failure!")
    return "Success!"

@memoize_decorator
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """Demonstrate the usage of decorators."""
    # Timer decorator example
    print("\nTesting timer decorator:")
    result = slow_function(10000)
    print(f"Result length: {len(result)}")
    
    # Retry decorator example
    print("\nTesting retry decorator:")
    try:
        result = unreliable_function(success_rate=0.3)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Final failure: {e}")
    
    # Memoize decorator example
    print("\nTesting memoize decorator:")
    start_time = time.time()
    result1 = fibonacci(35)  # First call will be slow
    time1 = time.time() - start_time
    
    start_time = time.time()
    result2 = fibonacci(35)  # Second call should be instant
    time2 = time.time() - start_time
    
    print(f"First call result: {result1}, took {time1:.4f} seconds")
    print(f"Second call result: {result2}, took {time2:.4f} seconds")

if __name__ == "__main__":
    main() 