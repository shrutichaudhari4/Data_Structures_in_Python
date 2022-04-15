# Binary Search is used in a sorted array by repeatedly dividing the search interval in half.
# The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n). 
# It is one of the Searching Algorithms

# Binary Search work for only Sorted Array

# Time Complexity : 
# Best Case: 0(1)
# Worst Case: 0(logn)

# 1. Implementation of Binary Search Using Function:
def BinarySearch(arr,element):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=low+(high-low)//2
        if(arr[mid]==element):
            return mid+1
        elif(arr[mid]<element):
            low=mid+1
        else:
            high=mid-1
    return "Element not found"

array1=[12,33,44,55,66,77,88]
print(BinarySearch(array1,77))

# 2. Using Recursive Method:
def BinarySearch2(array2,low2,high2,ele):
    while(low2<=high2):
        mid2=(low2+high2)//2
        if(array2[mid2]==ele):
            return f"Element {ele} found at {mid2+1}"
        elif(array2[mid2]<ele):
            return BinarySearch2(array2,mid2+1,high2,ele)
        else:
            return BinarySearch2(array2,low2,mid2-1,ele)
    return "Element not Found"
arra2=[12,22,33,44,56,67]
print(BinarySearch2(arra2,0,len(arra2),44))
