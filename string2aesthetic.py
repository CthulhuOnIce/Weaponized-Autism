import pyperclip
while True:
    string = input("Enter string: ")
    final = ""
    for x in list(string):
        final += x+" "
    print(final)
    pyperclip.copy(final)
