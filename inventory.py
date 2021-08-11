
stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
         item_total += v
         print("{}  {}".format(v,k))
    print("Total number of items:" + str(item_total))

displayInventory(stuff)

dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']

def addToInventory(inventory,addedItems):
    for think in addedItems:
        inventory.setdefault(think,0)
        inventory[think]=inventory[think] + 1
    return inventory

stuff = addToInventory(stuff,dragonLoot)
print("*******************")
print("kill dragon update ")
displayInventory(stuff)
