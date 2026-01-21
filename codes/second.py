#write a code that have palindrome-checking function def is_palindrome(s):
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]
# Example usage
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hello"))  # False  
print(is_palindrome("racecar"))  # True
print(is_palindrome("12321"))  # True
print(is_palindrome("12345"))  # False
#user-defined test cases
print(is_palindrome(input())) # Takes user input and checks if it's a palindrome
