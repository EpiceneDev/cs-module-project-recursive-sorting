# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []   #[0] * elements # sets space
    
   
    # compare and merge
    a = 0  # index of arrA (pointer A)
    b = 0  # index of arrB (pointer B)

    # while a and b are not at the end of the array:
    while a < len(arrA) & b < len(arrB):
        if arrA[a] > arrB[b]:
            merged_arr.append(arrB[b])
            b += 1
        else:
            merged_arr.append(arrA[i])
            a += 1

    # if a reaches the end before b
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a+=1

    # if b reaches the end before a
    while b < len(arrB):
        merged_arr.append(arrB[b])
        b+=1

    return merged_arr

'''
from pair prog with Ari:
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [] #[0] * elements
    # Your code here
    # track index in merged_arr
    r = 0
    l = 0
    # for i in range(elements):
    #     # compare left-most of each arr
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            print(left,  right,  merged_arr, l, r)
            merged_arr.append(left[l])
            # iterate to next index in merged_arr
            l+=1
        if left[l] > right[r]:
            print(left,  right,  merged_arr, l, r)
            merged_arr.append(right[r])
            r += 1
        while r < len(right):
            print(left,  right,  merged_arr, l, r)
            merged_arr.append(right[r])
            r+=1
        while l < len(left):
            print(left,  right,  merged_arr, l, r)
            merged_arr.append(left[l])
            l+=1
    return merged_arr
print(merge([2,4, 6, 8], [ 1, 3, 5, 7]))
'''


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) <=1:
        return arr
        
    # divide in half until subarrays len 1
    # for i in range(len(arr)):
   
    # while len(arr) > 1:
    middle = len(arr)//2
    right = merge_sort(arr[middle:])
    left = merge_sort(arr[:middle])
        
    merge(right, left)
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces


    # merge sorted lists together in groups of 2
        # compare the first element of each group for smallest
        # place smallest into array first 
            # recurse through this ^
        # when one left, add to end of new array

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

def partition(arr):
    left = []
    right = []
    pivot = arr[0]

    # iterate over the rest of the array
    for num in arr[1:]:
    # if the element is greater than pivot, in the right
        if num > pivot:
            right.append(num)
    # else, in the left
        else:
            left.append(num)

    return left, pivot, right



def quick_sort(arr):  # O(N)
    # choose a pivot ..can be first element
    # move all elements LESS than the pivot to its LHS
    # move all elements GREATER than the pivot to its RHS
    if len(arr) == 0:
        return arr

    # helper function to find the pivot
    # partition here into left, pivot, right
    left, pivot, right = partition(arr)

    return quick_sort(left) + pivot + quick_sort(right)
    
def quicksort_in_place(arr):
    pass
