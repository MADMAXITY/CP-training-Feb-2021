def sort_array(arr):
    zero = 0
    one = 0
    two = len(arr)-1

    while one<=two:

        if arr[one]==0:
            arr[zero],arr[one] = arr[one],arr[zero]
            zero+=1
            one+=1
        elif arr[one]==2:
            arr[one],arr[two] = arr[two],arr[one]
            two-=1
        else:
            one+=1
    return arr

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(sort_array(arr))

