import pyperclip
while True:
    string = input("Enter string: ")
    final = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    for x in list(string):

        # parse for emoji-able characters
        if x in list(alphabet):
            final += ":regional_indicator_"+x+": "
        if x == " ":
            final += "\n"
        if x == "0":
            final += ":zero: "
        if x == "1":
            final += ":one: "
        if x == "2":
            final += ":two: "
        if x == "3":
            final += ":three: "
        if x == "4":
            final += ":four: "
        if x == "5":
            final += ":five: "
        if x == "6":
            final += ":six: "
        if x == "7":
            final += ":seven: "
        if x == "8":
            final += ":eight: "
        if x == "9":
            final += ":nine: "
        if x == "!":
            final += ":exclamation: "
        if x == "?":
            final += ":question: "
        if x == ">":
            final += ":arrow_forward: "
        if x == "<":
            final += ":arrow backward: "

    # copy it
    print(final)
    pyperclip.copy(final)
