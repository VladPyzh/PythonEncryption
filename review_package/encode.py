from review_package.utility import alphabet_filler, vigenere_table_filler, parse_execute_command, output, alphabet_size


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

    vigenere_table_small = []
    vigenere_table_big = []

    vigenere_table_filler(vigenere_table_small, vigenere_table_big)
    ans = ''
    j = 0
    for i in range(len(text)):
        if text[i].islower():
            ans += vigenere_table_small[ord(key[j % len(key)]) - ord('a')][ord(text[i]) - ord('a')]
            j += 1
        elif text[i].isupper():
            ans += vigenere_table_big[ord(KEY[j % len(KEY)]) - ord('A')][ord(text[i]) - ord('A')]
            j += 1
        else:
            ans += text[i]
    return ans


def encode(argv):
    text = parse_execute_command(argv)
    encoded = caesar_encoder(text, argv.key) if argv.cipher == 'caesar' else vigenere_encoder(text, argv.key)
    output(argv, encoded)
