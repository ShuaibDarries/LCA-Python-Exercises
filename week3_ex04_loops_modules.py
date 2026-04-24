
# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)



# Question 2: Using a while loop to count down from 5

# Initializing the counter
counter = 5

# Using a while loop to count down from 5 to 1
while counter > 0:
    print(counter)
    counter -= 1



# Question 3: Using a for loop with the range function

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    print(i ** 2)



# Question 4: Using the random mdule 

# TODO: Import the random module
import random

# TODO: Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple"]

# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3) :
    random_color = random.choice(colors)
    print(random_color)



# Question 5: Creating and using a custom module

# TODO: Import the custom module and use its functions
import math_operations

# TODO: Use a while loop to create a simple calculator
while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = math_operations.add(num1, num2)
        elif choice == "2":
            result = math_operations.subtract(num1, num2)
        elif choice == "3":
            result = math_operations.multiply(num1, num2)
        elif choice == "4":
            result = math_operations.divide(num1, num2)

        print(f"Result: {result}")
    else:
        print("Invalid choice. Please try again.")