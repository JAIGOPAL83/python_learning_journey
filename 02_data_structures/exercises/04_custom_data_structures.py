#!/usr/bin/env python3
"""
Practice exercises for implementing custom data structures.
Focus on implementing efficient and practical data structures.
"""

from typing import Any, List, Optional, Dict
from collections import deque

class Exercise1Stack:
    """
    Exercise 1: Implement a Stack with Maximum Element Tracking
    
    Implement a stack that keeps track of the maximum element
    and can return it in O(1) time.
    
    Methods to implement:
    - push(value): Add element to top of stack
    - pop(): Remove and return top element
    - get_max(): Return maximum element in stack
    - is_empty(): Return True if stack is empty
    
    Example usage:
    stack = Exercise1Stack()
    stack.push(3)
    stack.push(5)
    stack.push(2)
    print(stack.get_max())  # Should print: 5
    stack.pop()
    print(stack.get_max())  # Should print: 5
    stack.pop()
    print(stack.get_max())  # Should print: 3
    """
    
    def __init__(self):
        # Your solution here
        # self.stack = []
        # self.max_stack = []
        pass
    
    def push(self, value: int) -> None:
        # Your solution here
        # self.stack.append(value)
        # if not self.max_stack or value >= self.max_stack[-1]:
        #     self.max_stack.append(value)
        pass
    
    def pop(self) -> Optional[int]:
        # Your solution here
        # if not self.stack:
        #     return None
        # value = self.stack.pop()
        # if value == self.max_stack[-1]:
        #     self.max_stack.pop()
        # return value
        return None
    
    def get_max(self) -> Optional[int]:
        # Your solution here
        # return self.max_stack[-1] if self.max_stack else None
        return None
    
    def is_empty(self) -> bool:
        # Your solution here
        # return len(self.stack) == 0
        return True

class Exercise2Queue:
    """
    Exercise 2: Implement a Queue with Average Tracking
    
    Implement a queue that maintains a running average of its elements
    and can return it in O(1) time.
    
    Methods to implement:
    - enqueue(value): Add element to end of queue
    - dequeue(): Remove and return front element
    - get_average(): Return average of all elements
    - get_size(): Return number of elements in queue
    
    Example usage:
    queue = Exercise2Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.get_average())  # Should print: 20.0
    queue.dequeue()
    print(queue.get_average())  # Should print: 25.0
    """
    
    def __init__(self):
        # Your solution here
        # self.queue = deque()
        # self.sum = 0
        # self.count = 0
        pass
    
    def enqueue(self, value: float) -> None:
        # Your solution here
        # self.queue.append(value)
        # self.sum += value
        # self.count += 1
        pass
    
    def dequeue(self) -> Optional[float]:
        # Your solution here
        # if not self.queue:
        #     return None
        # value = self.queue.popleft()
        # self.sum -= value
        # self.count -= 1
        # return value
        return None
    
    def get_average(self) -> Optional[float]:
        # Your solution here
        # return self.sum / self.count if self.count > 0 else None
        return None
    
    def get_size(self) -> int:
        # Your solution here
        # return self.count
        return 0

class Exercise3Cache:
    """
    Exercise 3: Implement a Time-Based Cache
    
    Implement a cache that automatically expires entries after a given duration.
    
    Methods to implement:
    - put(key, value, duration): Add key-value pair that expires after duration seconds
    - get(key): Get value for key (None if expired or not found)
    - remove(key): Remove key-value pair
    - clear_expired(): Remove all expired entries
    
    Example usage:
    cache = Exercise3Cache()
    cache.put("A", 1, 60)  # Expires in 60 seconds
    print(cache.get("A"))  # Should print: 1
    # After 60 seconds...
    print(cache.get("A"))  # Should print: None
    """
    
    def __init__(self):
        # Your solution here
        # from time import time
        # self.cache = {}  # {key: (value, expiry_timestamp)}
        pass
    
    def put(self, key: str, value: Any, duration: int) -> None:
        # Your solution here
        # from time import time
        # self.cache[key] = (value, time() + duration)
        pass
    
    def get(self, key: str) -> Optional[Any]:
        # Your solution here
        # from time import time
        # if key not in self.cache:
        #     return None
        # value, expiry = self.cache[key]
        # if time() > expiry:
        #     del self.cache[key]
        #     return None
        # return value
        return None
    
    def remove(self, key: str) -> None:
        # Your solution here
        # self.cache.pop(key, None)
        pass
    
    def clear_expired(self) -> None:
        # Your solution here
        # from time import time
        # current_time = time()
        # expired_keys = [
        #     key for key, (_, expiry) in self.cache.items()
        #     if current_time > expiry
        # ]
        # for key in expired_keys:
        #     del self.cache[key]
        pass

class Exercise4PriorityQueue:
    """
    Exercise 4: Implement a Priority Queue with Update Priority
    
    Implement a priority queue that allows updating priorities of existing items.
    
    Methods to implement:
    - add_task(task, priority): Add a task with given priority
    - get_highest_priority(): Get and remove highest priority task
    - update_priority(task, new_priority): Update priority of existing task
    - remove_task(task): Remove a specific task
    
    Example usage:
    pq = Exercise4PriorityQueue()
    pq.add_task("Task A", 3)
    pq.add_task("Task B", 1)
    pq.add_task("Task C", 2)
    print(pq.get_highest_priority())  # Should print: "Task A"
    pq.update_priority("Task B", 4)
    print(pq.get_highest_priority())  # Should print: "Task B"
    """
    
    def __init__(self):
        # Your solution here
        # import heapq
        # self.tasks = []  # [(priority, task)]
        # self.task_lookup = {}  # {task: index}
        # self.counter = 0
        pass
    
    def add_task(self, task: str, priority: int) -> None:
        # Your solution here
        # import heapq
        # if task in self.task_lookup:
        #     self.remove_task(task)
        # entry = [-priority, self.counter, task]
        # self.counter += 1
        # heapq.heappush(self.tasks, entry)
        # self.task_lookup[task] = entry
        pass
    
    def get_highest_priority(self) -> Optional[str]:
        # Your solution here
        # import heapq
        # while self.tasks:
        #     priority, count, task = heapq.heappop(self.tasks)
        #     if task in self.task_lookup:
        #         del self.task_lookup[task]
        #         return task
        # return None
        return None
    
    def update_priority(self, task: str, new_priority: int) -> None:
        # Your solution here
        # self.remove_task(task)
        # self.add_task(task, new_priority)
        pass
    
    def remove_task(self, task: str) -> None:
        # Your solution here
        # entry = self.task_lookup.pop(task, None)
        # if entry:
        #     entry[-1] = None  # Mark as removed
        pass

def check_exercise_1():
    """Test Exercise 1: Stack with Maximum Element"""
    print("\nTesting Exercise 1: Stack with Maximum Element")
    stack = Exercise1Stack()
    
    # Test push and get_max
    stack.push(3)
    stack.push(5)
    stack.push(2)
    print(f"After pushing 3, 5, 2:")
    print(f"Maximum element: {stack.get_max()} (Expected: 5)")
    
    # Test pop and get_max
    stack.pop()
    print(f"After popping once:")
    print(f"Maximum element: {stack.get_max()} (Expected: 5)")
    
    stack.pop()
    print(f"After popping twice:")
    print(f"Maximum element: {stack.get_max()} (Expected: 3)")

def check_exercise_2():
    """Test Exercise 2: Queue with Average Tracking"""
    print("\nTesting Exercise 2: Queue with Average Tracking")
    queue = Exercise2Queue()
    
    # Test enqueue and average
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"After enqueueing 10, 20, 30:")
    print(f"Average: {queue.get_average()} (Expected: 20.0)")
    
    # Test dequeue and average
    queue.dequeue()
    print(f"After dequeuing once:")
    print(f"Average: {queue.get_average()} (Expected: 25.0)")
    
    print(f"Queue size: {queue.get_size()} (Expected: 2)")

def check_exercise_3():
    """Test Exercise 3: Time-Based Cache"""
    print("\nTesting Exercise 3: Time-Based Cache")
    cache = Exercise3Cache()
    
    # Test put and get
    cache.put("A", 1, 60)
    print(f"Value for key 'A': {cache.get('A')} (Expected: 1)")
    
    # Test remove
    cache.remove("A")
    print(f"Value after removal: {cache.get('A')} (Expected: None)")
    
    # Test clear_expired
    cache.put("B", 2, 0)  # Expires immediately
    cache.clear_expired()
    print(f"Value for expired key 'B': {cache.get('B')} (Expected: None)")

def check_exercise_4():
    """Test Exercise 4: Priority Queue with Update Priority"""
    print("\nTesting Exercise 4: Priority Queue with Update Priority")
    pq = Exercise4PriorityQueue()
    
    # Test add_task and get_highest_priority
    pq.add_task("Task A", 3)
    pq.add_task("Task B", 1)
    pq.add_task("Task C", 2)
    print(f"Highest priority task: {pq.get_highest_priority()} (Expected: Task A)")
    
    # Test update_priority
    pq.add_task("Task D", 2)
    pq.update_priority("Task D", 4)
    print(f"Highest priority task after update: {pq.get_highest_priority()} (Expected: Task D)")

def main():
    """Run all exercise tests."""
    check_exercise_1()
    check_exercise_2()
    check_exercise_3()
    check_exercise_4()

if __name__ == "__main__":
    main() 