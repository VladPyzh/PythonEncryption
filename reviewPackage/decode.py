import sys

def CaesarDecoder(text, key):
    key = int(key)
    ans = ''
    for i in text:
        if i.isupper():
            ans += chr((ord(i) - ord('A') - key) % (ord('Z') - ord('A') + 1) + ord('A'))
        elif i.islower():
            ans += chr((ord(i) - ord('a') - key) % (ord('z') - ord('a') + 1) + ord('a'))
        else:
            ans += i
    return ans

def VigenereDecoder(text, key):
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
    k = 0
    for i in range(len(text)):
        if text[i].islower():
            for j in range(26):
                if vigenereTableS[ord(key[k % len(key)]) - ord('a')][j] == text[i]:
                    ans += chr(ord('a') + j)
                    k += 1
                    break
        elif text[i].isupper():
            for j in range(26):
                if vigenereTableB[ord(KEY[k % len(KEY)]) - ord('A')][j] == text[i]:
                    ans += chr(ord('A') + j)
                    k += 1
                    break
        else:
            ans += text[i]

    return ans


def decode(argv):
    text = argv.input_file.read() if argv.input_file else sys.stdin.read()
    decoded = CaesarDecoder(text, argv.key) if argv.cipher == 'caesar' else VigenereDecoder(text, argv.key)
    if argv.output_file:
        argv.output_file.write(decoded)
    else:
        sys.stdout.write(decoded)
