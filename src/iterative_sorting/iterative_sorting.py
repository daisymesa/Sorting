# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements

    # Start with current index = 0
    # For all indices EXCEPT the last index:
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # a. Loop through elements on right-hand-side of current index and find the smallest element
        for x in range(cur_index, len(arr)):
            if arr[cur_index] > arr[x]:
                # b. Swap the element at current index with the smallest element found in above loop
                arr[cur_index], arr[x] = arr[x], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # NOTES
    # Loop through your array
    # Compare each element to its neighbor
    # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

    # set default to not sorted
    sorted = False

    # loop while array is not sorted
    while not sorted:
        # change sorted to True to break out of outer loop
        sorted = True
        for i in range(0, len(arr)-1):
            # if item being looped through is bigger than the next item: swap the values of the two items
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # whenever a swap occurs, sorted boolean goes back to false
                sorted = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
