'''
def is_even(num):
    return (num & 1) == 0

#genrate test cases with integer values as input
test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]
for num in test_cases:
    print(f"{num} is even: {is_even(num)}")
'''
'''
def to_uppercase(s):
    return s.upper()
def to_lowercase(s):
    return s.lower()
'''
'''
def to_uppercase(s):
    if isinstance(s, str):
        return s.upper()
    return None

def to_lowercase(s):
    if isinstance(s, str):
        return s.lower()
    return None

#genrate test cases with string values as input for both to_uppercase & to_lowercase functions that 
#handle empty string, invalid input like numbers, None and special characters, 
#mixed-cased input & normal string input
test_cases = ["hello", "WORLD", "Python3", "", None, "123", 123, 12.3, True, 'a', "!@#$%", "MiXeD CaSe"]
for s in test_cases:
    print(f"Original: '{s}' | Uppercase: '{to_uppercase(s)}' | Lowercase: '{to_lowercase(s)}'")
'''

'''
Write a Python program using Test-Driven Development (TDD) to implement a function sum_list(numbers) 
that returns the sum of all numeric elements in a list. The function must return 0 for an empty list, 
correctly handle negative numbers, and ignore or safely skip non-numeric values such as strings or None. 
Generate comprehensive AI-created test cases covering normal cases, edge cases, and mixed-type lists. 
Implement the tests using unittest, ensuring all tests validate the correctness of the function. 
Provide the complete Python code including the function implementation and the test cases
'''
'''
import unittest
def sum_list(numbers):
    if not isinstance(numbers, list):
        return 0
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
    return total
class TestSumList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_list([]), 0)

    def test_all_numeric(self):
        self.assertEqual(sum_list([1, 2, 3, 4]), 10)

    def test_mixed_types(self):
        self.assertEqual(sum_list([1, 'a', None, 2.5, '3', -1]), 2.5)

    def test_negative_numbers(self):
        self.assertEqual(sum_list([-1, -2, -3]), -6)

    def test_non_list_input(self):
        self.assertEqual(sum_list("not a list"), 0)
        self.assertEqual(sum_list(123), 0)
        self.assertEqual(sum_list(None), 0)
if __name__ == '__main__':
    unittest.main()
'''

'''
Write a Python program that implements a StudentResult class with the methods add_marks(mark), 
calculate_average(), and get_result(). The add_marks method must only accept marks between 0 and 100, 
otherwise raise an error. The calculate_average method should compute the average of all stored marks, 
and get_result should return "Pass" if average ≥ 40, otherwise "Fail". Generate comprehensive AI-created test cases 
covering normal inputs, failing averages, boundary values, and invalid marks. Implement the tests using unittest, 
and provide the complete code including the class implementation and all test cases.
'''
'''
import unittest
class StudentResult:
    def __init__(self):
        self.marks = []

    def add_marks(self, mark):
        if not isinstance(mark, (int, float)):
            raise ValueError("Mark must be a number.")
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100.")
        self.marks.append(mark)

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def get_result(self):
        average = self.calculate_average()
        return "Pass" if average >= 40 else "Fail"
class TestStudentResult(unittest.TestCase):
    def setUp(self):
        self.student = StudentResult()

    def test_add_valid_marks(self):
        self.student.add_marks(85)
        self.student.add_marks(90)
        self.assertEqual(self.student.marks, [85, 90])

    def test_add_invalid_marks(self):
        with self.assertRaises(ValueError):
            self.student.add_marks(-5)
        with self.assertRaises(ValueError):
            self.student.add_marks(105)
        with self.assertRaises(ValueError):
            self.student.add_marks("not a number")

    def test_calculate_average(self):
        self.student.add_marks(80)
        self.student.add_marks(90)
        self.assertEqual(self.student.calculate_average(), 85)

    def test_calculate_average_empty(self):
        self.assertEqual(self.student.calculate_average(), 0)

    def test_get_result_pass(self):
        self.student.add_marks(50)
        self.student.add_marks(60)
        self.assertEqual(self.student.get_result(), "Pass")

    def test_get_result_fail(self):
        self.student.add_marks(30)
        self.student.add_marks(35)
        self.assertEqual(self.student.get_result(), "Fail")
if __name__ == '__main__':
    unittest.main()
'''

'''
Write a Python program using Test-Driven Development (TDD) to implement a function is_valid_username(username) 
that validates usernames based on the following rules: minimum length of 5 characters,no spaces allowed, and only alphanumeric 
characters are permitted. Generate comprehensive AI-created test cases that include valid usernames, too-short usernames, 
usernames with spaces, and usernames containing special characters. Implement the tests using pytest to ensure the function 
passes all scenarios. Provide the complete Python code including the validation function and the corresponding test cases.
'''
'''
import re
def is_valid_username(username):
    if not isinstance(username, str):
        return False
    if len(username) < 5:
        return False
    if ' ' in username:
        return False
    if not re.match("^[a-zA-Z0-9]+$", username):
        return False
    return True
# Test cases for is_valid_username function
test_cases = [
    ("validUser", True),
    ("user", False),  # Too short
    ("user name", False),  # Contains space
    ("user@name", False),  # Contains special character
    ("user_name", False),  # Contains special character
    ("12345", True),  # Valid numeric username
    ("user123", True),  # Valid alphanumeric username
    ("", False),  # Empty string
    (None, False),  # None input
    (12345, False)  # Non-string input
]   
for username, expected in test_cases:
    result = is_valid_username(username)
    print(f"Username: '{username}' | Valid: {result} | Expected: {expected} | Test Passed: {result == expected}")
'''
