"""This repl was written to serve as a 'warm-up' exercise for an online teaching session on the theme of "Search Sort and Pathfinding"."""

# Copy and paste the code below into your own repl
# Fix it!  :)
# Refer to the pseudo code presented to you
# Ask questions in the chat
#fixed

def binarySearch(someSortedList, e):
  index = -1
  found = False
  first = 0
  last = len(someSortedList) - 1
  while (first <= last) and not found:
    midpoint = (first + last)//2
    if someSortedList[midpoint] == e:
      index = midpoint
      found = True
      print(last)
      print(someSortedList[midpoint])
    elif someSortedList[midpoint] < e:
        print(someSortedList[midpoint])
        first = midpoint + 1
    else:
        print(last)
        last = midpoint - 1
  return (index+1)

while True:
  print("Select the list you want to use for your test:")
  print("A: [2,5,7,8,6]")
  print("B: [2,6,9,243,56,78,345,567,899]")
  print("C: [23,45, 58, 79, 132,454]")
  print("Enter A, B or C, or X for exit")
  choice = input()
  if choice == 'X': break
  if choice == 'A':
    print("Which number do you want to look for?")
    e = int(input())
    result = binarySearch([2, 5, 7, 8, 6], e)
    if result:
      print("Your number is on your list, at index: ", result)
    else:
      print("Your number is NOT on your list")
  elif choice == 'B':
    print("Which number do you want to lool for?")
    e = int(input())
    result = binarySearch([2, 6, 9, 243, 56, 78, 345, 567, 899], e)
    if result:
      print("Your number is on your list, at index: ", result)
    else:
      print("Your number is NOT on your list")
  elif choice == 'C':
    print("Which number do you want to lool for?")
    e = int(input())
    result = binarySearch([23, 45, 58, 79, 132, 454], e)
    if result:
      print("Your number is on your list, at index: ", result)
    else:
      print("Your number is NOT on your list")
  else:
    print("Sorry - wrong input")
