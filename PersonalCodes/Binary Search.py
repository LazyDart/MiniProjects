def find_first(arr, n):
    if arr[0] == n:
        return 0
    start = 0
    end = len(arr) -1
    mid = (start + end)//2
    while arr[mid] != n or arr[mid-1] >= n:
        if arr[mid] >= n:
            end = mid
            mid = (start+end)//2
        else:
            start = mid
            mid = (start+end)//2
        if start + 1 >= end:
            return -1
    return mid

def find_last(arr, n):
    end = len(arr) - 1 
    if arr[end] == n:
        return end
    start = 0
    mid = (start + end)//2
    while arr[mid] != n or arr[mid+1] <= n:
        if arr[mid] <= n:
            start = mid
            mid = (start+end)//2
        else:
            end = mid
            mid = (start+end)//2
        if start + 1 >= end:
            return -1
    return mid

def find_first_last(arr, n):
    first = find_first(arr, n)
    last = find_last(arr, n)
    return (first, last)


print(find_first_last([4], 4))