import os
#os.environ.get('PATH') 取得所有環境變數
os.environ.get('PATH')
home=os.path.expanduser('~')
pict_path=os.path.join(home,'pictures','照片.jpg')
#isfile - os.path.isfile
#isdir - os.path.isdir

os.path.expanduser('~')
path=r'/Users/linzongqing/Python/python/data'
os.walk(path)
for dir_path,dir_names,file_names in os.walk(path):
    print('目前路徑：',dir_path)
    if len(dir_names) != 0:
        print('子目錄',dir_names)
    else:
        print('這裡沒有子目錄')
    if len(file_names) != 0:
        print('檔案',file_names)
    else:
        print('這裡沒有檔案')
    for f in file_names:
        print('檔案完整路徑：',os.path.join(dir_path,f))
        