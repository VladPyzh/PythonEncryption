import sys
import string
import collections

alphabet_size = 26
language_vigenere_hack_const = 0.06
alphabet_lower_utility = list(string.ascii_lowercase)
alphabet_upper_utility = list(string.ascii_uppercase)


def model_creator(text):
    model = collections.defaultdict(int)
    for i in alphabet_lower_utility:
        model[i] = 0
    for i in text:
        if i.islower():
            model[i] += 1
        elif i.isupper():
            i = i.lower()
            model[i] += 1
    return dict(model)


def shift(arr):
    arr.append(arr.pop(0))
    return arr.copy()


def parse_input_command(argv):
    text = argv.input_file.read() if argv.input_file else sys.stdin.read()
    return text


def output(argv, text):
    if argv.output_file:
        argv.output_file.write(text)
    else:
        sys.stdout.write(text)
