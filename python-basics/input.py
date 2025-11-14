# print(): Prints to the console. By default, it adds a newline (\n) at the end. You can change this: print("Hello", end=" ").
#
# input(): Always returns a string. You must explicitly cast it if you need a number.
name = input("Enter your name: ")
age_str = input("Enter your age: ")

try:
    age_num = int(age_str)
    print(f"{name} is {age_num} years old")
except ValueError:
    print("Please enter a valid age")
