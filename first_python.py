
name="benny"
age=35
print("My name is"+name)
print("I\'m " + str(age) + " yeaes old")

#name=input("Type your name: ")

a_list=["A","B"]
s_list=[]
a_tuple=("W","E")
s_tuple=()
for i in a_list:
  print("alist",i)

for x in a_tuple:
  print("a_tuple",x)


def add(num1,num2):
    num1+num2  #沒有使用return 不會返回
  
print(add(3,5))


#dictionart

dic={"蘋果":"apple","貓":"cat"}
for i in dic:
    print(i +":"+dic[i])

class phone:
  def __init__(self,os):
    self.os=os
    


