def arrLen(array):
    length = 0
    for item in array:
        length += 1
    return length

def getIndex(array, target):
    index = 0
    for item in array:
        if item != target:
            index += 1
        else:
            break
    return index

plaintext = input('Plaintext: ')
rotation = int(input('Rotation: '))

letters = 'abcdefghijklmnopqrstuvwxyz'
ciphertext = ""

for char in plaintext:
    index = getIndex(letters, char)
    index += rotation
    ciphertext += letters[index % arrLen(letters)]

print(ciphertext)

