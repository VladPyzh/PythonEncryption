import sys


from reviewPackage.utility import parse_execute_command, alphabet_filler, alphabet_size, output


def vernam_code(text, key, mode):
    ans = ''
    alphabet_small = []
    alphabet_big = []
    alphabet_filler(alphabet_small, 'lower')
    alphabet_filler(alphabet_big, 'upper')
    alphabet_small = ''.join(alphabet_small)
    alphabet_big = ''.join(alphabet_big)
    k = 0
    for i in range(len(text)):
        if text[i].islower():
            k += 1
            ans += alphabet_small[(alphabet_small.find(text[i]) + mode * alphabet_small.find(key[k % len(key)])) % alphabet_size]
        elif text[i].isupper():
            k += 1
            ans += alphabet_big[(alphabet_big.find(text[i]) + mode * alphabet_big.find(key[k % len(key)])) % alphabet_size]
        else:
            ans += text[i]
    return ans


def vernam_cipher(argv):
    mode = 1 if argv.mode == 'encode' else -1
    text = parse_execute_command(argv)
    key = argv.key.read() if argv.key else sys.stdin.read()
    ans = vernam_code(text, key, mode)
    output(argv, ans)
