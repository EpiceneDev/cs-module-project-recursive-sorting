# def merge( arrA, arrB ):
#     # given 2 sorted arrays,
#     # return a new combined array
#     merged_arr = []
   
#     # TO-DO
#     i = 0
#     j = 0
#     # perform the actions thru both arrays
#     while i < len(arrA) and j < len(arrB):
#         # compare the two vlues, choose the smaller one
#         if arrB[j] >= arrA[i]:
#             merged_arr.append(arrA[i])
#             i+=1
#         # if not true, merge value from second array (because it is smaller)
#         else:
#             merged_arr.append(arrB[j])
#             j+=1
#     # Whichever array remains as the last one, 
#     # the remaining values will be pushed into the merged array.
   
#     return merged_arr  + arrA[i:] + arrB[j:]

# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements # sets space
    
   
#     # compare and merge
#     a = 0  # index of arrA (pointer A)
#     b = 0  # index of arrB (pointer B)

#     # checking for smallest item to be merged first
#     # while a and b are not at the end of the array:
#     #iterate with elements as range
#     for i in range(0, len(elements)-1):
#         # if a < len(arrA) & b < len(arrB):

#         # if item in first array is bigger than item in second, merge second
#         if arrA[a] < arrB[b]:

#         elif arrA[a] > arrB[b]:
#             merged_arr.append(arrB[b]) # merge_arr[i] = arrB[b]
#             b += 1
#             print(arrA, arrB, merged_arr)
#             # if item in second array is bigger than item in first
#         else:
#             merged_arr.append(arrA[i])
#             a += 1
#             print(arrA, arrB, merged_arr)

#     # if a reaches the end before b, append remaining values of b
#     while arrA[a] < len(arrA):
#         merged_arr.append(arrA[a]) 
#         # if a is greater than length
#         a+=1
#         print(arrA, arrB, merged_arr)

#     # if b reaches the end before a, append remaining values of a
#     while arrB[b] < len(arrB):
#         merged_arr.append(arrB[b])
#         b+=1
#         print(arrA, arrB, merged_arr)

#     return merged_arr

'''
from pair prog with Ari:
'''
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements
    # Your code here
    m = 0 # inital index of merged_arr
    l = 0 # inital index of left
    r = 0 # inital index of right
    print("====in merge", left, right)
    #while index of sub-array less than length
    ## compare at index if left, right
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            print(left,  right,  merged_arr, m)
            # print(f'left: {l}/{len(left)}\nright:{r}/{len(right)}')
            merged_arr[m] = left[l]
            # iterate to next index in left and merged
            l+=1
            m+=1
        # else:
        elif left[l] > right[r]:
            print(left,  right,  merged_arr, m)
            print(f'left: {l}/{len(left)}\nright:{r}/{len(right)}')
            merged_arr[m] = right[r]
            r += 1
            m+=1
             # while r < len(right) :
    while l == len(left) and r < len(right):
        print(left,  right,  merged_arr, m)
        print(f'left: {l}/{len(left)}\nright:{r}/{len(right)}')
        merged_arr[m] = right[r]
        # merged_arr[m:] = right[r:]

        r+=1
        m+=1
    # while l < len(left) :
    while r == len(right) and l < len(left):
        print(left,  right,  merged_arr, m)
        print(f'left: {l}/{len(left)}\nright:{r}/{len(right)}')
        merged_arr[m] = left[l]
        # merged_arr[m:] = left[l:]
        l+=1
        m+=1
    
    print("===merge done", merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    #  if len( arr ) > 1: 
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces
    # TO-DO
    # base-case (easiest case)
    if len(arr) <= 1:
        return arr
    

    # divide the arrays
    half = len(arr) // 2
    left = arr[0:half]
    right = arr[half:]

    return merge(merge_sort(left), merge_sort(right))
    # merging sorted arrays
    # return merge(left, right)


# def merge_sort(arr):
#     # Your code here
#     # base case
#     # if len(arr) <=1:
#     #     return arr
        
#     # divide in half until subarrays len 1
#     # for i in range(len(arr)):
   
#     if len(arr) > 1:
#         middle = len(arr)//2
#         left = merge_sort(arr[0:middle])
#         right = merge_sort(arr[middle:])
            
#         arr = merge(left, right)
#             # recursively call merge_sort() on LHS
#         # recursively call merge_sort() on RHS
#         # merge sorted pieces


#     # merge sorted lists together in groups of 2
#         # compare the first element of each group for smallest
#         # place smallest into array first 
#             # recurse through this ^
#         # when one left, add to end of new array

#     return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start_2nd_half = mid +1

    # if it is already sorted
    if arr[mid] <= arr[start_2nd_half]:
        return 

    # make 2 pointers to keep track of start of arrays to merge
    while start <= mid and start_2nd_half <= end:
        # first location already sorted:
        if start <= start_2nd_half:
            start+=1
        # otherwise
        else:
            value = arr[start_2nd_half]
            index = start_2nd_half

            # shift right while working back to first start
            while index != start:
                arr[index] = arr[index-1]
                index-=1

                arr[start] = value

                # increase pointers to move through
                start+=1
                mid+=1
                start_2nd_half+=1


    return arr


def merge_sort_in_place(arr, l, r):
    
# Implement Merge Sort i.e. standard implementation keeping the sorting algorithm as in-place.
# In-place means it does not occupy extra memory for merge operation as in standard case.
# Maintain two pointers which point to start of the segments which have to be merged.
# Compare the elements at which the pointers are present.
# If element1 < element2 then element1 is at right position, simply increase pointer1.
# Else place element2 in its right position
# and all the elements at the right of element2 will be shifted right by one position. Increment all the pointers by 1.
# implement an in-place merge sort algorithm
# based on C solution at: https://www.geeksforgeeks.org/in-place-merge-sort/



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

