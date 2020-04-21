import sys
import json
from review_package.utility import parse_execute_command, empty_dict_creator


def train(argv):
    text = argv.text_file.read() if argv.text_file else sys.stdin.read()
    model = empty_dict_creator()
    for i in text:
        if i.islower():
            model[i] += 1
        elif i.isupper():
            i = i.lower()
            model[i] += 1
    argv.model_file.write(json.dumps(model))
