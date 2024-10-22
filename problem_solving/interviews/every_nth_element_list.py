def get_every_nth_element_array(a, n):
    counter = 0
    for i in range(len(a)):
        counter += 1
        index = n * counter - 1
        if index >= len(a):
            continue
        print(a[index])


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = 5

    get_every_nth_element_array(a, n)

