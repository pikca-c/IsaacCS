#Bsearch finds whether the value is in slist
def Bsearch(slist,value):
    lb = 0
    ub = len(slist)-1
    found = False
    while found == False and ub >= lb:
        mid = (lb+ub)//(2)
        if slist[mid] == value:
            found = True
            break
        elif slist[mid] > value:
            ub = mid - 1
        else:
            lb = mid + 1
    return found

#Sample use, returns False
print(Bsearch([1,2,3,4,5],7))
#Sample use, returns True
print(Bsearch([1,2,3,4,5],1))
