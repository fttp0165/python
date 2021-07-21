
print("Enter lenghs:",end='')
len=input()
print("Enter unit(in or cm):",end='')
unit=input()

if unit == "in":
    result = float(len)*2.54
    print(len +"in equal "+ str(result) + "cm" )
else:
    result = float(len) / 2.54
    print(len + "cm equal " + str(result) + "in")
