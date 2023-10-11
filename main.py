def calc_ent(arr, index):
    sum_left = 0
    sum_right = 0
    for i in range(len(arr)):
        if i <= index:
            sum_left += arr[i]
        else:
            sum_right += arr[i]
    ent = sum_left * sum_right
    if index <= len(arr):
        return ent
    else:
        return -1


def calc_strength(arr):
    length = len(arr)
    ent = []
    for j in range(length):
        ent.append(calc_ent(arr, j))
    return max(ent)


n = int(input())
strength = []
if 1 <= n <= 10e5:
    s = input()
    s = s.split(" ")
    for i in s:
        strength.append(int(i))

print(calc_strength(strength))

