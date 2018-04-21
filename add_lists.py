def memberwiseAddition(l1, l2):
    new = [sum(x) for x in zip(l1, l2)]
    return new

list_1 = [1,2,3,4]
list_2 = [2,3,4]
n = memberwiseAddition(list_1, list_2)
print(n)