import string

def shifting(p_shift,p_mess):
    alphabet = string.ascii_uppercase
    v = alphabet[p_shift-1:]+alphabet[0:p_shift-1]
    store = []
    final = []
    for strings in p_mess:
        if strings in alphabet:
            store.append(alphabet.index(strings))
        else:
            store.append(strings)
            
    for digits in store:
        if isinstance(digits, int):
            final.append(v[digits])
        else:
            final.append(digits)
    return final
print("Welcome to encrypting and decrypting your words/sentences")
name = input("What's your name? ")
ans = input("Do you want your input to be in lowercase or uppercase? ").lower()
message = input("Enter your message : ").upper()
shift = int(input("Enter your shift : "))
result = shifting(shift,message)
result = "".join(result)
if ans=='lowercase':
    print("Your encrypted word is",result.lower())
if ans=='uppercase':
     print("Your encrypted word is",result)
    
