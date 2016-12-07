a = [2,4,10,16]
def multiply(list,multiplier):
    for counter in range(len(list)):
        list[counter]=list[counter] * multiplier
    return list



print multiply(a,5)
