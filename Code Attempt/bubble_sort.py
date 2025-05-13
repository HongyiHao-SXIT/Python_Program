def bubble_sort(arr):
    len = len(arr)
    for i in range(len):
        for j in range(len):
            if arr[i] > arr[j]