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

res = []
for row in range(len(arr)):
    for col in range(len(arr[row])):
        i = row
        j = col
        num = []
        while i < len(arr):
            while j < len(arr[0]):
                num.append(arr[i][j])
                break
            i += 1
            j += 1
            # if len(num) == 4:
            #     res.append(num)
            #     num = []
        res.append(num)

res_filtered = [x for x in res if len(x) == 4]
res_string = [''.join(x) for x in res_filtered]

res_reverse = []
for row in range(len(arr)):
    for col in range(len(arr[row])-1, 0, -1):
        i = row
        j = col
        num = []
        while i < 10:
            while j >= 0:
                num.append(arr[i][j])
                break
            i += 1
            j -= 1
            # if len(num) == 4:
                # res_reverse.append(num)
                # num = []
        res_reverse.append(num)

res_rev_filtered = [x for x in res_reverse if len(x) == 4]
res_rev_string = [''.join(x) for x in res_rev_filtered]

final_array = res_rev_string + res_string
1==1


