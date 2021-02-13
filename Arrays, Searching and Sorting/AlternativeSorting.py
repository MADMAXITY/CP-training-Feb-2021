def sort_alternatively(arr):
    arr.sort()
    left =  0
    right = len(arr)-1
    while right >left:
        print(arr[right],end=' ')
        print(arr[left],end=' ')
        right-=1
        left+=1
    if right==left:
        print(arr[right],end=' ')
    print()

arr = [1, 6, 9, 4, 3, 7, 8, 2]
sort_alternatively(arr)