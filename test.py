import string

def shifting(p_shift,p_mess):
    alphabet = string.ascii_uppercase
    v = alphabet[p_shift-1:]+alphabet[0:p_shift-1]
    store = []
    final = []
    for strings in p_mess:
        store.append(alphabet.index(strings))
    for digits in store:
        final.append(v[digits])
    return final
print("Welcome to encrypting and decrypting your words/sentences")
name = input("What's your name? ")
ans = input("Do you want your input to be in lowercase or uppercase? ").lower()
message = input("Enter your message : ").upper()
shift = int(input("Enter your shift : "))
result = shifting(shift,message)
print(result)
