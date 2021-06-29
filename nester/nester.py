"""
This is the standard way to include a multiple-line
comment in your code.
"""
def print_lol(the_list):
    for each_list in the_list:
        if isinstance(each_list, list):
            print("----------------------------------------------------------------")
            print_lol(each_list)
        else:
            print(each_list)



