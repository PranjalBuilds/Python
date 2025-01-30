import random
import string

def coding(words):
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = random.choice(string.ascii_letters)
            r2 = random.choice(string.ascii_letters)
            stword = r1 + word[1:] + word[0] + r2
            nwords.append(stword)
        else:
            nwords.append(word[::-1])
    print("Encoded Message:", " ".join(nwords))

def decoding(words):
    nwords = []
    for word in words:
        if len(word) >= 3:
            stword = word[1:-1]
            stword = stword[-1] + stword[:-1]
            nwords.append(stword)
        else:
            nwords.append(word[::-1])
    print("Decoded Message:", " ".join(nwords))

st = input("Enter message: ")
words = st.split(' ')

choice = input("Enter 1 for Coding or 2 for Decoding: ")
if choice == "1":
    coding(words)
else:
    decoding(words)
