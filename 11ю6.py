def who_are_you_and_hello():
    name = input()
    print(name.count(" "))
    print(name.isalpha())
    print(name[0].isupper())
    print(name[1:].islower())
    if name.count(" ") == 0 and name.isalpha() and name[0].isupper() and name[1:].islower():
        print("Привет,", name + "!")
    else:
        who_are_you_and_hello()



who_are_you_and_hello()