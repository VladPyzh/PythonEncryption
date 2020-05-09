import sys
import json
from review_package.utility import shift, output, alphabet_size, model_creator, alphabet_lower_utility


def distance(model_numbers, text_mode_numbers):
    ans = 0
    for i in range(alphabet_size):
        ans += abs(model_numbers[i] - text_mode_numbers[i])
    return ans


def model_compare(model, text_model):
    model_numbers = list(model.values())
    text_model_numbers = list(text_model.values())
    dist = float('inf')
    for i in range(alphabet_size):
        if dist > distance(model_numbers, text_model_numbers):
            move = i
            dist = distance(model_numbers, text_model_numbers)
        shift(text_model_numbers)
    alphabet = alphabet_lower_utility
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
    text_model = model_creator(text)
    map_for_decode = model_compare(model, text_model)
    ans = ''
    for i in text:
        if i.islower():
            ans += map_for_decode[i]
        elif i.isupper():
            ans += map_for_decode[i.lower()].upper()
        else:
            ans += i
    if gift_from_vigenere == "":
        output(argv, ans)
    else:
        return ans
