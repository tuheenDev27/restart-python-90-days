# Write an if-else statement in Python to check if a number is positive or negative.
number  = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# create a loop that print all even numbers from 1 to 20
for num in range(1, 20):
    if num % 2 == 0:
        print(num)

# Use a while loop to sum the individual digits of a given integer.
user_input = input("Enter an integer: ")
sum_of_digits = 0
while user_input.isdigit() and int(user_input) > 0:
    sum_of_digits += int(user_input) % 10
    user_input = str(int(user_input) // 10)
print("The sum of the digits is:", sum_of_digits)

# Iterate through the string "Python" and print each character on a new line.
char = "python"
for char in "Python":
    print(char[0], end="\n")

# Write a loop that uses break when it hits a multiple of 7, and continue to skip multiples of 3.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    if i % 7 == 0:
        break
    print(i)