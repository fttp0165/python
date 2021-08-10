import random

coin_List=[]
for i in range(100):
    coin=random.randint(0,1)
    if coin == 0:
        coin_List.append('T')
    