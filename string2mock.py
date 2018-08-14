import pyperclip
up = True
while True:
    string = input("Enter string: ")
    final = ""
    for x in list(string):
        if up:
            if x == " ":
                # don't alternate caps if theres a space
                final += x
                continue
            final += x.upper()
            up = False
        elif not up:
            if x == " ":
                # don't alternate caps if theres a space
                final += x
                continue
                continue
            final += x.lower()
            up = True
    print(final)
    pyperclip.copy(final)