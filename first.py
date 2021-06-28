movies = ["The Holy Grail",1975,
"Terry Jones & Terry Gilliam",91,
["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
print(movies)
print("----------------------------------------------------------------")
for each_movie in movies:
    if isinstance(each_movie,list):
        for each_sub_movie in each_movie:
            print(each_sub_movie)
    else:
        print(each_movie)
print("----------------------------------------------------------------")

print("****************************************************************")
#------------------------------------------------
#function
#use def 為函數提供一個函數名
# def firstFun(arf):
#     --------------------
#     |                  |
#     |    代碼           |
#     |                  |
#     --------------------
#------------------------------------------------

def print_lol(the_list):
    for each_list in the_list:
        if isinstance(each_list,list):
            print("----------------------------------------------------------------")
            print_lol(each_list)
        else:
            print(each_list)

print_lol(movies)

#-----PDF_page 60/book_page 33

