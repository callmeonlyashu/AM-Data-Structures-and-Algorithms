def bubble_sort(arr, desc=False):
    # sorting merge array using bubble sort.
    for i in range(len(arr)):
        for j in range(len(arr)):
            if desc:
                cond = arr[i] > arr[j]
            else:
                cond = arr[i] < arr[j]
            if cond:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == '__main__':
    a = bubble_sort([2,4,1,54,12,434,67,78,34,12])