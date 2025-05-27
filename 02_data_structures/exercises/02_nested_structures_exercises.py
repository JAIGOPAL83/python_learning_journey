#!/usr/bin/env python3
"""
Practice exercises for nested data structures.
Focus on manipulating and extracting data from complex nested structures.
"""

from typing import List, Dict, Any
from collections import defaultdict

def exercise_1(data: Dict[str, List[Dict]]) -> List[str]:
    """
    Exercise 1: Extract Unique Technologies
    
    Task: Given a nested structure of company data, extract a sorted list of
    unique technologies used across all departments in all companies.
    
    Example structure:
    {
        'companies': [
            {
                'name': 'TechCorp',
                'departments': [
                    {'name': 'Engineering', 'technologies': ['Python', 'JavaScript']},
                    {'name': 'Design', 'technologies': ['Figma', 'JavaScript']}
                ]
            },
            {
                'name': 'DataCo',
                'departments': [
                    {'name': 'Analytics', 'technologies': ['Python', 'R']},
                ]
            }
        ]
    }
    
    Expected output: ['Figma', 'JavaScript', 'Python', 'R']
    """
    # Your solution here
    # solution = sorted(set(
    #     tech
    #     for company in data['companies']
    #     for dept in company['departments']
    #     for tech in dept['technologies']
    # ))
    solution = []
    
    return solution

def exercise_2(data: Dict[str, List[Dict]]) -> Dict[str, int]:
    """
    Exercise 2: Department Statistics
    
    Task: Given the organization data, count how many employees in each department
    have more than 2 years of experience.
    
    Example structure:
    {
        'departments': [
            {
                'name': 'Engineering',
                'employees': [
                    {'name': 'Alice', 'experience': 3},
                    {'name': 'Bob', 'experience': 1},
                    {'name': 'Charlie', 'experience': 5}
                ]
            },
            {
                'name': 'Design',
                'employees': [
                    {'name': 'David', 'experience': 2},
                    {'name': 'Eve', 'experience': 4}
                ]
            }
        ]
    }
    
    Expected output: {'Engineering': 2, 'Design': 1}
    """
    # Your solution here
    # solution = {
    #     dept['name']: len([
    #         emp for emp in dept['employees']
    #         if emp['experience'] > 2
    #     ])
    #     for dept in data['departments']
    # }
    solution = {}
    
    return solution

def exercise_3(data: Dict[str, List[Dict]]) -> Dict[str, List[str]]:
    """
    Exercise 3: Project Dependencies
    
    Task: Given a structure of projects and their dependencies, create a dictionary
    where keys are programming languages and values are lists of projects using them.
    
    Example structure:
    {
        'projects': [
            {
                'name': 'Web App',
                'dependencies': [
                    {'language': 'Python', 'libraries': ['Django', 'Requests']},
                    {'language': 'JavaScript', 'libraries': ['React']}
                ]
            },
            {
                'name': 'Mobile App',
                'dependencies': [
                    {'language': 'JavaScript', 'libraries': ['React Native']},
                    {'language': 'Python', 'libraries': ['FastAPI']}
                ]
            }
        ]
    }
    
    Expected output: {
        'Python': ['Web App', 'Mobile App'],
        'JavaScript': ['Web App', 'Mobile App']
    }
    """
    # Your solution here
    # result = defaultdict(list)
    # for project in data['projects']:
    #     for dep in project['dependencies']:
    #         result[dep['language']].append(project['name'])
    # solution = {k: sorted(set(v)) for k, v in result.items()}
    solution = {}
    
    return solution

def exercise_4(data: Dict[str, Any]) -> Dict[str, Dict[str, int]]:
    """
    Exercise 4: Advanced Metrics
    
    Task: Given a nested structure of sales data, calculate the total revenue
    and average order value for each product category.
    
    Example structure:
    {
        'sales': {
            'electronics': [
                {'product': 'laptop', 'price': 1000, 'quantity': 2},
                {'product': 'phone', 'price': 500, 'quantity': 3}
            ],
            'books': [
                {'product': 'python_book', 'price': 40, 'quantity': 5},
                {'product': 'js_book', 'price': 35, 'quantity': 4}
            ]
        }
    }
    
    Expected output: {
        'electronics': {'total_revenue': 3500, 'avg_order': 750},
        'books': {'total_revenue': 340, 'avg_order': 37.5}
    }
    """
    # Your solution here
    # solution = {}
    # for category, items in data['sales'].items():
    #     total_revenue = sum(item['price'] * item['quantity'] for item in items)
    #     avg_order = total_revenue / len(items)
    #     solution[category] = {
    #         'total_revenue': total_revenue,
    #         'avg_order': avg_order
    #     }
    solution = {}
    
    return solution

def check_exercise(exercise_func, test_data, expected_output):
    """Helper function to check exercise results."""
    result = exercise_func(test_data)
    print(f"\nTesting {exercise_func.__name__}:")
    print(f"Your output: {result}")
    print(f"Expected output: {expected_output}")
    print(f"{'✓ Correct!' if result == expected_output else '✗ Not quite right.'}")

def main():
    """Run all exercises with test data."""
    # Test data for Exercise 1
    companies_data = {
        'companies': [
            {
                'name': 'TechCorp',
                'departments': [
                    {'name': 'Engineering', 'technologies': ['Python', 'JavaScript']},
                    {'name': 'Design', 'technologies': ['Figma', 'JavaScript']}
                ]
            },
            {
                'name': 'DataCo',
                'departments': [
                    {'name': 'Analytics', 'technologies': ['Python', 'R']},
                ]
            }
        ]
    }
    
    # Test data for Exercise 2
    org_data = {
        'departments': [
            {
                'name': 'Engineering',
                'employees': [
                    {'name': 'Alice', 'experience': 3},
                    {'name': 'Bob', 'experience': 1},
                    {'name': 'Charlie', 'experience': 5}
                ]
            },
            {
                'name': 'Design',
                'employees': [
                    {'name': 'David', 'experience': 2},
                    {'name': 'Eve', 'experience': 4}
                ]
            }
        ]
    }
    
    # Test data for Exercise 3
    projects_data = {
        'projects': [
            {
                'name': 'Web App',
                'dependencies': [
                    {'language': 'Python', 'libraries': ['Django', 'Requests']},
                    {'language': 'JavaScript', 'libraries': ['React']}
                ]
            },
            {
                'name': 'Mobile App',
                'dependencies': [
                    {'language': 'JavaScript', 'libraries': ['React Native']},
                    {'language': 'Python', 'libraries': ['FastAPI']}
                ]
            }
        ]
    }
    
    # Test data for Exercise 4
    sales_data = {
        'sales': {
            'electronics': [
                {'product': 'laptop', 'price': 1000, 'quantity': 2},
                {'product': 'phone', 'price': 500, 'quantity': 3}
            ],
            'books': [
                {'product': 'python_book', 'price': 40, 'quantity': 5},
                {'product': 'js_book', 'price': 35, 'quantity': 4}
            ]
        }
    }
    
    # Run tests
    check_exercise(exercise_1, companies_data, ['Figma', 'JavaScript', 'Python', 'R'])
    check_exercise(exercise_2, org_data, {'Engineering': 2, 'Design': 1})
    check_exercise(exercise_3, projects_data, {
        'Python': ['Web App', 'Mobile App'],
        'JavaScript': ['Web App', 'Mobile App']
    })
    check_exercise(exercise_4, sales_data, {
        'electronics': {'total_revenue': 3500, 'avg_order': 750},
        'books': {'total_revenue': 340, 'avg_order': 37.5}
    })

if __name__ == "__main__":
    main() 