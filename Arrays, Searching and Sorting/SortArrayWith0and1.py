def sort_array(arr):
    zero = 0
    one = len(arr)-1

    while zero<one:

        while zero<one and arr[zero]==0:
            zero+=1
        
        while zero<one and arr[one]==1:
            one-=1
        
        if zero<one:
            arr[zero],arr[one] = arr[one],arr[zero]
            zero+=1
            one-=1
    return arr

arr = [0, 1, 0, 1, 0, 1]
print(sort_array(arr))