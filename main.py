import argparse

parser = argparse.ArgumentParser(description='A CLI Caesar Cipher Encryption tool.')
parser.add_argument('plaintext', nargs='+', type=str)
parser.add_argument('rotation', type=int)

args = parser.parse_args()

letters = 'abcdefghijklmnopqrstuvwxyz'
ciphertext = ''

for char in args.plaintext:
    if char in letters:
        index = letters.index(char)
        index += args.rotation
        ciphertext += letters[index % len(letters)]
    else:
        ciphertext += char

print(ciphertext)

