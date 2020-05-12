import sys


from review_package.utility import parse_input_command, alphabet_size, output, alphabet_lower_utility, \
    alphabet_upper_utility


def vernam_code(text, key, mode):
    ans = []
    alphabet_lower = "".join(alphabet_lower_utility)
    alphabet_upper = "".join(alphabet_upper_utility)
    k = 0
    for i in range(len(text)):
        if text[i].islower():
            k += 1
            ans.append(alphabet_lower[(alphabet_lower.find(text[i]) +
                                   mode * alphabet_lower.find(key[k % len(key)])) % alphabet_size])
        elif text[i].isupper():
            k += 1
            ans.append(alphabet_upper[(alphabet_upper.find(text[i]) +
                                   mode * alphabet_upper.find(key[k % len(key)])) % alphabet_size])
        else:
            ans.append(text[i])
    return ans


def vernam_cipher(argv):
    mode = 1 if argv.mode == "encode" else -1
    text = parse_input_command(argv)
    key = argv.key.read() if argv.key else sys.stdin.read()
    ans = vernam_code(text, key, mode)
    output(argv, ans)
