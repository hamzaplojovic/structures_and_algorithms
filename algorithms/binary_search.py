arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary(target, start, end):
    if start > end:
        return "Not found."
    middle = (start+end)//2
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary(target, start, middle-1)
    else:
        return binary(target, middle+1, end)


print(binary(5, 0, len(arr)))
