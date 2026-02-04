'''
def add(a, b):
    return a + b
'''
'''
def count_down(n):
    while n >= 0:
        print(n)
        n -= 1
'''
'''
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
print(divide(10, 0))
'''
'''
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
'''
numbers = [1, 2, 3]
if len(numbers) > 5:
    print(numbers[5])
else:
    print("Index out of range")