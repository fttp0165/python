import os
#read current file
file_loc='/Users/linzongqing/Python/python'
location=os.getcwd()
file_contant=os.listdir(path='.')

# for file_item in file_contant:
#     if file_item == "sketch.txt":
#         print("file exist")

def checkFile(file_path,file):
    file_contant = os.listdir(path=file_path)
    File_exist=False
    for file_item in file_contant:
        if file_item == file:
            File_exist=True
    return File_exist
file_exist=checkFile('.', "sketch.txt")
print(file_exist)
if file_exist:
    the_file=open('sketch.txt')
    for each_line in the_file:
        #print(the_file.readline(), end='')
        try:
            #if not each_line.find(':') == -1:
            (role,line_spoken)=each_line.split(':',1)
            print(role,end='')
            print(' said:', end='')
            print(line_spoken, end='')
        except:
            pass
    the_file.seek(0)
    the_file.close()







