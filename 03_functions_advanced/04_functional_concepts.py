#!/usr/bin/env python3
"""
Functional Programming Concepts
This module demonstrates functional programming concepts in Python.
"""

from typing import Callable, List, Any, TypeVar, Iterable
from functools import reduce, partial
from operator import add, mul
import itertools

T = TypeVar('T')
R = TypeVar('R')

def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Compose multiple functions from right to left.
    
    Args:
        *functions: Variable number of functions to compose
        
    Returns:
        A function that is the composition of all input functions
    
    Example:
        compose(f, g, h)(x) is equivalent to f(g(h(x)))
    """
    def composed_function(x: Any) -> Any:
        result = x
        for f in reversed(functions):
            result = f(result)
        return result
    return composed_function

def pipe(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Pipe multiple functions from left to right.
    
    Args:
        *functions: Variable number of functions to pipe
        
    Returns:
        A function that applies all functions in sequence
    
    Example:
        pipe(f, g, h)(x) is equivalent to h(g(f(x)))
    """
    return compose(*reversed(functions))

def curry(func: Callable[..., R]) -> Callable[..., Any]:
    """
    Curry a function to allow partial application of arguments.
    
    Args:
        func: Function to curry
        
    Returns:
        Curried version of the function
    """
    def curried(*args: Any, **kwargs: Any) -> Any:
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(
            *args, *more_args, **{**kwargs, **more_kwargs}
        )
    return curried

def memoize(func: Callable[..., R]) -> Callable[..., R]:
    """
    Memoize a function to cache its results.
    
    Args:
        func: Function to memoize
        
    Returns:
        Memoized version of the function
    """
    cache = {}
    
    def memoized(*args: Any, **kwargs: Any) -> Any:
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return memoized

@memoize
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number (memoized version)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def map_reduce(data: Iterable[T],
               mapper: Callable[[T], R],
               reducer: Callable[[R, R], R],
               initial: R) -> R:
    """
    Implement a basic map-reduce operation.
    
    Args:
        data: Input data to process
        mapper: Function to map each element
        reducer: Function to reduce mapped elements
        initial: Initial value for reduction
        
    Returns:
        Result of the map-reduce operation
    """
    return reduce(reducer, map(mapper, data), initial)

def demonstrate_partial_application():
    """Demonstrate partial function application."""
    # Create partially applied functions
    add_five = partial(add, 5)
    multiply_by_three = partial(mul, 3)
    
    # Create a pipeline of operations
    pipeline = pipe(add_five, multiply_by_three)
    
    return pipeline(10)  # (10 + 5) * 3 = 45

def demonstrate_function_composition():
    """Demonstrate function composition."""
    # Define some simple functions
    square = lambda x: x * x
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    
    # Create composed functions
    square_then_add_one = compose(add_one, square)
    add_one_then_square = compose(square, add_one)
    
    return {
        'square_then_add_one': square_then_add_one(5),  # 26
        'add_one_then_square': add_one_then_square(5)   # 36
    }

def demonstrate_currying():
    """Demonstrate currying of functions."""
    # Define a function that takes three arguments
    @curry
    def volume(length: float, width: float, height: float) -> float:
        return length * width * height
    
    # Create partially applied versions
    cube = volume(10)  # length = 10
    square_prism = cube(10)  # width = 10
    result = square_prism(10)  # height = 10
    
    return result

def main():
    """Demonstrate functional programming concepts."""
    # Demonstrate map-reduce
    print("\nDemonstrating map-reduce:")
    numbers = [1, 2, 3, 4, 5]
    sum_of_squares = map_reduce(
        numbers,
        lambda x: x * x,  # mapper
        add,              # reducer
        0                 # initial value
    )
    print(f"Sum of squares: {sum_of_squares}")
    
    # Demonstrate partial application
    print("\nDemonstrating partial application:")
    result = demonstrate_partial_application()
    print(f"Partial application result: {result}")
    
    # Demonstrate function composition
    print("\nDemonstrating function composition:")
    composition_results = demonstrate_function_composition()
    for name, value in composition_results.items():
        print(f"{name}: {value}")
    
    # Demonstrate currying
    print("\nDemonstrating currying:")
    volume = demonstrate_currying()
    print(f"Curried volume calculation: {volume}")
    
    # Demonstrate memoization with Fibonacci
    print("\nDemonstrating memoization:")
    n = 35
    import time
    start = time.time()
    result = fibonacci(n)
    end = time.time()
    print(f"Fibonacci({n}) = {result}")
    print(f"Time taken: {end - start:.4f} seconds")
    
    # Demonstrate with larger number (cached)
    start = time.time()
    result = fibonacci(n)
    end = time.time()
    print(f"Fibonacci({n}) [cached] = {result}")
    print(f"Time taken: {end - start:.4f} seconds")

if __name__ == "__main__":
    main() 