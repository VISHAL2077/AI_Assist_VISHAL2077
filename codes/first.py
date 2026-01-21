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

#write a python code to An recursive Fibonacci implementation
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_recursive(n - 1)
        series.append(series[-1] + series[-2])
        return series   
n = int(input("Enter the Number of terms: "))
fib_series_recursive = fibonacci_recursive(n)   
print(fib_series_recursive)
