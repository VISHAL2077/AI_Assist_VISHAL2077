
#write a python code for simple login system where the code has to check
#Whether credentials are hardcoded
#Whether passwords are stored or compared in plain text
#Whether insecure logic is used
#code should cater for all the above points and Identification of security risks Then, revise the code to improve security .
'''
import string
def count_vowels_case_insensitive(input_string):
    vowels = "aeiou"
    count = sum(1 for char in input_string.lower() if char in vowels)
    return count
# Example usages
example1 = "This is a Test String!"
example2 = "Another Example, with Punctuation."
example3 = "   Spaces   and Vowels!  "
print(f"The number of vowels in '{example1}' is {count_vowels_case_insensitive(example1)}")
print(f"The number of vowels in '{example2}' is {count_vowels_case_insensitive(example2)}")
print(f"The number of vowels in '{example3}' is {count_vowels_case_insensitive(example3)}")

# Simple login system with improved security
import hashlib
def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()
def verify_password(stored_password_hash, provided_password):
    """Verify a stored password against one provided by user."""
    return stored_password_hash == hash_password(provided_password)
# Simulated user database with hashed passwords
user_db = {
    "user1": hash_password("SecurePassword123"),
    "user2": hash_password("Another$trongP@ss") 
}
def login(username, password):
    if username in user_db:
        if verify_password(user_db[username], password):
            return "Login successful!"
        else:
            return "Invalid password."
    else:
        return "Username not found."
# Example usage
print(login("user1", "SecurePassword123"))  # Should print "Login successful!"
print(login("user2", "WrongPassword"))      # Should print "Invalid password."
print(login("user3", "NoSuchUser"))         # Should print "Username not found."
'''
'''
#Design a loan approval system in Python that takes applicant details including name, gender, income, and credit score.
#Test the system using applicants with identical financial profiles but different names and genders.
#Analyze whether approval decisions show bias based on gender or name.
#Identify biased logic (if any) and suggest methods to reduce or eliminate such bias.
'''
'''
def loan_approval_system(applicant):
    # Unbiased criteria for loan approval
    income_threshold = 50000
    credit_score_threshold = 650
    if applicant['income'] >= income_threshold and applicant['credit_score'] >= credit_score_threshold:
        return "Approved"
    else:
        return "Denied" 
# Test applicants
applicants = [
    {"name": "Alice", "gender": "Female", "income": 60000, "credit_score": 700},
    {"name": "Bob", "gender": "Male ", "income": 60000, "credit_score": 700},
    {"name": "Charlie", "gender": "Male", "income": 40000, "credit_score": 700},
    {"name": "Diana", "gender": "Female", "income": 60000, "credit_score": 600}
]   
for applicant in applicants:
    decision = loan_approval_system(applicant)
    print(f"Applicant: {applicant['name']}, Gender: {applicant['gender']}, Decision: {decision}")

# Example usages
example1 = "This is a Test String!"
example2 = "Another Example, with Punctuation."
example3 = "   Spaces   and Vowels!  "
print(f"The number of vowels in '{example1}' is {count_vowels_case_insensitive(example1)}")
print(f"The number of vowels in '{example2}' is {count_vowels_case_insensitive(example2)}")
print(f"The number of vowels in '{example3}' is {count_vowels_case_insensitive(example3)}") 
'''
'''
Generate a Python program that implements recursive binary search on a sorted list.
Include clear inline comments and a step-by-step explanation of the recursive logic.
Explain the base case and recursive case explicitly.
Evaluate whether the code and explanation are clear and understandable for beginners.
'''
'''
def recursive_binary_search(arr, target, low, high):
    """
    Perform a recursive binary search on a sorted list.

    Parameters:
    arr (list): A sorted list of elements to search.
    target: The element to search for.
    low (int): The lower index of the current search range.
    high (int): The upper index of the current search range.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    # Base case: If the range is invalid, the target is not in the list
    if low > high:
        return -1  # Target not found

    # Calculate the middle index
    mid = (low + high) // 2

    # Check if the target is at the mid index
    if arr[mid] == target:
        return mid  # Target found at index mid
    # If the target is less than the middle element, search in the left half
    elif target < arr[mid]:
        return recursive_binary_search(arr, target, low, mid - 1)
    # If the target is greater than the middle element, search in the right half
    else:
        return recursive_binary_search(arr, target, mid + 1, high)

def count_vowels_case_insensitive(input_string):
    vowels = "aeiou"
    count = sum(1 for char in input_string.lower() if char in vowels)
    return count      
# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = 7
result_index = recursive_binary_search(sorted_list, target_value, 0, len(sorted_list) - 1)
if result_index != -1:
    print(f"Target {target_value} found at index {result_index}.")  
else:
    print(f"Target {target_value} not found in the list.")
# Example usages
example1 = "This is a Test String!"
example2 = "Another Example, with Punctuation."
example3 = "   Spaces   and Vowels!  "
print(f"The number of vowels in '{example1}' is {count_vowels_case_insensitive(example1)}")
print(f"The number of vowels in '{example2}' is {count_vowels_case_insensitive(example2)}")
print(f"The number of vowels in '{example3}' is {count_vowels_case_insensitive(example3)}")
'''

#Generate a Python-based job applicant scoring system using skills, experience, and education.
#Analyze the code to identify any bias or ethical issues in the scoring logic.
'''
def score_applicant(applicant):
    """
    Score a job applicant based on skills, experience, and education.

    Parameters:
    applicant (dict): A dictionary containing applicant details.

    Returns:
    int: The total score of the applicant.
    """
    score = 0
    # Scoring based on skills
    skill_scores = {
        "Python": 30,
        "Java": 25,
        "C++": 20,
        "JavaScript": 15
    }
    for skill in applicant['skills']:
        score += skill_scores.get(skill, 0)

    # Scoring based on years of experience
    score += applicant['experience'] * 10  # 10 points per year of experience

    # Scoring based on education level
    education_scores = {
        "High School": 10,
        "Bachelor's": 20,
        "Master's": 30,
        "PhD": 40
    }
    score += education_scores.get(applicant['education'], 0)

    return score    

# Example usage
applicants = [
    {"name": "Alice", "skills": ["Python", "Java"], "experience": 5, "education": "Master's"},
    {"name": "Bob", "skills": ["C++", "JavaScript"], "experience": 3, "education": "Bachelor's"},
    {"name": "Charlie", "skills": ["Python", "C++", "JavaScript"], "experience": 7, "education": "PhD"}
]
for applicant in applicants:
    total_score = score_applicant(applicant)
    print(f"Applicant: {applicant['name']}, Total Score: {total_score}")
# Example usages
example1 = "This is a Test String!"
example2 = "Another Example, with Punctuation." 
example3 = "   Spaces   and Vowels!  "
print(f"The number of vowels in '{example1}' is {count_vowels_case_insensitive(example1)}")
print(f"The number of vowels in '{example2}' is {count_vowels_case_insensitive(example2)}")
print(f"The number of vowels in '{example3}' is {count_vowels_case_insensitive(example3)}")
'''
'''
Generate a Python code snippet that processes user or employee details.
Analyze the code for gender-specific variables, identity-based assumptions, or non-inclusive logic.
Revise the code to use gender-neutral variable names and inclusive design practices.
Briefly explain what was non-inclusive and how inclusiveness was improved.
'''
def process_employee_details(employee):
    """
    Process employee details in an inclusive manner.

    Parameters:
    employee (dict): A dictionary containing employee details.

    Returns:
    str: A summary of the employee details.
    """
    # Using gender-neutral variable names
    name = employee['name']     
    role = employee['role']
    department = employee['department']
    return f"Employee Name: {name}, Role: {role}, Department: {department}"

def count_vowels_case_insensitive(input_string):
    vowels = "aeiou"
    count = sum(1 for char in input_string.lower() if char in vowels)
    return count

# Example usage
employee_info = {
    "name": "Jordan Smith",
    "role": "Software Engineer",
    "department": "Development"
}
summary = process_employee_details(employee_info)
print(summary)

# Example usages
example1 = "This is a Test String!"
example2 = "Another Example, with Punctuation."
example3 = "   Spaces   and Vowels!  "
print(f"The number of vowels in '{example1}' is {count_vowels_case_insensitive(example1)}")
print(f"The number of vowels in '{example2}' is {count_vowels_case_insensitive(example2)}")
print(f"The number of vowels in '{example3}' is {count_vowels_case_insensitive(example3)}")
