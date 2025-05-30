#!/usr/bin/env python3
"""
Closures and Function Factories
This module demonstrates the use of closures and function factories in Python.
"""

from typing import Callable, List, Any
import math

def create_multiplier(factor: float) -> Callable[[float], float]:
    """
    A function factory that creates a function to multiply by a specific factor.
    
    Args:
        factor: The multiplication factor
        
    Returns:
        A function that multiplies its input by the factor
    """
    def multiplier(x: float) -> float:
        """Multiply the input by the factor from the outer scope."""
        return x * factor
    
    return multiplier

def create_power_function(exponent: int) -> Callable[[float], float]:
    """
    Creates a function that raises its input to the specified power.
    
    Args:
        exponent: The power to raise the number to
        
    Returns:
        A function that raises its input to the specified power
    """
    def power_function(x: float) -> float:
        """Raise the input to the power specified in the outer scope."""
        return math.pow(x, exponent)
    
    return power_function

def create_logger(prefix: str) -> Callable[..., Any]:
    """
    Creates a logging function with a predefined prefix.
    
    Args:
        prefix: The prefix to add to log messages
        
    Returns:
        A function that logs messages with the specified prefix
    """
    def logger(*args: Any, **kwargs: Any) -> None:
        """Log a message with the prefix from the outer scope."""
        args_str = ", ".join(str(arg) for arg in args)
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"{prefix}: {all_args}")
    
    return logger

def create_counter() -> Callable[[], int]:
    """
    Creates a counter function that maintains its state between calls.
    
    Returns:
        A function that returns incrementing counts
    """
    count = 0
    
    def counter() -> int:
        """Return the next count."""
        nonlocal count
        count += 1
        return count
    
    return counter

def create_accumulator(initial_value: float = 0) -> tuple[
    Callable[[float], float],  # add function
    Callable[[], float],       # get_total function
    Callable[[], None]         # reset function
]:
    """
    Creates a set of functions that work with a shared accumulator.
    
    Args:
        initial_value: The starting value for the accumulator
        
    Returns:
        Tuple of (add, get_total, reset) functions
    """
    total = initial_value
    
    def add(value: float) -> float:
        """Add a value to the accumulator."""
        nonlocal total
        total += value
        return total
    
    def get_total() -> float:
        """Get the current total."""
        return total
    
    def reset() -> None:
        """Reset the accumulator to the initial value."""
        nonlocal total
        total = initial_value
    
    return add, get_total, reset

def create_filter_chain(*predicates: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """
    Creates a function that chains multiple filter predicates.
    
    Args:
        *predicates: Variable number of filter functions
        
    Returns:
        A function that returns True only if all predicates return True
    """
    def combined_filter(x: Any) -> bool:
        """Apply all predicates to the input."""
        return all(predicate(x) for predicate in predicates)
    
    return combined_filter

def main():
    """Demonstrate the usage of closures and function factories."""
    # Demonstrate multiplier factory
    print("\nDemonstrating multiplier factory:")
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print(f"Double 5: {double(5)}")
    print(f"Triple 5: {triple(5)}")
    
    # Demonstrate power function factory
    print("\nDemonstrating power function factory:")
    square = create_power_function(2)
    cube = create_power_function(3)
    print(f"5 squared: {square(5)}")
    print(f"5 cubed: {cube(5)}")
    
    # Demonstrate logger factory
    print("\nDemonstrating logger factory:")
    debug_logger = create_logger("[DEBUG]")
    error_logger = create_logger("[ERROR]")
    debug_logger("Testing", "debug", status="ok")
    error_logger("An error occurred", code=500)
    
    # Demonstrate counter
    print("\nDemonstrating counter:")
    counter1 = create_counter()
    counter2 = create_counter()
    print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
    print(f"Counter2: {counter2()}, {counter2()}")
    
    # Demonstrate accumulator
    print("\nDemonstrating accumulator:")
    add, get_total, reset = create_accumulator(10)
    print(f"Initial total: {get_total()}")
    print(f"Add 5: {add(5)}")
    print(f"Add 3: {add(3)}")
    print(f"Current total: {get_total()}")
    reset()
    print(f"After reset: {get_total()}")
    
    # Demonstrate filter chain
    print("\nDemonstrating filter chain:")
    is_positive = lambda x: x > 0
    is_even = lambda x: x % 2 == 0
    is_less_than_10 = lambda x: x < 10
    
    combined_filter = create_filter_chain(is_positive, is_even, is_less_than_10)
    numbers = range(-5, 15)
    filtered_numbers = [n for n in numbers if combined_filter(n)]
    print(f"Filtered numbers: {filtered_numbers}")

if __name__ == "__main__":
    main() 