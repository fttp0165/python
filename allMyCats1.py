# catName1='Zophie'
# catName2='Pooka'
# catName3='Simon'
# catName4='Lady Macbeth'
# catName5='Fat-tail'
# catName6='Miss Cleo'
# catNmaes = ['Zophie', 'Pooka', 'Simon', 'Lady Macbeth', 'Fat-tail', 'Miss Cleo']
catNmaes=[]
while True:
    print('Enter the name of cat' + str(len(catNmaes)+1)+'(Or enter nothing to stop.):')
    name=input()
    if name == '':
        break
    catNmaes=catNmaes+[name]

print('The cat names are:')
for name in catNmaes:
    print(' '+name)
