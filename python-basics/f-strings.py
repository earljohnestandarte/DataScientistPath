# This is the "Pythonic f-strings"

# Old and chunky way:
name = "Earl John"
age = 21
print("Hello I am "+name+" and I am "+str(age)+" years old")

# Better .format() way
print("Hello I am {} and I am {} years old".format(name,age))

# Pythonic f-strings way
print(f"Hello I am {name} and I will be {age+5} years old in 5 years")