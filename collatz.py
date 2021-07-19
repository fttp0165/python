#
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3*number+1
    

for i in range(50):
    print(collatz(i))
k=0
print("type number")
while k != 1:
    print("type " ,end='')
    try:
        inputNumber=input()
        k = collatz(int(inputNumber))
        print("back",k)
    except:
        print("please type in number")



 
