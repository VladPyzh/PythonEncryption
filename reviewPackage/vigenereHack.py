import sys
import json


def strDif(sample, aim):
    def shift(str):
        str = list(str)
        for i in range(len(str)):
            if str[i] == 'a':
                str[i] = 'z'
            else:
                str[i] = chr(ord(str[i]) - 1)
        str = ''.join(str)
        return str

    def mutualIndex(sample, aim):
        modelSample = {}
        modelAim = {}
        n = len(sample)
        m = len(aim)
        ans = 0
        for i in range(26):
            modelSample[chr(i + ord('a'))] = 0
            modelAim[chr(i + ord('a'))] = 0
        for i in sample:
            modelSample[i] += 1
        for i in aim:
            modelAim[i] += 1
        for i in range(26):
            frequency = modelSample[chr(i + ord('a'))] * modelAim[chr(i + ord('a'))]
            ans += frequency / (n * m)
        return ans

    for i in range(26):
        if mutualIndex(sample, aim) > 0.06:
            return i
        else:
            aim = shift(aim)


def findShift(text, keyLen):
    shifts = [0 for i in range(keyLen)]
    movedStrings = ['' for i in range(keyLen)]
    k = 0
    for j in range(len(text)):
        if text[j].isalpha():
            movedStrings[k % keyLen] += text[j].lower()
            k += 1
    for i in range(1, keyLen):
        shifts[i] = strDif(movedStrings[0], movedStrings[i])
    return shifts


def findIndex(testStr):
    n = len(testStr)
    ans = 0
    model = {}
    for i in range(26):
        model[chr(i + ord('a'))] = 0
    for i in testStr:
        if i.islower():
            model[i] += 1
        elif i.isupper():
            i = i.lower()
            model[i] += 1
    for i in range(26):
        frequency = model[chr(i + ord('a'))]
        ans += (frequency * (model[chr(i + ord('a'))] - 1)) / (n * (n - 1))
    return ans


def findLen(text):
    j = 1
    k = 0
    while True:
        testStr = ''
        k = 0
        for i in range(len(text)):
            if text[i].isalpha():
                if k % j == 0:
                    testStr += text[i].lower()
                k += 1
        if findIndex(testStr) > 0.06:
            return j
        j += 1


def vigHack(argv):
    text = argv.input_file.read() if argv.input_file else sys.stdin.read()
    model = argv.model_file.read()
    model = json.loads(model)
    keyLen = findLen(text)
    shifts = findShift(text, keyLen)
    k = 0
    ans = ''
    for i in range(len(text)):
        if text[i].islower():
            ans += chr((((ord(text[i]) - ord('a')) - shifts[k % len(shifts)]) % 26) + ord('a'))
            k += 1
        elif text[i].isupper():
            ans += chr((((ord(text[i]) - ord('A')) - shifts[k % len(shifts)]) % 26) + ord('A')).upper()
            k += 1
        else:
            ans += text[i]
    if argv.output_file:
        argv.output_file.write(ans)
    else:
        sys.stdout.write(ans)
