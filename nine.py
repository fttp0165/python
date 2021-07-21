
for i in range(1,10):
    for x in range(1,10):
        print(str(i*x),end=' ')
        if i*x < 10:
            print(end=' ') 
    print('')    
