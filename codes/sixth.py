#write a python code to to generate a student class with attributes: name, roll_no, and marks, 
# Add a method is_pass() that returns whether the student has passed (marks ≥ 40).
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40
# Example usage:
student1 = Student("Alice", 1, 45)
print(f"Student: {student1.name}, Roll No: {student1.roll_no}, Marks: {student1.marks}, Passed: {student1.is_pass()}")  
student2 = Student("Bob", 2, 35)
print(f"Student: {student2.name}, Roll No: {student2.roll_no}, Marks: {student2.marks}, Passed: {student2.is_pass()}")

#write a python for loop to print right angle triangle pattern with stars pattern with given number of rows
def print_triangle_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)
# Example usage:
print_triangle_pattern(5)

#write a python while loop to print right angle triangle 
# pattern with stars pattern with given number of rows
def print_triangle_pattern_while(rows):
    i = 1
    while i <= rows:
        print('*' * i)
        i += 1
# Example usage:
print_triangle_pattern_while(5)

#write a python function that checks whether a given 
# number is positive, negative, or zero using if-elif-else
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"  
# Example usage:
print(check_number(10))   # Output: Positive
print(check_number(-5))   # Output: Negative
print(check_number(0))    # Output: Zero

'''
write a python function check_discount(age, is_member) that
determines discount eligibility:
age ≥ 60 → Senior discount
member → Additional discount
also use nested if statements.
'''
def check_discount(age, is_member):
    if age >= 60:
        discount = "Senior discount"
        if is_member:
            discount += " with Additional member discount"
    else:
        if is_member:
            discount = "Member discount"
        else:
            discount = "No discount"
    return discount 
# Example usage:
print(check_discount(65, True))   # Output: Senior discount with Additional member discount
print(check_discount(30, True))   # Output: Member discount
print(check_discount(70, False))  # Output: Senior discount

#write a python Circle class with methods to calculate area () and circumference () given the radius
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius
# Example usage:
circle = Circle(5)
print(f"Area: {circle.area()}")                 # Output: Area: 78.53981633974483
print(f"Circumference: {circle.circumference()}")  # Output: Circumference: 31.41592653589793