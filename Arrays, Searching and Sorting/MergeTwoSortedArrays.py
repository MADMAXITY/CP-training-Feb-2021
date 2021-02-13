def merge_two_sorted_arrays(arr1, arr2):
    merged = [0]*(len(arr1) + len(arr2))
    a1 = 0
    a2 = 0
    i = 0

    while a1 < len(arr1) and a2 < len(arr2):
        if arr1[a1] < arr2[a2]:
            merged[i] = arr1[a1]
            i += 1
            a1 += 1
        else:
            merged[i] = arr2[a2]
            i += 1
            a2 += 1
    while a1 < len(arr1):
        merged[i] = arr1[a1]
        i += 1
        a1 += 1
    while a2 < len(arr2):
        merged[i] = arr2[a2]
        i += 1
        a2 += 1
    return merged


arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
print(merge_two_sorted_arrays(arr1, arr2))
