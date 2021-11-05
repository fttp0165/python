import sys
admins={'Justin','caterpillar'}
users=set(sys.argv[1:])
print('站長:{}'.format(admins & users))
print('非站長:{}'.format(users - admins))
print('全部使用者:{}'.format(admins | users))
print('身分不重複使用者:{}'.format(admins ^ users))

name='Guest'
if len(sys.argv)>1:
    name = sys.argv[1]

print(f'Hello,{name}')
