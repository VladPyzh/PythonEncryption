import sys

alphabet_size = 26
language_vigenere_hack_const = 0.06


def alphabet_filler(alphabet, register):
    if register == 'upper':
        for i in range(alphabet_size):
            alphabet.append(chr(ord('A') + i))
    else:
        for i in range(alphabet_size):
            alphabet.append(chr(ord('a') + i))


def shift(arr):
    arr.append(arr.pop(0))
    return arr.copy()


def vigenere_table_filler(vigenere_table_small,
                          vigenere_table_big):
    alphabet_small = []
    alphabet_big = []
    alphabet_filler(alphabet_small, 'lower');
    alphabet_filler(alphabet_big, 'upper');

    for i in range(alphabet_size):
        vigenere_table_small.append(alphabet_small.copy())
        alphabet_small = shift(alphabet_small)
        vigenere_table_big.append(alphabet_big.copy())
        alphabet_big = shift(alphabet_big)


def parse_execute_command(argv):
    text = argv.input_file.read() if argv.input_file else sys.stdin.read()
    return text


def output(argv, text):
    if argv.output_file:
        argv.output_file.write(text)
    else:
        sys.stdout.write(text)


def empty_dict_creator():
    alphabet = []
    alphabet_filler(alphabet, 'lower')
    model = dict(zip(alphabet, [0] * alphabet_size))
    return model
