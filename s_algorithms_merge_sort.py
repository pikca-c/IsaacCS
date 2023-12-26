def mergeSort(listToSort):
    
    #if the length of the unsorted list has more than one element remaining
    print("Entering function with listToSort: ", listToSort)
    next = input()
    if len(listToSort) > 1:
        #then find mid index
        mIndex = len(listToSort) // 2
        #split into left side and right side 
        leftHalf = listToSort[:mIndex]
        rightHalf = listToSort[mIndex:]
        print("Left Half: ", leftHalf)
        mergeSort(leftHalf)
        print("Right Half: ", rightHalf)
        mergeSort(rightHalf)
    
        lIndex = 0
        rIndex = 0
        index = 0
        #when all is split up:
        #... on the return from the stack
        while lIndex < len(leftHalf) and rIndex < len(rightHalf):
            print("to merge: ", leftHalf, " and ", rightHalf)
            if leftHalf[lIndex] < rightHalf[lIndex]:
              listToSort[index] = leftHalf[lIndex]
              lIndex = lIndex + 1
              print("merged: ", listToSort)
            else:
              listToSort[index] = rightHalf[rIndex]
              rIndex = rIndex + 1
              print("merged: ", listToSort)
            index = index + 1
        #copy any remainig elements across
        while lIndex < len(leftHalf):
            listToSort[index] = leftHalf[lIndex]
            index = index + 1
            lIndex = lIndex + 1
        while rIndex < len(rightHalf):
            listToSort[index] = rightHalf[rIndex]
            index = index + 1
            rIndex = rIndex + 1

arr = [12, 11, 10, 9, 8, 7, 6, 5]  
print ("Given array is ", arr)  
mergeSort(arr) 
print("Sorted array is: ", arr) 
