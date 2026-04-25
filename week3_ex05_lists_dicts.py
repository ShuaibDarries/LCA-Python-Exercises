
# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# TODO: Add a fruit to the end of the list
fruits.append("fig")

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "grape")

# TODO: Remove a fruit from the list
fruits.remove("banana")

# TODO: Print the modified list
print(fruits)



# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# TODO: Create a new list with each number squared
squared_numbers = [num ** 2 for num in numbers]

# TODO: Find the sum and average of the original numbers
total_sum = sum(numbers)
average = total_sum / len(numbers)

# TODO: Print the results
print("Squared Numbers:", squared_numbers)
print("Sum:", total_sum)
print("Average:", average)



# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi"
}

# TODO: Add a new country-capital pair
countries["Germany"] = "Berlin"

# TODO: Update the capital of an existing country
countries["India"] = "Delhi"

# TODO: Remove a country-capital pair
del countries["France"]

# TODO: Print the modified dictionary
print(countries)



# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "date": "brown",
    "elderberry": "purple"
}

# TODO: Print all the fruits (keys)
keys = fruit_colors.keys()
print(keys)

# TODO: Print all the colors (values)
values = fruit_colors.values()
print(values)

# TODO: Print each fruit and its color
for fruit, color in fruit_colors.items():
    print(f"{fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color
# TODO: Check if "banana" is in the dictionary and print its color
if "banana" in fruit_colors:
    print(f"The color of banana is {fruit_colors['banana']}")
    
        
