import random



coin_list_total=[]
for throw in range(1000):
    coin_list=[]
    for time in range(6):
        coin_orientation = random.randint(0,1)
        if coin_orientation == 0:
            coin_list.append('T')
        else:
            coin_list.append('H')
    coin_list_total.append(coin_list)
coin_number=0

def check_list(each_coin,face):
    for coin in each_coin:
        if coin == face:
            return Fail
    return True


for index,coin in enumerate(coin_list_total):
    if 'T' not in coin:
        coin_number += 1
        print(index,coin_list)
        #print(coin,'\n')
print(coin_number)

