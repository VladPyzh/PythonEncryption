import argparse

from review_package.encode import encode
from review_package.decode import decode
from review_package.train import train
from review_package.vigenere_hack import vig_hack
from review_package.vernam_cipher import vernam_cipher

parser = argparse.ArgumentParser(description='Work with ciphers and hacks')
subparsers = parser.add_subparsers()

# Parsing encode command
parser_encode = subparsers.add_parser('encode', help='Calls encode. Standard: '
                                                     'encode --cipher {caesar,vigenere}'
                                                     '--key {number|word}'
                                                     '[--input-file input.txt]'
                                                     '[--output-file output.txt]')
parser_encode.set_defaults(func=encode)
parser_encode.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
parser_encode.add_argument('--key', required=True)
parser_encode.add_argument('--input-file', type=argparse.FileType('r'))
parser_encode.add_argument('--output-file', type=argparse.FileType('w'))

# Parsing decode command
parser_decode = subparsers.add_parser('decode', help='Calls decode. Standard: '
                                                     'decode --cipher {caesar,vigenere}'
                                                     '--key {number for caesar or word for vigenere}'
                                                     '[--input-file input.txt]'
                                                     '[--output-file output.txt]')
parser_decode.set_defaults(func=decode)
parser_decode.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
parser_decode.add_argument('--key', required=True)
parser_decode.add_argument('--input-file', type=argparse.FileType('r'))
parser_decode.add_argument('--output-file', type=argparse.FileType('w'))

# Parsing train command
parser_train = subparsers.add_parser('train', help='Training. Standard: '
                                                   'train --text-file {input.txt}'
                                                   '--model-file {model}')
parser_train.set_defaults(func=train)
parser_train.add_argument('--text-file', type=argparse.FileType('r'))
parser_train.add_argument('--model-file', required=True, type=argparse.FileType('w'))

# Parsing hack command
parser_hack = subparsers.add_parser('hack', help='Hack. Standard:'
                                                 '[--input-file input.txt]'
                                                 '[--output-file output.txt] '
                                                 '--model-file {model}')
parser_hack.set_defaults(func=vig_hack)
parser_hack.add_argument('--input-file', type=argparse.FileType('r'))
parser_hack.add_argument('--output-file', type=argparse.FileType('w'))
parser_hack.add_argument('--model-file', required=True, type=argparse.FileType('r'))

# Parsing Vernam cipher command
parser_vernam_cipher = subparsers.add_parser('vernam-cipher', help='Vernam Cipher. Take number in Z/26*Z')
parser_vernam_cipher.set_defaults(func=vernam_cipher)
parser_vernam_cipher.add_argument('--mode', choices=['decode', 'encode'], required=True)
parser_vernam_cipher.add_argument('--input-file', type=argparse.FileType('r'))
parser_vernam_cipher.add_argument('--key', type=argparse.FileType('r'))
parser_vernam_cipher.add_argument('--output-file', type=argparse.FileType('w'))

argv = parser.parse_args()
argv.func(argv)
