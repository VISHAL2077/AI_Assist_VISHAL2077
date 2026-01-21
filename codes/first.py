'''
# optimize the code below using a function definition and removing redundant variables and simplifying the loop logic
# original code generates Fibonacci series up to n terms without using functions

def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
n = int(input("Enter the Number of terms: "))
fib_series = fibonacci_series(n)
print(fib_series)

a, b = 0, 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
'''

# write a python code to An iterative Fibonacci implementation
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
n = int(input("Enter the Number of terms: "))
fib_series = fibonacci_series(n)
print(fib_series)
