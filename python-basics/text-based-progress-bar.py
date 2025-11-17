print("This is a text based progress bar")

input("Press enter to continue")

percent_str=input("Enter a percentage between 0 and 100: ")

try:
    percent_float=float("0."+percent_str)
    number = int(percent_float*50);
    print("=" * number)
except ValueError:
    print("Please enter a percentage between 0 and 100")