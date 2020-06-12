def insertionSort(arr):
  # If the length is 1, there's no sorting to do so just return it
  if len(arr) == 1:
    return arr
  # We want to loop through from the second element to the last. This is because we compare with the previous element we're on 
  # (if we start at the first element, there's nothing before it to compare with)
  for index in range(1, len(arr)):
    # We want to continuously swap the element with the element before it as long as the element before it is smaller, we also want
    # to make sure we don't allow our index to fall under 1 because like above, if we let the index fall to 0 (the first element), 
    # there's nothing to compare it with
    while((arr[index] < arr[index-1]) and index > 0):
      # Temp variable to hold the value at the current index
      temp = arr[index]
      # Swap the elements
      arr[index] = arr[index-1]
      arr[index-1] = temp
      # Reduce the index since we swapped the elements making the element we care about (which was originally at arr[index])
      # end up at the index before it (so now the element we care about is at arr[index - 1])
      index -= 1
  # Return the sorted array!
  return arr