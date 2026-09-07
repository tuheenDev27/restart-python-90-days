# Define a function that takes two numbers and returns their product.
def multiply_num(num1, num2):
    return num1 * num2

result = multiply_num(7, 5.4)
print(result)

# Write a function with a default parameter (e.g., def greet(name, greeting="Hello")).
def student_greeting(name, greeting="hello"):
    return f"{ greeting}, {name}!"

name = input("Enter your name: ")
greeting_message = student_greeting(name)
print(greeting_message)


# Create a function that checks whether a given string is a palindrome.
def is_palindrome(s):
    # Remove spaces and convert to lowercase for accurate comparison
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

 
resulrt = is_palindrome("A man a plan a canal Panama")
print(resulrt)  

# Write a function accepting an arbitrary number of arguments (*args) that returns their average.
def avarage(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

result = avarage(1, 2, 3, 4, 5)
print(result)