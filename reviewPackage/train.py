import sys
import json


def train(argv):
    text = argv.text_file.read() if argv.text_file else sys.stdin.read()
    model = {}
    for i in range(26):
        model[chr(i+ord('a'))] = 0
    for i in text:
        if i.islower():
            model[i] += 1
        elif i.isupper():
            i = i.lower()
            model[i] += 1
    argv.model_file.write(json.dumps(model))

