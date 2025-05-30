#!/usr/bin/env python3
"""
Advanced Function Arguments and Parameters
This module demonstrates various advanced concepts related to function arguments in Python.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
from dataclasses import dataclass

@dataclass
class Person:
    """Simple class for demonstration purposes."""
    name: str
    age: int

def demonstrate_args(*args: Any) -> List[Any]:
    """
    Demonstrates the use of variable positional arguments.
    
    Args:
        *args: Variable number of positional arguments
        
    Returns:
        List of the provided arguments
    """
    return list(args)

def demonstrate_kwargs(**kwargs: Any) -> Dict[str, Any]:
    """
    Demonstrates the use of variable keyword arguments.
    
    Args:
        **kwargs: Variable number of keyword arguments
        
    Returns:
        Dictionary of the provided keyword arguments
    """
    return kwargs

def combined_args_kwargs(*args: Any, **kwargs: Any) -> Tuple[List[Any], Dict[str, Any]]:
    """
    Demonstrates combining both *args and **kwargs.
    
    Args:
        *args: Variable number of positional arguments
        **kwargs: Variable number of keyword arguments
        
    Returns:
        Tuple containing list of args and dict of kwargs
    """
    return list(args), kwargs

def default_mutable_warning(items: Optional[List[int]] = None) -> List[int]:
    """
    Demonstrates proper handling of mutable default arguments.
    
    Args:
        items: Optional list of integers
        
    Returns:
        Modified list of integers
    """
    # Proper way to handle mutable defaults
    if items is None:
        items = []
    items.append(1)
    return items

def enforce_keyword_args(*, name: str, age: int) -> Person:
    """
    Demonstrates enforcing keyword arguments using *.
    
    Args:
        name: Person's name (must be keyword arg)
        age: Person's age (must be keyword arg)
        
    Returns:
        Person instance
    """
    return Person(name=name, age=age)

def positional_only_args(a: int, b: int, /, c: int) -> int:
    """
    Demonstrates positional-only arguments using /.
    
    Args:
        a: First number (positional-only)
        b: Second number (positional-only)
        c: Third number (position or keyword)
        
    Returns:
        Sum of the numbers
    """
    return a + b + c

def combined_argument_types(
    a: int,           # positional or keyword
    b: int,           # positional or keyword
    /,                # marks end of positional-only
    c: int,           # positional or keyword
    d: int,           # positional or keyword
    *,                # marks beginning of keyword-only
    e: int,           # keyword-only
    f: int           # keyword-only
) -> int:
    """
    Demonstrates combining different argument types.
    
    Args:
        a: First number (positional-only)
        b: Second number (positional-only)
        c: Third number (positional or keyword)
        d: Fourth number (positional or keyword)
        e: Fifth number (keyword-only)
        f: Sixth number (keyword-only)
        
    Returns:
        Sum of all numbers
    """
    return a + b + c + d + e + f

def main():
    """Demonstrate the usage of advanced argument handling."""
    # Demonstrate *args
    print("\nDemonstrating *args:")
    result = demonstrate_args(1, "hello", 3.14, [1, 2, 3])
    print(f"Args result: {result}")
    
    # Demonstrate **kwargs
    print("\nDemonstrating **kwargs:")
    result = demonstrate_kwargs(name="Alice", age=30, city="New York")
    print(f"Kwargs result: {result}")
    
    # Demonstrate combined args and kwargs
    print("\nDemonstrating combined args and kwargs:")
    args, kwargs = combined_args_kwargs(1, 2, 3, name="Alice", age=30)
    print(f"Combined result - Args: {args}, Kwargs: {kwargs}")
    
    # Demonstrate mutable default argument handling
    print("\nDemonstrating mutable default argument handling:")
    result1 = default_mutable_warning()
    result2 = default_mutable_warning()
    print(f"First call: {result1}")
    print(f"Second call: {result2}")  # Note: Lists are different objects
    
    # Demonstrate keyword-only arguments
    print("\nDemonstrating keyword-only arguments:")
    person = enforce_keyword_args(name="Alice", age=30)
    print(f"Person created: {person}")
    
    # Demonstrate positional-only arguments
    print("\nDemonstrating positional-only arguments:")
    result = positional_only_args(1, 2, c=3)
    print(f"Positional-only result: {result}")
    
    # Demonstrate combined argument types
    print("\nDemonstrating combined argument types:")
    result = combined_argument_types(1, 2, 3, 4, e=5, f=6)
    print(f"Combined types result: {result}")
    
    # Demonstrate some common errors (commented out)
    """
    # These would raise errors:
    enforce_keyword_args("Alice", 30)  # Error: positional arguments not allowed
    positional_only_args(a=1, b=2, c=3)  # Error: positional-only args with keywords
    """

if __name__ == "__main__":
    main() 