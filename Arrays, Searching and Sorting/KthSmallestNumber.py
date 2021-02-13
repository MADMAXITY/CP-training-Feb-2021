def find_kth_smallest_el(arr,k):
    arr.sort()
    return arr[k-1]

arr = [7, 10, 4, 3, 20, 15]
k = 4
print(find_kth_smallest_el(arr,k))