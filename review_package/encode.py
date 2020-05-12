from review_package.utility import parse_input_command, output, alphabet_size, \
    alphabet_lower_utility, alphabet_upper_utility


def caesar_encoder(text, key):
    key = int(key)
    ans = []
    alphabet_lower = "".join(alphabet_lower_utility)
    alphabet_upper = "".join(alphabet_upper_utility)
    for i in text:
        if i.isupper():
            ans.append(alphabet_upper[(alphabet_upper.find(i) + key) % alphabet_size])
        elif i.islower():
            ans.append(alphabet_lower[(alphabet_lower.find(i) + key) % alphabet_size])
        else:
            ans.append(i)
    return "".join(ans)


def vigenere_encoder(text, key, mode):
    mode = int(mode)
    KEY = key.upper()

    alphabet_lower = "".join(alphabet_lower_utility)
    alphabet_upper = "".join(alphabet_upper_utility)

    ans = []
    j = 0
    for i in range(len(text)):
        if text[i].islower():
            ans.append(alphabet_lower[(mode * alphabet_lower.find(key[j % len(key)])
                                   + alphabet_lower.find(text[i])) % alphabet_size])
            j += 1
        elif text[i].isupper():
            ans.append(alphabet_upper[(mode * alphabet_upper.find(KEY[j % len(KEY)])
                                   + alphabet_upper.find(text[i])) % alphabet_size])
            j += 1
        else:
            ans.append(text[i])
    return "".join(ans)


def encode(argv):
    text = parse_input_command(argv)
    encoded = caesar_encoder(text, argv.key) if argv.cipher == "caesar" else vigenere_encoder(text, argv.key, 1)
    output(argv, encoded)
