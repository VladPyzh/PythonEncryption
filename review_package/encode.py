from review_package.utility import alphabet_filler, parse_execute_command, output, alphabet_size


def caesar_encoder(text, key):
    key = int(key)
    ans = ''
    alphabet_small = []
    alphabet_big = []
    alphabet_filler(alphabet_small, 'lower')
    alphabet_filler(alphabet_big, 'upper')
    alphabet_big = ''.join(alphabet_big)
    alphabet_small = ''.join(alphabet_small)
    for i in text:
        if i.isupper():
            ans += alphabet_big[(alphabet_big.find(i) + key) % alphabet_size]
        elif i.islower():
            ans += alphabet_small[(alphabet_small.find(i) + key) % alphabet_size]
        else:
            ans += i
    return ans


def vigenere_encoder(text, key):
    KEY = key.upper()

    alphabet_lower = []
    alphabet_filler(alphabet_lower, 'lower')
    alphabet_lower = "".join(alphabet_lower)
    alphabet_upper = []
    alphabet_filler(alphabet_upper, 'upper')
    alphabet_upper = "".join(alphabet_upper)

    ans = ''
    j = 0
    for i in range(len(text)):
        if text[i].islower():
            ans += alphabet_lower[(alphabet_lower.find(key[j % len(key)])
                                   + alphabet_lower.find(text[i])) % alphabet_size]
            j += 1
        elif text[i].isupper():
            ans += alphabet_lower[(alphabet_upper.find(KEY[j % len(KEY)])
                                   + alphabet_upper.find(text[i])) % alphabet_size]
            j += 1
        else:
            ans += text[i]
    return ans


def encode(argv):
    text = parse_execute_command(argv)
    encoded = caesar_encoder(text, argv.key) if argv.cipher == 'caesar' else vigenere_encoder(text, argv.key)
    output(argv, encoded)
