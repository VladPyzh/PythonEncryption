import sys
import json


def distance(modelNumbers, textModeNumbers):
    ans = 0
    for i in range(26):
        ans += abs(modelNumbers[i] - textModeNumbers[i])
    return ans


def modelCompr(model, textModel):
    def shift(arr):
        arr.append(arr.pop(0))
        return arr.copy()
    modelNumbers = (list(model.values()))
    textModelNumbers = (list(textModel.values()))
    dist = 100000000000
    for i in range(26):
        if dist > distance(modelNumbers, textModelNumbers):
            move = i
            dist = distance(modelNumbers, textModelNumbers)
        shift(textModelNumbers)
    alphabet = []
    for i in range(26):
        alphabet.append(chr(ord('a') + i))
    alphabetCopy = alphabet.copy()
    for i in range(move):
        shift(alphabet)
    return dict(zip(alphabet, alphabetCopy))


def hack(argv):
    text = argv.input_file.read() if argv.input_file else sys.stdin.read()
    model = argv.model_file.read()
    model = json.loads(model)
    textModel = {}
    for i in range(26):
        textModel[chr(i + ord('a'))] = 0
    for i in text:
        if i.islower():
            textModel[i] += 1
        elif i.isupper():
            i = i.lower()
            textModel[i] += 1
    dic = modelCompr(model, textModel)
    ans = ''
    for i in text:
        if i.islower():
            ans += dic[i]
        elif i.isupper():
            ans += dic[i.lower()].upper()
        else:
            ans += i
    if argv.output_file:
        argv.output_file.write(ans)
    else:
        sys.stdout.write(ans)

