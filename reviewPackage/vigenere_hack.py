import sys
from reviewPackage.utility import empty_dict_creator, alphabet_size, language_vigenere_hack_const, alphabet_filler, \
    parse_execute_command, output
from reviewPackage.hack import hack


def str_dif(sample, aim):
    def shift(line):
        line = list(line)
        for i in range(len(line)):
            if line[i] == 'a':
                line[i] = 'z'
            else:
                line[i] = chr(ord(line[i]) - 1)
        line = ''.join(line)
        return line

    def mutual_index(sample, aim):
        model_sample = empty_dict_creator()
        model_aim = empty_dict_creator()
        alphabet = []
        alphabet_filler(alphabet, 'lower')
        n = len(sample)
        m = len(aim)
        ans = 0
        for i in sample:
            model_sample[i] += 1
        for i in aim:
            model_aim[i] += 1
        for i in alphabet:
            frequency = model_sample[i] * model_aim[i]
            ans += frequency / (n * m)
        return ans

    for i in range(alphabet_size):
        if mutual_index(sample, aim) > language_vigenere_hack_const:
            return i
        else:
            aim = shift(aim)


def find_shift(text, key_length):
    shifts = [0 for i in range(key_length)]
    moved_strings = ['' for i in range(key_length)]
    k = 0
    for j in range(len(text)):
        if text[j].isalpha():
            moved_strings[k % key_length] += text[j].lower()
            k += 1
    for i in range(1, key_length):
        shifts[i] = str_dif(moved_strings[0], moved_strings[i])
    return shifts


def find_index(test_str):
    n = len(test_str)
    ans = 0
    model = empty_dict_creator()
    alphabet = []
    alphabet_filler(alphabet, 'lower')
    for i in test_str:
        if i.islower():
            model[i] += 1
        elif i.isupper():
            i = i.lower()
            model[i] += 1
    for i in alphabet:
        frequency = model[i]
        ans += (frequency * (model[i] - 1)) / (n * (n - 1))
    return ans


def find_len(text):
    j = 1
    while True:
        test_str = ''
        k = 0
        for i in range(len(text)):
            if text[i].isalpha():
                if k % j == 0:
                    test_str += text[i].lower()
                k += 1
        if find_index(test_str) > language_vigenere_hack_const:
            return j
        j += 1


def vig_hack(argv):
    text = parse_execute_command(argv)
    key_len = find_len(text)
    shifts = find_shift(text, key_len)
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
    ans = hack(argv, ans)
    output(argv, ans)
