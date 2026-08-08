import string
def al():
    v = string.ascii_uppercase
    contain = []
    for strings in v:
        contain.append(strings)
    return contain
print("Welcome to encrypting and decrypting your words/sentences")
alphabet = al()
print(alphabet[0])
