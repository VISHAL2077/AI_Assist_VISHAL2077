#Write a Python function to determine whether a given number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
number = 29 
if is_prime(number):
    print(f"{number} is a prime number.")   
else:
    print(f"{number} is not a prime number.")



#write a python function to sum the given list of numbers
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
# Example usage
num_list = [1, 2, 3, 4, 5]  
result = sum_of_list(num_list)
print(f"The sum of the list {num_list} is {result}.") 



#write a python function that extracts digits from an alphanumeric string. with 2-3 example usages
def extract_digits(input_string):
    digits = ''.join([char for char in input_string if char.isdigit()])
    return digits
# Example usages
example1 = "abc123xyz"  
example2 = "no_digits_here!"
example3 = "2024isTheYear"
print(f"Extracted digits from '{example1}': {extract_digits(example1)}")
print(f"Extracted digits from '{example2}': {extract_digits(example2)}")    
print(f"Extracted digits from '{example3}': {extract_digits(example3)}")




#write a python function that counts the number of vowels in a string.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count
# Example usage
example_string = "Hello, World!"
vowel_count = count_vowels(example_string)  
print(f"The number of vowels in '{example_string}' is {vowel_count}.")



#write a python function counts the number of vowels in a string. where be case insensitive, ignores spaces and punctuation.
#also provide 2-3 example usages, 
import string
def count_vowels_case_insensitive(input_string):
    vowels = "aeiou"
    count = sum(1 for char in input_string.lower() if char in vowels)
    return count
# Example usages
example1 = "Hello, World!"  
example2 = "Python is fun."
example3 = "A quick brown fox."
print(f"The number of vowels in '{example1}' is {count_vowels_case_insensitive(example1)}")
print(f"The number of vowels in '{example2}' is {count_vowels_case_insensitive(example2)}")    
print(f"The number of vowels in '{example3}' is {count_vowels_case_insensitive(example3)}") 



#write a python function that determines the minimum of three numbers without using the built-in min() function. also provide 2-3 example usages

def min_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c    
# Example usages
print(f"The minimum of (3, 1, 2) is {min_of_three(3, 1, 2)}")
print(f"The minimum of (10, 20, 5) is {min_of_three(10, 20, 5)}")       
print(f"The minimum of (-1, -5, 0) is {min_of_three(-1, -5, 0)}")       
