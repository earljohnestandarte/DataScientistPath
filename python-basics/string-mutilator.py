def mutilator(text, remove, upper, reverse):
    if(remove):
        translation = text.maketrans('','',remove)
        text = text.translate(translation)

    if(upper == True):
        text = text.upper()

    if(reverse == True):
        text = text[::-1]

    return text

print(mutilator("Hello World", "lo", True, True))