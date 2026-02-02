#write a python code AI to design a simple calculator program by initially providing only the function name
'''
def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (+|-|*|/): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '-':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '*':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '/':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")
    
calculator()
'''
#update the code to handle invalid inputs gracefully like non-numeric values and unsupported operations, and add a loop to allow multiple calculations until the user decides to exit.
#also do exception handling for division by zero, and provide an option to clear the screen before each calculation.
#add a other operations used in simple calculator like modulus, exponentiation, floor division, square & cubic rooots, percentages, average of numbers, log funtions, trigonometric functions & calculus calculations.
'''
import math
import os
def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def modulus(x, y):
        return x % y

    def exponentiation(x, y):
        return x ** y

    def floor_division(x, y):
        if y == 0:
            return "Error! Division by zero."
        return x // y

    def square_root(x):
        return math.sqrt(x)

    def cubic_root(x):
        return x ** (1/3)

    def percentage(x, total):
        return (x / total) * 100

    def average(numbers):
        return sum(numbers) / len(numbers)

    def logarithm(x, base=10):
        return math.log(x, base)

    def sine(x):
        return math.sin(math.radians(x))

    def cosine(x):
        return math.cos(math.radians(x))

    def tangent(x):
        return math.tan(math.radians(x))
    
    #add ln function
    def natural_log(x):
        return math.log(x)
    
    #add base e exponentiation
    def exp_e(x):  
        return math.exp(x)
    
    #add factorial function
    def factorial(x):
        if x < 0:
            return "Error! Factorial of negative number doesn't exist."
        return math.factorial(x)
    
    #add combination function
    def combination(n, r):
        if r > n:
            return "Error! r cannot be greater than n."
        return math.comb(n, r)
    
    #add permutation function
    def permutation(n, r):
        if r > n:
            return "Error! r cannot be greater than n."
        return math.perm(n, r)
    
    #add gcd function
    def gcd(x, y):
        return math.gcd(x, y)
    
    #add lcm function
    def lcm(x, y): 
        return abs(x * y) // math.gcd(x, y)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Select operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (^)")
        print("7. Floor Division (//)")
        print("8. Square Root (√)")
        print("9. Cubic Root (∛)")
        print("10. Percentage (%)")
        print("11. Average")
        print("12. Logarithm (log)")
        print("13. Sine (sin)")
        print("14. Cosine (cos)")
        print("15. Tangent (tan)")
        print("16. Natural Log (ln)")
        print("17. Exponential (e^x)")
        print("18. Factorial (!)")
        print("19. Combination (nCr)")
        print("20. Permutation (nPr)")
        print("21. GCD")    
        print("22. LCM")
        print("23. Exit")

        choice = input("Enter choice: ")

        try:
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} % {num2} = {modulus(num1, num2)}")
                elif choice == '6':
                    print(f"{num1} ^ {num2} = {exponentiation(num1, num2)}")
                elif choice == '7':
                    print(f"{num1} // {num2} = {floor_division(num1, num2)}")
            elif choice == '8':
                num = float(input("Enter number: "))
                print(f"√{num} = {square_root(num)}")
            elif choice == '9':
                num = float(input("Enter number: "))
                print(f"∛{num} = {cubic_root(num)}")
            elif choice == '10':
                part = float(input("Enter part value: "))
                total = float(input("Enter total value: "))
                print(f"{part} is {percentage(part, total)}% of {total}")
            elif choice == '11':
                nums = list(map(float, input("Enter numbers separated by space: ").split()))
                print(f"Average = {average(nums)}")
            elif choice == '12':
                num = float(input("Enter number: "))
                base = input("Enter base (default 10): ")
                base = float(base) if base else 10
                print(f"log_{base}({num}) = {logarithm(num, base)}")
            elif choice == '13':
                angle = float(input("Enter angle in degrees: "))
                print(f"sin({angle}) = {sine(angle)}")
            elif choice == '14':
                angle = float(input("Enter angle in degrees: "))
                print(f"cos({angle}) = {cosine(angle)}")
            elif choice == '15':
                angle = float(input("Enter angle in degrees: "))
                print(f"tan({angle}) = {tangent(angle)}")
            elif choice == '16':
                num = float(input("Enter number: "))
                print(f"ln({num}) = {natural_log(num)}")
            elif choice == '17':
                num = float(input("Enter number: "))
                print(f"e^{num} = {exp_e(num)}")
            elif choice == '18':
                num = int(input("Enter non-negative integer: "))
                print(f"{num}! = {factorial(num)}")
            elif choice == '19':
                n = int(input("Enter n: "))
                r = int(input("Enter r: "))
                print(f"{n}C{r} = {combination(n, r)}")
            elif choice == '20':
                n = int(input("Enter n: "))
                r = int(input("Enter r: "))
                print(f"{n}P{r} = {permutation(n, r)}")
            elif choice == '21':
                num1 = int(input("Enter first integer: "))
                num2 = int(input("Enter second integer: "))
                print(f"GCD({num1}, {num2}) = {gcd(num1, num2)}")
            elif choice == '22':
                num1 = int(input("Enter first integer: "))
                num2 = int(input("Enter second integer: "))
                print(f"LCM({num1}, {num2}) = {lcm(num1, num2)}")
            elif choice == '23':
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input! Please enter numeric values.")    
        input("Press Enter to continue...")
calculator()
'''
#now update the above code to include a history feature that logs all calculations performed during the session and provides an option to view this history.
#aswell optimize the code for better readability and maintainability
'''
import math
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")       
def calculator():
    history = []
    operations = {
        '1': ("Add (+)", lambda x, y: x + y),
        '2': ("Subtract (-)", lambda x, y: x - y),
        '3': ("Multiply (*)", lambda x, y: x * y),
        '4': ("Divide (/)", lambda x, y: "Error! Division by zero." if y == 0 else x / y),
        '5': ("Modulus (%)", lambda x, y: x % y),
        '6': ("Exponentiation (^)", lambda x, y: x ** y),
        '7': ("Floor Division (//)", lambda x, y: "Error! Division by zero." if y == 0 else x // y),
        '8': ("Square Root (√)", lambda x: math.sqrt(x)),
        '9': ("Cubic Root (∛)", lambda x: x ** (1/3)),
        '10': ("Percentage (%)", lambda x, total: (x / total) * 100),
        '11': ("Average", lambda nums: sum(nums) / len(nums)),
        '12': ("Logarithm (log)", lambda x, base=10: math.log(x, base)),
        '13': ("Sine (sin)", lambda x: math.sin(math.radians(x))),
        '14': ("Cosine (cos)", lambda x: math.cos(math.radians(x))),
        '15': ("Tangent (tan)", lambda x: math.tan(math.radians(x))),
        '16': ("Natural Log (ln)", lambda x: math.log(x)),
        '17': ("Exponential (e^x)", lambda x: math.exp(x)),
        '18': ("Factorial (!)", lambda x: "Error! Factorial of negative number doesn't exist." if x < 0 else math.factorial(int(x))),
        '19': ("Combination (nCr)", lambda n, r: "Error! r cannot be greater than n." if r > n else math.comb(int(n), int(r))),
        '20': ("Permutation (nPr)", lambda n, r: "Error! r cannot be greater than n." if r > n else math.perm(int(n), int(r))),
        '21': ("GCD", lambda x, y: math.gcd(int(x), int(y))),
        '22': ("LCM", lambda x, y: abs(int(x) * int(y)) // math.gcd(int(x), int(y))),
    }
    while True:
        clear_screen()
        print("Select operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("23. View History")
        print("24. Exit")

        choice = input("Enter choice: ")

        if choice == '24':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice == '23':
            clear_screen()
            print("Calculation History:")
            for record in history:
                print(record)
            input("Press Enter to continue...")
            continue
        elif choice in operations:
            operation_name, operation_func = operations[choice]
            try:
                if choice in ['1', '2', '3', '4', '5', '6', '7']:
                    num1 = get_number("Enter first number: ")
                    num2 = get_number("Enter second number: ")
                    result = operation_func(num1, num2)
                    record = f"{operation_name}: {num1} and {num2} = {result}"
                elif choice in ['8', '9']:
                    num = get_number("Enter number: ")
                    result = operation_func(num)
                    record = f"{operation_name}: {num} = {result}"
                elif choice == '10':
                    part = get_number("Enter part value: ")
                    total = get_number("Enter total value: ")
                    result = operation_func(part, total)
                    record = f"{operation_name}: {part} is {result}% of {total}"
                elif choice == '11':
                    nums = list(map(float, input("Enter numbers separated by space: ").split()))
                    result = operation_func(nums)
                    record = f"{operation_name}: Average of {nums} = {result}"
                elif choice == '12':
                    num = get_number("Enter number: ")
                    base_input = input("Enter base (default 10): ")
                    base = float(base_input) if base_input else 10
                    result = operation_func(num, base)
                    record = f"{operation_name}: log_{base}({num}) = {result}"
                elif choice in ['13', '14', '15']:
                    angle = get_number("Enter angle in degrees: ")
                    result = operation_func(angle)
                    record = f"{operation_name}: {operation_name.split()[0]}({angle}) = {result}"
                elif choice == '16':    
                    num = get_number("Enter number: ")
                    result = operation_func(num)
                    record = f"{operation_name}: ln({num}) = {result}"  
                elif choice == '17':
                    num = get_number("Enter number: ")
                    result = operation_func(num)
                    record = f"{operation_name}: e^{num} = {result}"
                elif choice == '18':
                    num = get_number("Enter non-negative integer: ")
                    result = operation_func(num)
                    record = f"{operation_name}: {int(num)}! = {result}"
                elif choice in ['19', '20']:
                    n = get_number("Enter n: ")
                    r = get_number("Enter r: ")
                    result = operation_func(n, r)
                    record = f"{operation_name}: {int(n)}{operation_name[-3:]}{int(r)} = {result}"
                elif choice in ['21', '22']:
                    num1 = get_number("Enter first integer: ")
                    num2 = get_number("Enter second integer: ")
                    result = operation_func(num1, num2)
                    record = f"{operation_name}: {operation_name}({int(num1)}, {int(num2)}) = {result}"
                print(record)
                history.append(record)
            except Exception as e:
                print(f"An error occurred: {e}")    
            input("Press Enter to continue...")
        else:
            print("Invalid input")
            input("Press Enter to continue...") 
calculator()  
'''

#write a python program that sort the given student marks 
#update the code to sort in descending order
#update the code to user input for no of students and their marks and there names aswell
#and add feature to search for a particular student's marks by their name
#add exception handling for invalid inputs 0 < marks > 100
#and as per there marks assign grades A, B, C, D, F
#store the data in a dictionary with student names as keys and a tuple of (names, marks, grade) as values
#then sort the dictionary based on marks in descending order and print the sorted list of students with their marks and grades
#finally optimize the code for better readability and maintainability
'''
def get_grade(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks < 70:
        return 'D'
    elif 0 <= marks < 60:
        return 'F'
    else:
        return None
def main():
    student_data = {}
    try:
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            name = input("Enter student name: ")
            marks = float(input(f"Enter marks for {name} (0-100): "))
            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100.")
            grade = get_grade(marks)
            student_data[name] = (name, marks, grade)
        
        # Sort the dictionary based on marks in descending order
        sorted_students = dict(sorted(student_data.items(), key=lambda item: item[1][1], reverse=True))
        
        print("\nSorted Student Marks and Grades:")
        for name, (student_name, marks, grade) in sorted_students.items():
            print(f"Name: {student_name}, Marks: {marks}, Grade: {grade}")
        
        # Search for a particular student's marks by their name
        search_name = input("\nEnter a student's name to search for their marks: ")
        if search_name in student_data:
            student_name, marks, grade = student_data[search_name]
            print(f"Found - Name: {student_name}, Marks: {marks}, Grade: {grade}")
        else:
            print("Student not found.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()  
'''

#write a python code to check if a given number is prime or not
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")   
else:
    print(f"{number} is not a prime number.")
'''

#write a python code for a student to calculate their total marks, average marks, 
# and grade based on their scores for the no of subjects as per the user input and marking scheme
'''
def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'  
def main():
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        total_marks = 0
        for i in range(num_subjects):
            marks = float(input(f"Enter marks for subject {i + 1}: "))
            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100.")
            total_marks += marks
        average_marks = total_marks / num_subjects
        grade = get_grade(average_marks)
        print(f"\nTotal Marks: {total_marks}")
        print(f"Average Marks: {average_marks}")
        print(f"Grade: {grade}")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")    
if __name__ == "__main__":
    main()
'''

#write a python code to perform unit conversions between kilometers and miles,
#update the code to implement all the exception handling for invalid inputs and provide user-friendly messages. 
#also take all required constraints into consideration while writing the code.

def km_to_miles(km):
    return km * 0.621371
def miles_to_km(miles):
    return miles / 0.621371 
def main():
    try:
        print("Unit Conversion:")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        choice = input("Enter choice (1/2): ")
        if choice == '1':
            km = float(input("Enter distance in kilometers: "))
            if km < 0:
                raise ValueError("Distance cannot be negative.")
            miles = km_to_miles(km)
            print(f"{km} kilometers is equal to {miles} miles.")
        elif choice == '2':
            miles = float(input("Enter distance in miles: "))
            if miles < 0:
                raise ValueError("Distance cannot be negative.")
            km = miles_to_km(miles)
            print(f"{miles} miles is equal to {km} kilometers.")
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")    
if __name__ == "__main__":
    main()

