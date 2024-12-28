arr = [
    ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
    ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
    ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
    ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
    ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
    ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
    ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
    ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
    ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
    ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']
]

result_count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        num = []
        count = 0
        while i < len(arr):
            while j < len(arr[0]):
                if count <= 3:
                    num.append(arr[i][j])
                    count += 1
                break
            i += 1
            j += 1

        joined_string = ''.join(num)
        if joined_string in ['MAS', 'SAM']:
            k = j + 2
            l = i
            count_2 = 0
            num_2 = []
            while k < len(arr):
                while l >= 0:
                    if count_2 < 3:
                        num_2.append(arr[k][l])
                        count_2 += 1
                    break
                k += 1
                l -= 1
            joined_string_2 = ''.join(num_2)
            if joined_string in ['MAS', 'SAM']:
                result_count += 1
