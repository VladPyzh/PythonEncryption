a = [1,2,3,4,5,6]
b = [2,3,4,5,6,1]


def distance(modelNumbers, textModeNumbers):
    ans = 0
    for i in range(6):
        ans += abs(modelNumbers[i] - textModeNumbers[i])
    return ans


def shift(arr):
    arr.append(arr.pop(0))
    return arr.copy()

dist = 1000000000000
for i in range(26):
    if dist > distance(a, b):
        move = i
        dist = distance(a, b)
    shift(a)
    print(a)
print(move)