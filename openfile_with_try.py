import os
os.chdir('D:\Benny_document\python\python_HeadFirst\data')
man=[]
other=[]
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role ==  'Man':
                man.append(line_spoken)
            elif role =='Other Man':
                other.append(line_spoken)
            # print(role,end='')
            # print(' said:',end='')
            # print(line_spoken,end='')
         
        except ValueError:
            pass
    out=open("data.out","w")
    print("open",file=out)
    out.close()
    data.close()

except IOError:
    print('The datafile is missing')

try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt', 'w')
    print(man,file=man_file)
    print(other, file=other_file)
   
except IOError:
    print("File error")
# print(man)
# print(other)
finally:
     man_file.close()
     other_file.close()
