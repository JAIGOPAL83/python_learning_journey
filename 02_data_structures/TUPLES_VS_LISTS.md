# Tuples vs Lists in Python

This guide explains the key differences between tuples and lists in Python, helping you choose the right data structure for your needs.

## Core Differences

### 1. Mutability
- **Lists**: Mutable - can be modified after creation
  ```python
  my_list = [1, 2, 3]
  my_list[0] = 100    # Valid
  my_list.append(4)   # Valid
  ```
- **Tuples**: Immutable - cannot be modified after creation
  ```python
  my_tuple = (1, 2, 3)
  my_tuple[0] = 100   # Raises TypeError
  ```

### 2. Syntax
- **Lists**: Use square brackets `[]`
- **Tuples**: Use parentheses `()` (optional for creation)
  ```python
  # Both create the same tuple
  tuple1 = (1, 2, 3)
  tuple2 = 1, 2, 3
  ```

### 3. Performance
- **Memory**: Tuples use less memory than lists
- **Creation**: Tuples are faster to create
- **Access**: Tuple operations are slightly faster
- **Size**: Lists have variable size, tuples are fixed

## When to Use Each

### Use Tuples For:
1. **Immutable Data**
   - Coordinates: `(x, y)`
   - RGB colors: `(255, 128, 0)`
   - Date/Time: `(2024, 3, 14)`

2. **Dictionary Keys**
   ```python
   locations = {
       (0, 0): "Origin",
       (1, 0): "Right"
   }
   ```

3. **Multiple Return Values**
   ```python
   def get_dimensions():
       return (1920, 1080)
   
   width, height = get_dimensions()
   ```

4. **Named Data (Using namedtuple)**
   ```python
   from collections import namedtuple
   Point = namedtuple('Point', ['x', 'y'])
   p = Point(3, 4)
   ```

### Use Lists For:
1. **Mutable Collections**
   - Shopping lists
   - Task queues
   - Dynamic data sets

2. **When You Need to:**
   - Add/remove items
   - Sort items
   - Modify elements
   - Change the collection size

3. **Data Processing**
   - Filtering results
   - Accumulating values
   - Building result sets

## Performance Considerations

1. **Memory Usage**
   - Lists require more memory (dynamic allocation)
   - Tuples have fixed memory footprint

2. **Operation Speed**
   - Tuple creation is faster
   - Tuple element access is slightly faster
   - Lists are faster for dynamic operations

## Best Practices

1. **Use Tuples When:**
   - Data shouldn't change
   - Need dictionary keys
   - Returning multiple values
   - Want to ensure data integrity

2. **Use Lists When:**
   - Need to modify contents
   - Working with homogeneous data
   - Need dynamic sizing
   - Implementing data structures (stacks, queues)

## Common Operations

### Tuple Operations
```python
# Creation
t = (1, 2, 3)
t = tuple([1, 2, 3])

# Access
first = t[0]
last = t[-1]

# Unpacking
x, y, z = t

# Methods
length = len(t)
count = t.count(2)
index = t.index(2)
```

### List Operations
```python
# Creation
lst = [1, 2, 3]
lst = list((1, 2, 3))

# Modification
lst.append(4)
lst.extend([5, 6])
lst.insert(0, 0)
lst.remove(3)
lst.pop()

# Sorting
lst.sort()
lst.reverse()
```

## Summary

- **Tuples**: Immutable, faster, memory-efficient, good for fixed data
- **Lists**: Mutable, flexible, good for changing data
- Choose based on whether your data needs to change and how you'll use it
- Consider performance implications for large datasets

For practical examples and performance comparisons, see the `tuple_vs_list.py` file in this directory. 