def mergeSort(arr):
  # Base case, if there's only one element, return it since there's nothing to sort
  if(len(arr) == 1):
    return arr
  # Get the middle index (doing // means divide but floor the number, aka 5 // 2 = 2)
  mid = len(arr) // 2
  # This is the recursive function, we keep splitting the array down the middle and calling the sort function on the new
  # splitted array
  l = mergeSort(arr[:mid])
  r = mergeSort(arr[mid:])
  # Initialize the necessary variables
  result = []
  i = j = 0
  # This is the "two finger algorithm". There's two fingers (pointers) pointed to the smallest element in each of the
  # arrays (since the array is sorted from smallest to largest, it is the first element), it then compares which is smaller 
  # and adds that element to the new array. You then move the finger from the array that had the smallest value to 
  # the next element and compare again. Keep going till one finger reaches the end of the array
  while(i < len(l) and j < len(r)):
    if (l[i] <= r[j]):
      result.append(l[i])
      i += 1
    elif (r[j] < l[i]):
      result.append(r[j])
      j += 1
  # At this point, one finger reached the end but there's still elements in the other array. Since the two arrays are sorted,
  # this ensures that the items remaining in the other array are sorted, so simply add the elements to the result
  if (i == len(l)):
    result.extend(r[j:])
  elif (j == len(r)):
    result.extend(l[i:])
  # Return the sorted array!
  return result