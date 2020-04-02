import sys


def CaesarEncoder(text, key):
    key = int(key)
    ans = ''
    for i in text:
        if i.isupper():
            ans += chr((ord(i) - ord('A') + key) % (ord('Z') - ord('A') + 1) + ord('A'))
        elif i.islower():
            ans += chr((ord(i) - ord('a') + key) % (ord('z') - ord('a') + 1) + ord('a'))
        else:
            ans += i
    return ans


def VigenereEncoder(text, key):
    KEY = key.upper()
    def shift(arr):
        arr.append(arr.pop(0))
        return arr.copy()

    alphabetSmall = []
    alphabetBig = []
    vigenereTableS = []
    vigenereTableB = []
    for i in range(26):
        alphabetSmall.append(chr(ord('a') + i))
        alphabetBig.append(chr(ord('A') + i))
    for i in range(26):
        vigenereTableS.append(alphabetSmall.copy())
        alphabetSmall = shift(alphabetSmall)
        vigenereTableB.append(alphabetBig.copy())
        alphabetBig = shift(alphabetBig)
    ans = ''
    for i in range(len(text)):
        if text[i].islower():
            ans += vigenereTableS[ord(key[i % len(key)]) - ord('a')][ord(text[i]) - ord('a')]
        elif text[i].isupper():
            ans += vigenereTableB[ord(KEY[i % len(KEY)]) - ord('A')][ord(text[i]) - ord('A')]
        else:
            ans += text[i]

    return ans


def encode(argv):
    text = argv.input_file.read() if argv.input_file else sys.stdin.read()
    encoded = CaesarEncoder(text, argv.key) if argv.cipher == 'caesar' else VigenereEncoder(text, argv.key)
    if argv.output_file:
        argv.output_file.write(encoded)
    else:
        sys.stdout.write(encoded)
