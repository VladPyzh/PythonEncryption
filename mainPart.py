import argparse

from review_package.encode import encode
from review_package.decode import decode
from review_package.train import train
from review_package.hack import hack
from review_package.vigenere_hack import vig_hack
from review_package.vernam_cipher import vernam_cipher

parser = argparse.ArgumentParser(description='Work with ciphers and hacks')
subparsers = parser.add_subparsers()

# Parsing encode command
parserEncode = subparsers.add_parser('encode', help='Calls encode. Standard: '
                                                    'encode --cipher {caesar,vigenere}'
                                                    '--key {number|word}'
                                                    '[--input-file input.txt]'
                                                    '[--output-file output.txt]')
parserEncode.set_defaults(func=encode)
parserEncode.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
parserEncode.add_argument('--key', required=True)
parserEncode.add_argument('--input-file', type=argparse.FileType('r'))
parserEncode.add_argument('--output-file', type=argparse.FileType('w'))

# Parsing decode command
parserDecode = subparsers.add_parser('decode', help='Calls decode. Standard: '
                                                    'decode --cipher {caesar,vigenere}'
                                                    '--key {number for caesar or word for vigenere}'
                                                    '[--input-file input.txt]'
                                                    '[--output-file output.txt]')
parserDecode.set_defaults(func=decode)
parserDecode.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
parserDecode.add_argument('--key', required=True)
parserDecode.add_argument('--input-file', type=argparse.FileType('r'))
parserDecode.add_argument('--output-file', type=argparse.FileType('w'))

# Parsing train command
parserTrain = subparsers.add_parser('train', help='Training. Standard: '
                                                  'train --text-file {input.txt}'
                                                  '--model-file {model}')
parserTrain.set_defaults(func=train)
parserTrain.add_argument('--text-file', type=argparse.FileType('r'))
parserTrain.add_argument('--model-file', required=True, type=argparse.FileType('w'))

# Parsing hack command
parserHack = subparsers.add_parser('hack', help='Hack. Standard:'
                                                'hack --cipher {vigenere | caesar}'
                                                '[--input-file input.txt]'
                                                '[--output-file output.txt] '
                                                '--model-file {model}')
parserHack.set_defaults(func=hack)
parserHack.add_argument('--cipher', choices=['caesar', 'vigenere'], required=True)
parserHack.add_argument('--input-file', type=argparse.FileType('r'))
parserHack.add_argument('--output-file', type=argparse.FileType('w'))
parserHack.add_argument('--model-file', required=True, type=argparse.FileType('r'))


# Parsing Vernam cipher command
parserVernamCipher = subparsers.add_parser('vernam-cipher', help='Vernam Cipher. Take number in Z/26*Z')
parserVernamCipher.set_defaults(func=vernam_cipher)
parserVernamCipher.add_argument('--mode', choices=['decode', 'encode'], required=True)
parserVernamCipher.add_argument('--input-file', type=argparse.FileType('r'))
parserVernamCipher.add_argument('--key', type=argparse.FileType('r'))
parserVernamCipher.add_argument('--output-file', type=argparse.FileType('w'))

argv = parser.parse_args()
if argv.func == hack and argv.cipher == 'vigenere':
    argv.func = vig_hack
argv.func(argv)
