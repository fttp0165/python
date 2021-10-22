import os
current_lo=os.getcwd()
print("current location:",current_lo)
os.chdir('D:\Benny_document\python\python_HeadFirst\data')
print('change location...')
current_lo = os.getcwd()
print("current location:", current_lo)
if os.path.exists('sketch.txt'):
    data=open('sketch.txt')
    print(data.readline(),end='')
    print(data.readline(), end='')
    data.seek(0)
    print('return to start....')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role,line_spoken)=each_line.split(":",1)
            print(role,end='')
            print(' said:', end='')
            print(line_spoken,end='')

    data.close()
else:
    print('The data file is missing!')
    
print('\n')
print('close sketch.txt....',end='')
