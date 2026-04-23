
# Question 1: Basic Function Definition and Calling

def greet():
    print("Hello, World!")

greet()

#----------------------------------------------------------
# Question 2: Function with Parameters

def personalized_greeting(name):
    print(f"Hello, {name}")

personalized_greeting("Shuaib")

#----------------------------------------------------------
# Question 3: Function with Return Value

def square(number):
    return number * number

result = square(5)
print(result)

#----------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

def rectangle_area(Length, Width):
    return Length * Width

area = rectangle_area(4, 5)
print(area)

#----------------------------------------------------------
# Question 5: Using a Function as an Argument

def apply_opperation(func, number):
    return func(number)

def double(number):
    return number * 2

# Use apply_operation with double and 7
print(apply_opperation(double, 7))

# Use apply_operation with square (from Question 3) and 3
print(apply_opperation(square, 3))
