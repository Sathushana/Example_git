#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time

def bubblesort(arr):
    n = len(arr)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                k = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = k

        if not swapped:
            return

def insertionsort(arr):
    for i in range (1,len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = key
            
def selectionsort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
            k = i
        arr[i],arr[min_index] = arr[min_index],arr[k]
        
        
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        L = arr[ :mid]
        R = arr[mid: ]
        
        mergesort(L)
        mergesort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[i]
                j += 1
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
            

def partition(arr,p,r):
    pivot = arr[r]
    i = p-1
    
    for j in range(p,r):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1

def quicksort(arr,p,r):
    if p < r:
        q = partition(arr,p,r)
        
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)

def countsort(arr):
    max_element = max(arr)
    count = [0] * (max_element + 1)
    output = [0] * len(arr)
    
    for element in arr:
        count[element] += 1
        
    for i in range(0,len(count)):
        count[i] += count[i-1]
    
    i = len(arr) -1
    while i >= 0:
        output[count[i] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
        
    for i in range(0,len(arr)):
        arr[i] = output[i]
    

def timing(func,length):
    timingList = list()
    for x in range(100):
        array = [random.randint(0,20000) for i in range(length)]
        time1 = time.time()
        # func(array)
        if(func == quicksort):
            func(array,0,length-1)
        else:
            func(array)
        time2 = time.time()
        timingList.append(time2-time1)
        
    return (sum(timingList)/len(timingList)) 
        
print("**10**")
bubblesort_timing_10 = timing(bubblesort,10)
print(f"Computational time for bubblesort_10: ",bubblesort_timing_10)
insectionsort_timing_10 = timing(insertionsort,10)
print(f"Computational time for insectionsort_10: ",insectionsort_timing_10)
selection_timing_10 = timing(selectionsort,10)
print(f"Computational time for selectionsort_10: ",selection_timing_10)
merge_sort_timing_10 = timing(mergesort,10)
print(f"Computational time for mergesort_10:",merge_sort_timing_10)
quicksort_timing_10 = timing(quicksort,10)
print(f"Computational time for quicksort_10:",quicksort_timing_10)
countsort_timing_10 = timing(countsort,10)
print(f"Computational time for countsort_10:",countsort_timing_10)
print()

print("**100**")
bubblesort_timing_100 = timing(bubblesort,100)
print(f"Computational time for bubblesort_100: ",bubblesort_timing_100)
insectionsort_timing_100 = timing(insertionsort,100)
print(f"Computational time for insectionsort_100: ",insectionsort_timing_100)
selection_timing_100 = timing(selectionsort,100)
print(f"Computational time for selectionsort_100: ",selection_timing_100)
merge_sort_timing_100 = timing(mergesort,100)
print(f"Computational time for mergesort_100",merge_sort_timing_100)
quicksort_timing_100 = timing(quicksort,100)
print(f"Computational time for quicksort_10",quicksort_timing_100)
countsort_timing_100 = timing(countsort,100)
print(f"Computational time for countsort_100:",countsort_timing_100)
print()

print("**1000**")
bubblesort_timing_1000 = timing(bubblesort,1000)
print(f"Computational time for bubblesort_1000: ",bubblesort_timing_1000)
insectionsort_timing_1000 = timing(insertionsort,1000)
print(f"Computational time for insectionsort_1000: ",insectionsort_timing_1000)
selection_timing_1000 = timing(selectionsort,1000)
print(f"Computational time for selectionsort_1000: ",selection_timing_1000)
merge_sort_timing_1000 = timing(mergesort,1000)
print(f"Computational time for mergesort_1000:",merge_sort_timing_1000)
quicksort_timing_1000 = timing(quicksort,1000)
print(f"Computational time for quicksort_1000",quicksort_timing_1000)
countsort_timing_1000 = timing(countsort,1000)
print(f"Computational time for countsort_1000:",countsort_timing_1000)
print()


print("**10000**")
bubblesort_timing_10000 = timing(bubblesort,10000)
print(f"Computational time for bubblesort_10000: ",bubblesort_timing_10000)
insectionsort_timing_10000 = timing(insertionsort,10000)
print(f"Computational time for insectionsort_10000: ",insectionsort_timing_10000)
selection_timing_10000 = timing(selectionsort,10000)
print(f"Computational time for selectionsort_10000: ",selection_timing_10000)
merge_sort_timing_10000 = timing(mergesort,10000)
print(f"Computational time for mergesort_10000:",merge_sort_timing_10000)
quicksort_timing_10000 = timing(quicksort,10000)
print(f"Computational time for quicksort_10000",quicksort_timing_10000)
countsort_timing_10000 = timing(countsort,10000)
print(f"Computational time for countsort_10000:",countsort_timing_10000)
print()








