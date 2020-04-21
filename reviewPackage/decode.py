from reviewPackage.encode import caesar_encoder
from reviewPackage.utility import vigenere_table_filler, parse_execute_command, output


def caesar_decoder(text, key):
    key = int(key)
    return caesar_encoder(text, -key)


def vigenere_decoder(text, key):
    KEY = key.upper()

    vigenere_table_small = []
    vigenere_table_big = []

    vigenere_table_filler(vigenere_table_small, vigenere_table_big)
    ans = ''
    k = 0
    for i in range(len(text)):
        if text[i].islower():
            for j in range(26):
                if vigenere_table_small[ord(key[k % len(key)]) - ord('a')][j] == text[i]:
                    ans += chr(ord('a') + j)
                    k += 1
                    break
        elif text[i].isupper():
            for j in range(26):
                if vigenere_table_big[ord(KEY[k % len(KEY)]) - ord('A')][j] == text[i]:
                    ans += chr(ord('A') + j)
                    k += 1
                    break
        else:
            ans += text[i]

    return ans


def decode(argv):
    text = parse_execute_command(argv)
    decoded = caesar_decoder(text, argv.key) if argv.cipher == 'caesar' else vigenere_decoder(text, argv.key)
    output(argv, decoded)
