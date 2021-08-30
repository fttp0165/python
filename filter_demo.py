def filter_lt(predicate,lt):
    result=[]
    for elem in lt:
        if predicate(elem):
            result.append(elem)
    return result

def len_greater_than_6(elem):
    return len(elem) > 6

def len_less_than_5(elem):
    return len(elem) < 5

def has_i(elem):
    return 'i' in elem
    
    