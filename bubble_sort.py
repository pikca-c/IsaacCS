def bubbleSort(someList):
  index1 = 1
  while index1 < len(someList):
    index1 = index1 + 1
    index2 = 1
    while index2 < len(someList):
      if someList[index2-1] > someList[index2]:
        print("Ready to bubble ", someList[index2-1])
        h = input()
        tmp = someList[index2-1]
        someList[index2-1] = someList[index2]
        someList[index2] = tmp
      print("List looks like this: ", someList)
      index2  = index2 + 1
  return someList
    
    
print(bubbleSort([8,7,5,3]))
