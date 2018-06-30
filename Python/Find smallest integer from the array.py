def findSmallestInt(arr):
    return min(arr)

findSmallestInt=min   

def findSmallestInt(arr):
    smallest = []
    for i in range(0,len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
    return smallest

def findSmallestInt(arr):
    #sort array
    arr.sort()
    return arr[0]

def findSmallestInt(arr):
  a=arr[0]
  for i in range(1,len(arr)):
    if arr[i]<a:
      a=arr[i]
  return a
