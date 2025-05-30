# Advanced Python Functions

This directory contains examples and exercises demonstrating advanced function concepts in Python. Each module focuses on specific aspects of Python's function capabilities, from decorators to functional programming concepts.

## Table of Contents
1. [Decorators](#decorators)
2. [Advanced Arguments](#advanced-arguments)
3. [Closures and Function Factories](#closures-and-function-factories)
4. [Functional Programming Concepts](#functional-programming-concepts)

## Decorators
File: `01_decorators.py`

Decorators are a powerful way to modify or enhance functions without changing their source code. They use the `@` syntax and are implemented as higher-order functions (functions that take/return other functions).

### Key Concepts Covered:
- Basic decorator syntax and implementation
- Decorators with arguments
- Function wrapping using `functools.wraps`
- Practical decorator examples:
  - Timer decorator for performance measurement
  - Retry decorator for handling failures
  - Memoization decorator for caching results

Example:
```python
@timer_decorator
def slow_function(n: int) -> list:
    return [i ** 2 for i in range(n)]

# Equivalent to:
slow_function = timer_decorator(slow_function)
```

## Advanced Arguments
File: `02_advanced_arguments.py`

Python provides various ways to handle function arguments, from basic positional arguments to complex parameter specifications.

### Key Concepts Covered:
- Variable positional arguments (`*args`)
- Variable keyword arguments (`**kwargs`)
- Keyword-only arguments (using `*`)
- Positional-only arguments (using `/`)
- Default argument pitfalls with mutable objects
- Type hints for complex argument patterns

Example:
```python
def combined_args_kwargs(*args: Any, **kwargs: Any) -> Tuple[List[Any], Dict[str, Any]]:
    return list(args), kwargs

# Usage:
args, kwargs = combined_args_kwargs(1, 2, 3, name="Alice", age=30)
```

## Closures and Function Factories
File: `03_closures_and_factories.py`

Closures are functions that remember values from their enclosing scope even when the outer function has finished execution. Function factories use closures to create specialized functions.

### Key Concepts Covered:
- Creating closures and maintaining state
- Function factories for generating specialized functions
- The `nonlocal` keyword
- Practical applications:
  - Counters with internal state
  - Configurable loggers
  - Accumulator functions
  - Filter chains

Example:
```python
def create_multiplier(factor: float) -> Callable[[float], float]:
    def multiplier(x: float) -> float:
        return x * factor
    return multiplier

double = create_multiplier(2)
print(double(5))  # Output: 10
```

## Functional Programming Concepts
File: `04_functional_concepts.py`

Functional programming emphasizes the use of pure functions and immutable data. Python supports many functional programming concepts through built-in functions and the `functools` module.

### Key Concepts Covered:
- Function composition and piping
- Currying and partial application
- Map-reduce operations
- Pure functions
- Higher-order functions
- Immutable data patterns

Example:
```python
def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def composed_function(x: Any) -> Any:
        result = x
        for f in reversed(functions):
            result = f(result)
        return result
    return composed_function

# Usage:
square_then_add_one = compose(lambda x: x + 1, lambda x: x * x)
print(square_then_add_one(5))  # Output: 26
```

## Best Practices

1. **Type Hints**
   - Use type hints to make function signatures clear
   - Leverage `typing` module for complex types
   - Document return types and parameter types

2. **Documentation**
   - Write clear docstrings explaining function purpose
   - Include examples in docstrings
   - Document exceptions and edge cases

3. **Error Handling**
   - Use appropriate error handling in decorators
   - Handle edge cases in function factories
   - Validate arguments appropriately

4. **Performance**
   - Use memoization for expensive computations
   - Be mindful of closure memory usage
   - Consider generator expressions for large datasets

## Running the Examples

Each Python file can be run directly to see demonstrations of the concepts:

```bash
python 01_decorators.py
python 02_advanced_arguments.py
python 03_closures_and_factories.py
python 04_functional_concepts.py
```

## Further Reading

- [Python Documentation - Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Python Documentation - Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function)
- [PEP 3102 -- Keyword-Only Arguments](https://www.python.org/dev/peps/pep-3102/)
- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/) 