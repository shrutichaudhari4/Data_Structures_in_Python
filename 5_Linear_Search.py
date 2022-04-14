# Linear Search is also called as Sequential Search
# It is one of the Searching Algorithms

# Linear Search work for both : Sorted and Unsorted Array:
# In Linear Search , it visits each element and returns the index number

# Time Complexity:
# Best Case:O(1)
# Worst Case:O(n)
# Average Case:O(n)

# Implementation of Linear Search Using Function:
def LinearSearch(arr,element):
    for i in range(len(arr)):
        if arr[i]==element:
            return i
    return -1

array1=[12,33,44,1,56,78]
print(LinearSearch(array1,56))
