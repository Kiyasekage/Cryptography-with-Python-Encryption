import string
def al(p_ans):
    v = string.ascii_uppercase
    contain = []
    if p_ans=="lowercase":
        v = string.ascii_lowercase
    for strings in v:
        contain.append(strings)
    return contain
print("Welcome to encrypting and decrypting your words/sentences")
name = input("What's your name? ")
ans = input("Do you want your input to be in lowercase or uppercase? ").lower()
alphabet = al(ans)
print(alphabet)
