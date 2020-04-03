import sys


def code(text, key):
    ans = ''
    for i in range(len(text)):
        ans += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return ans


def vernamCipher(argv):
    text = argv.input_file.read() if argv.input_file else sys.stdin.read()
    key = argv.key.read() if argv.key else sys.stdin.read()
    ans = code(text, key)
    if argv.output_file:
        argv.output_file.write(ans)
    else:
        sys.stdout.write(ans)
