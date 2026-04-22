# Week 3 - Exercise 02: Operators and Conditional Logic
# Question 1: Arithmetic and Assignment Operators

# Starting values
x = 10
y = 4

# TODO: Add 3 to x using the += operator
x += 3

# TODO: Multiply y by 2 using the *= operator
y *= 2

# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y

# TODO: Print the value of 'result'
print("Question 1 - Result:", result)



# Question 2: Comparison and Logical Operators

# Starting values
a = 15
b = 8
c = 10

# TODO: Create a condition that checks if a is greater than b
condition1 = a > b

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
# A number is even if divided by 2, the remainder is 0
condition2 = b % 2 == 0

# TODO: Create a condition that checks if c is less than or equal to a
condition3 = c <= a

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
# The 'final_condition' should be True if either:
#     - a is greater than b, or
#     - b is even and c is less than or equal to a
final_condition = condition1 or (condition2 and condition3)

# TODO: Print the value of 'final_condition'
print("Question 2 - Final condition:", final_condition)



# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("Enter your test score (0-100): "))

# TODO: Implement a grading system using if-elif-else statements:
#     90-100: A
#     80-89: B
#     70-79: C
#     60-69: D
#     Below 60: F
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
else:
    grade = "F"

# TODO: Print the grade for the given score
print("Question 3 - Your grade is:", grade)



# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation (+, -, *, /): ")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
# TODO: Handle the case of division by zero
if operation == "+":
    calc_result = num1 + num2
elif operation == "-":
    calc_result = num1 - num2
elif operation == "*":
    calc_result = num1 * num2
elif operation == "/":
    if num2 == 0:
        calc_result = "Error: Cannot divide by zero!"
    else:
        calc_result = num1 / num2
else:
    calc_result = "Error: Invalid operation!"

# TODO: Print the result of the operation
print("Question 4 - Result:", calc_result)
