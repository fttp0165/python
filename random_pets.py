import random

pet1 = ['cat','cat','moose']
pet2 = ['pig','bird','donkey']
pet3 = ['cat', 'cat', 'cat']
pets=[pet1,pet2,pet3]
got_pet =''
gift={}
for i in range(100):
    got_pet = random.choice(random.choice(pets))
    if got_pet in gift:
        gift[got_pet]+=1
    else:
        gift[got_pet]=1
    
print(gift)
