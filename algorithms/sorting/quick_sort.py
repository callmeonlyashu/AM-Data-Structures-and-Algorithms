def partition(array, low, high):
    # pivot = array[high]
    i = low + 1
    j = high
    pivot = arr[low]
    print(pivot)
    while i <= j:
        while arr[i] < pivot and i < high:
            print("value of i {} is: {}".format(i, arr[i]))
            i+=1
        while arr[j] > pivot:
            print("value of j {} is: {}".format(j, arr[j]))
            j-=1
        if i<j:
            print("before swapping of arr[i], arr[j] is: {} and {}".format(arr[i], arr[j]))
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        else:
            i+=1

    arr[low] = arr[j]
    arr[j] = pivot
    return j
    # for j in range(low, high):
    #     if array[j] <= pivot:
    #         i = i + 1
    #         (array[i], array[j]) = (array[j], array[i])
    #
    # (array[i + 1], array[high]) = (array[high], array[i + 1])
    # return i + 1


# function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)

        quick_sort(array, pi + 1, high)

    return array

if __name__ == '__main__':
    arr = [22, 12, 25, 7, 53, 84, 16, 61, 99]
    a = quick_sort(arr, 0, len(arr)-1)
    1+1