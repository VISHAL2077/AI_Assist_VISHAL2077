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

#generate a breif explanation of the code above
'''
This code defines a function called is_prime that checks whether a given number is prime or not. A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. The function first checks if the number is less than or equal to 1, in which case it returns False since prime numbers are greater than 1. Then, it iterates from 2 to the square root of the number (inclusive) to check for any divisors. If it finds any number that divides evenly into the input number, it returns False, indicating that the number is not prime. If no divisors are found, it returns True, indicating that the number is prime. The example usage demonstrates how to use the function and prints whether the specified number (29 in this case) is prime or not.
'''

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

#generate a breif explanation of the code above
'''
This code defines a function called sum_of_list that takes a list of numbers as input and returns the sum of those numbers. The function initializes a variable total to zero and then iterates through each number in the input list, adding each number to the total. After processing all the numbers, it returns the final total. The example usage demonstrates how to use the function by summing a list of numbers [1, 2, 3, 4, 5] and printing the result.
''' 

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


#generate a breif explanation of the code above
''' 
This code defines a function called extract_digits that takes an alphanumeric string as input and extracts all the digits from it. The function uses a list comprehension to iterate through each character in the input string, checking if the character is a digit using the isdigit() method. If it is a digit, it is included in the resulting list. The list of digits is then joined into a single string and returned. The example usages demonstrate how to use the function with different input strings, showing the extracted digits for each case.
'''

#write a python function that counts the number of vowels in a string.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count
# Example usage
example_string = "Hello, World!"
vowel_count = count_vowels(example_string)  
print(f"The number of vowels in '{example_string}' is {vowel_count}.")


#generate a breif explanation of the code above
'''
This code defines a function called count_vowels that counts the number of vowels in a given string. The function defines a string containing all the vowels (both lowercase and uppercase) and then uses a generator expression within the sum() function to iterate through each character in the input string. For each character that is found in the vowels string, it adds 1 to the count. Finally, the function returns the total count of vowels. The example usage demonstrates how to use the function by counting the vowels in the string "Hello, World!" and printing the result.
'''

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


#generate a breif explanation of the code above
''' 
This code defines a function called count_vowels_case_insensitive that counts the number of vowels in a given string while being case insensitive and ignoring spaces and punctuation. The function first converts the input string to lowercase to ensure case insensitivity. It then uses a generator expression within the sum() function to iterate through each character in the lowercase string, checking if the character is in the defined vowels string ("aeiou"). For each vowel found, it adds 1 to the count. Finally, the function returns the total count of vowels. The example usages demonstrate how to use the function with different input strings, showing the number of vowels for each case.
'''

#generate a breif explanation of above 2 functions
'''
The first function, count_vowels, counts the number of vowels in a given string by checking each character against a predefined list of vowels (both uppercase and lowercase). It uses a generator expression to sum up the occurrences of vowels in the input string.
The second function, count_vowels_case_insensitive, performs a similar task but is designed to be case insensitive. It converts the input string to lowercase before checking for vowels, ensuring that it counts vowels regardless of their case. Both functions return the total count of vowels found in the input string.
'''

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
