import sys
import json
from reviewPackage.utility import shift, output, empty_dict_creator, alphabet_size


def distance(model_numbers, text_mode_numbers):
    ans = 0
    for i in range(alphabet_size):
        ans += abs(model_numbers[i] - text_mode_numbers[i])
    return ans


def model_compare(model, text_model):
    model_numbers = (list(model.values()))
    text_model_numbers = (list(text_model.values()))
    dist = 100000000000
    for i in range(26):
        if dist > distance(model_numbers, text_model_numbers):
            move = i
            dist = distance(model_numbers, text_model_numbers)
        shift(text_model_numbers)
    alphabet = []
    for i in range(26):
        alphabet.append(chr(ord('a') + i))
    alphabet_copy = alphabet.copy()
    for i in range(move):
        shift(alphabet)
    return dict(zip(alphabet, alphabet_copy))


def hack(argv, gift_from_vigenere=""):
    if gift_from_vigenere == "":
        text = argv.input_file.read() if argv.input_file else sys.stdin.read()
    else:
        text = gift_from_vigenere
    model = argv.model_file.read()
    model = json.loads(model)
    text_model = empty_dict_creator()
    for i in text:
        if i.islower():
            text_model[i] += 1
        elif i.isupper():
            i = i.lower()
            text_model[i] += 1
    dic = model_compare(model, text_model)
    ans = ''
    for i in text:
        if i.islower():
            ans += dic[i]
        elif i.isupper():
            ans += dic[i.lower()].upper()
        else:
            ans += i
    if gift_from_vigenere == "":
        output(argv, ans)
    else:
        return ans
