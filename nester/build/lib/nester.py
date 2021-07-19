"""
This is the standard way to include a multiple-line
comment in your code.
"""
def print_lol(the_list,indent=False,Level=0):
    for each_list in the_list:
        if isinstance(each_list,list):
            print_lol(each_list,indent, Level+1)
        else:
            if indent:
                for tab_stop in range(Level):
                    print("\t",end='')
            print(each_list)




