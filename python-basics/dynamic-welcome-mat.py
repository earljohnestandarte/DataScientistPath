name: str = input("Please enter your name: ")
age: int = input("Please enter your age: ")

try:
    if int(age) < 18:
        print(f"Welcome, {name} you are a minor")
    else:
        print(f"Welcome, {name} you are an adult")
except ValueError:
    print(f"Invalid age input: {age}")
