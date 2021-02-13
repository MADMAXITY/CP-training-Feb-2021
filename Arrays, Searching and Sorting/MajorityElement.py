def find_candidate(arr):
    cur_el = arr[0]
    count = 1
    i = 1
    while i < len(arr):
        if arr[i] != cur_el:
            count -= 1
        else:
            count += 1
        if count == 0:
            count = 1
            cur_el = arr[i]
        i += 1
    return cur_el


def find_majority_element(arr):
    candidate = find_candidate(arr)
    occurrences = 0
    for i in arr:
        if i == candidate:
            occurrences += 1
    if occurrences > len(arr)//2:
        return candidate
    else:
        return "No Majority Element!"


arr = [3, 3, 4, 2, 4, 4, 2, 4]
print(find_majority_element(arr))
