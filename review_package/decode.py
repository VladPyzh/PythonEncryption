from review_package.encode import caesar_encoder, vigenere_encoder
from review_package.utility import parse_input_command, output


def caesar_decoder(text, key):
    key = int(key)
    return caesar_encoder(text, -key)


def vigenere_decoder(text, key):
    return vigenere_encoder(text, key, -1)


def decode(argv):
    text = parse_input_command(argv)
    decoded = caesar_decoder(text, argv.key) if argv.cipher == 'caesar' else vigenere_decoder(text, argv.key)
    output(argv, decoded)
