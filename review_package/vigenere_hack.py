from review_package.utility import alphabet_size, language_vigenere_hack_const, \
    alphabet_lower_utility, parse_input_command, output
from review_package.hack import hack
import collections


def str_dif(sample, aim):
    def shift(line):
        line = list(line)
        alphabet_lower = "".join(alphabet_lower_utility)
        for i in range(len(line)):
            if line[i] == alphabet_lower_utility[0]:
                line[i] = alphabet_lower_utility[alphabet_size - 1]
            else:
                line[i] = alphabet_lower[alphabet_lower.find(line[i]) - 1]
        line = "".join(line)
        return line

    def mutual_index(sample, aim):
        model_sample = collections.defaultdict(int)
        model_aim = collections.defaultdict(int)
        alphabet = alphabet_lower_utility
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
    moved_strings = [[] for i in range(key_length)]
    k = 0
    for j in text:
        if j.isalpha():
            moved_strings[k % key_length].append(j)
            k += 1
    for i in range(1, key_length):
        shifts[i] = str_dif(moved_strings[0], moved_strings[i])
    return shifts


def my_aimed_iter(text, j):
    cur = 0
    for i in text:
        if i.isalpha():
            if cur % j == 0:
                yield i.lower()
            cur += 1


def find_len(text):
    j = 1
    while True:
        if j > 6:
            exit()
        model = collections.defaultdict(int)
        check_str = ""
        leng = 0
        for i in my_aimed_iter(text, j):
            leng += 1
            check_str += i
            model[i] += 1
        alphabet = alphabet_lower_utility
        index = 0
        for i in alphabet:
            index += (model[i] * (model[i] - 1)) / (leng * (leng - 1))
        if index > language_vigenere_hack_const:
            return j
        j += 1


def vig_hack(argv):
    text = parse_input_command(argv)
    key_len = find_len(text)
    shifts = find_shift(text, key_len)
    alphabet_lower = ''.join(alphabet_lower_utility)
    k = 0
    ans = []
    for i in range(len(text)):
        if text[i].islower():
            ans.append(alphabet_lower[(alphabet_lower.find(text[i]) - shifts[k % len(shifts)]) % alphabet_size])
            k += 1
        elif text[i].isupper():
            aim = text[i].lower()
            ans.append(alphabet_lower[(alphabet_lower.find(aim) - shifts[k % len(shifts)]) % alphabet_size].upper())
            k += 1
        else:
            ans.append(text[i])
    ans = "".join(ans)
    ans = hack(argv, ans)
    output(argv, ans)
