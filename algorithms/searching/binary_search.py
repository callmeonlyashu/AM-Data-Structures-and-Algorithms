def binary_search(arr, element):
    mid_index = len(arr)//2
    if arr[mid_index] == element:
        return True

    if mid_index < 1:
        return False

    if arr[mid_index] < element:
        return binary_search(arr[mid_index:], element)
    else:
        return binary_search(arr[:mid_index], element)


if __name__ == '__main__':
    param = [-1,0,1,2,-1,-4]
    param.sort()
    is_there = binary_search(param, 0)
    1==1