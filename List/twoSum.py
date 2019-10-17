def removeEvne(list):
    l = []
    for n in list:
        if n%2 != 0:
            l.append(n)

    return l

def removeEvne2(list):
   return [num for num in list if num%2 != 0]



print(removeEvne([1,2,4,5,10,6,3]))
print(removeEvne2([1,2,4,5,10,6,3]))