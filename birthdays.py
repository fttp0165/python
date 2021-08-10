birthdays={'JK Lin':'may 10'}

while True:
    name = input("Enter a name: (blank to quit):")
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+ name)
    else:
        print('I do not have birthdat for' + name)
        print("What is their birthday?")
        bday=input()
        birthdays[name]=bday
        print("Birthday database updated.")
