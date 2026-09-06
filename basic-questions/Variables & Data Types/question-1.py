# string_variable = input("Enter a string: ")
# integer_variable = int(input("Enter a  integer value: "))
# float_variable = float(input("Enter a float value: "))
# booolen_value = bool(input("Enter a boolean value (True/False): "))

# # convert string to integer
# coverted_number = int(string_variable)
# if type(converted_number) == int:
#     print("The string has been successfully converted to an integer.")

# write a script to swap the values of two variables
val1 = input("Enter the first value: ")
print(val1)
val2 = input("Enter the second  value:")
print(val2)
val1, val2 = val2, val1
print("After swapping:")
print("First value:", val1)
print("Second value:", val2)

# extract the first and last  charactor pf the string
str_value = input("Enter a string: ")
total_length = len(str_value)
print(str_value[0], str_value[total_length - 1])


# formapt a string to output "my name is [name] and I am [age] years old.
name = input("Enter your name:")
age = int(input("Enter your age:"))
print(f'My name is {name} and I am {age} years old.')