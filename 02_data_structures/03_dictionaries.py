#!/usr/bin/env python3
"""
Python Dictionaries
This script demonstrates the creation, manipulation, and operations on Python dictionaries.
"""

def demonstrate_dictionary_creation():
    """Demonstrate different ways to create dictionaries."""
    print("=== Dictionary Creation ===")
    
    # Empty dictionary
    empty_dict = {}
    print(f"Empty dictionary: {empty_dict}")
    
    # Dictionary with initial key-value pairs
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    print(f"Person dictionary: {person}")
    
    # Dictionary from list of tuples
    items = [("a", 1), ("b", 2), ("c", 3)]
    dict_from_tuples = dict(items)
    print(f"Dictionary from tuples: {dict_from_tuples}")
    
    # Dictionary comprehension
    squares = {x: x**2 for x in range(5)}
    print(f"Squares dictionary: {squares}")
    
    # Dictionary with mixed data types
    mixed = {
        "string": "hello",
        10: "number key",
        (1, 2): "tuple key",
        3.14: "float key"
    }
    print(f"Mixed types dictionary: {mixed}")
    
    # Dictionary from two lists
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    dict_from_lists = dict(zip(keys, values))
    print(f"Dictionary from lists: {dict_from_lists}")
    
    # Dictionary with fromkeys method
    default_dict = dict.fromkeys(["name", "age", "city"], "unknown")
    print(f"Dictionary with default values: {default_dict}")

def demonstrate_dictionary_operations():
    """Demonstrate basic dictionary operations."""
    print("\n=== Dictionary Operations ===")
    
    # Create a sample dictionary
    fruits = {
        "apple": 0.5,
        "banana": 0.3,
        "orange": 0.6
    }
    print(f"Original dictionary: {fruits}")
    
    # Accessing values
    print(f"Price of apple: ${fruits['apple']}")
    
    # Using get() with default value
    print(f"Price of mango: ${fruits.get('mango', 'not available')}")
    
    # Adding/Updating items
    fruits["mango"] = 1.0
    print(f"After adding mango: {fruits}")
    
    # Updating multiple items
    fruits.update({"apple": 0.6, "grape": 0.8})
    print(f"After update: {fruits}")
    
    # Removing items
    removed_price = fruits.pop("banana")
    print(f"Removed banana (${removed_price})")
    print(f"After removal: {fruits}")
    
    # Remove and return last inserted item (Python 3.7+)
    last_item = fruits.popitem()
    print(f"Removed last item: {last_item}")
    
    # Check key existence
    print(f"\nIs 'apple' in fruits? {'apple' in fruits}")
    print(f"Is 'banana' in fruits? {'banana' in fruits}")

def demonstrate_dictionary_methods():
    """Demonstrate common dictionary methods."""
    print("\n=== Dictionary Methods ===")
    
    student = {
        "name": "Alice",
        "grades": {"math": 90, "science": 95, "history": 88},
        "activities": ["chess", "swimming"]
    }
    
    # Get all keys
    print(f"Keys: {list(student.keys())}")
    
    # Get all values
    print(f"Values: {list(student.values())}")
    
    # Get all key-value pairs
    print(f"Items: {list(student.items())}")
    
    # Clear dictionary
    student_backup = student.copy()  # Make a shallow copy
    student.clear()
    print(f"After clear: {student}")
    
    # Restore from backup
    student = student_backup
    print(f"Restored dictionary: {student}")
    
    # Dictionary view objects
    keys_view = student.keys()
    values_view = student.values()
    items_view = student.items()
    
    print("\nDictionary views:")
    print(f"Keys view: {keys_view}")
    print(f"Values view: {values_view}")
    print(f"Items view: {items_view}")
    
    # Views are dynamic
    student["grade_level"] = "Senior"
    print(f"\nUpdated keys view: {keys_view}")
    
    # Set operations on views
    another_student = {
        "name": "Bob",
        "grade_level": "Junior",
        "major": "Computer Science"
    }
    
    # Find common keys
    common_keys = student.keys() & another_student.keys()
    print(f"\nCommon keys between students: {common_keys}")
    
    # Find different keys
    different_keys = student.keys() - another_student.keys()
    print(f"Keys only in first student: {different_keys}")

def demonstrate_nested_dictionaries():
    """Demonstrate working with nested dictionaries."""
    print("\n=== Nested Dictionaries ===")
    
    # Create a nested dictionary
    school = {
        "students": {
            "alice": {
                "grade": "A",
                "subjects": ["math", "science"]
            },
            "bob": {
                "grade": "B",
                "subjects": ["history", "english"]
            }
        },
        "teachers": {
            "math": "Mr. Smith",
            "science": "Mrs. Jones"
        }
    }
    
    # Accessing nested values
    print(f"Alice's grade: {school['students']['alice']['grade']}")
    print(f"Bob's subjects: {school['students']['bob']['subjects']}")
    print(f"Math teacher: {school['teachers']['math']}")
    
    # Modifying nested values
    school['students']['alice']['grade'] = 'A+'
    print(f"Alice's new grade: {school['students']['alice']['grade']}")
    
    # Safe nested access
    def get_nested_value(dict_obj, keys, default=None):
        """Safely get nested dictionary value."""
        try:
            for key in keys:
                dict_obj = dict_obj[key]
            return dict_obj
        except (KeyError, TypeError):
            return default
    
    # Example of safe nested access
    physics_teacher = get_nested_value(school, ['teachers', 'physics'], 'Not assigned')
    print(f"\nPhysics teacher: {physics_teacher}")
    
    # Merging nested dictionaries
    def deep_update(d1, d2):
        """Recursively update dictionary d1 with d2."""
        for key, value in d2.items():
            if key in d1 and isinstance(d1[key], dict) and isinstance(value, dict):
                deep_update(d1[key], value)
            else:
                d1[key] = value
    
    # Example of deep update
    update_info = {
        "students": {
            "alice": {
                "subjects": ["math", "science", "programming"]
            }
        }
    }
    
    deep_update(school, update_info)
    print(f"\nAlice's updated subjects: {school['students']['alice']['subjects']}")

def demonstrate_practical_examples():
    """Demonstrate practical examples using dictionaries."""
    print("\n=== Practical Examples ===")
    
    # Word frequency counter
    def count_words(text):
        words = text.lower().split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        return frequency
    
    text = "the quick brown fox jumps over the lazy dog"
    print(f"Word frequency: {count_words(text)}")
    
    # Dictionary as a cache
    def fibonacci_with_cache(n, cache=None):
        if cache is None:
            cache = {}
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fibonacci_with_cache(n-1, cache) + fibonacci_with_cache(n-2, cache)
        return cache[n]
    
    print(f"\nFibonacci of 10: {fibonacci_with_cache(10)}")
    
    # Group items by category
    items = [
        ("apple", "fruit"),
        ("carrot", "vegetable"),
        ("banana", "fruit"),
        ("broccoli", "vegetable")
    ]
    
    def group_by_category(items):
        from collections import defaultdict
        categories = defaultdict(list)
        for item, category in items:
            categories[category].append(item)
        return dict(categories)
    
    print(f"\nGrouped items: {group_by_category(items)}")
    
    # Dictionary as a simple cache with max size
    from collections import OrderedDict
    class LRUCache:
        def __init__(self, capacity):
            self.cache = OrderedDict()
            self.capacity = capacity
        
        def get(self, key):
            if key not in self.cache:
                return -1
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key, value):
            if key in self.cache:
                # Move to end
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                # Remove least recently used
                self.cache.popitem(last=False)
    
    # Example usage of LRU cache
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"\nLRU Cache example:")
    print(f"get(1): {cache.get(1)}")
    cache.put(3, 3)  # This will remove key 2
    print(f"get(2): {cache.get(2)}")  # Returns -1 (not found)
    print(f"get(3): {cache.get(3)}")  # Returns 3

def main():
    """Main function to run all demonstrations."""
    demonstrate_dictionary_creation()
    demonstrate_dictionary_operations()
    demonstrate_dictionary_methods()
    demonstrate_nested_dictionaries()
    demonstrate_practical_examples()

if __name__ == "__main__":
    main() 