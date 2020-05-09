import json
import sys

from review_package.utility import model_creator


def train(argv):
    text = argv.text_file.read() if argv.text_file else sys.stdin.read()
    model = model_creator(text)
    argv.model_file.write(json.dumps(model))
