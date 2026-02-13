import random
def getSecret(guess_len=0):
    f= open("WORDS.TXT","r")
    words={}
    for word in f:
        word = word.strip()
        length = len(word)
        if length in words:
            words[length].append(word)
        else:
            words[length]=[word]
    min_len = min(words.keys())
    max_len = max(words.keys())
    if guess_len == 0:
        guess_len = random.randint(min_len, max_len)
    no_words = len( words[guess_len])
    secret = words[guess_len][ random.randint(0,no_words-1)]
    return secret

def cheat(secret):
    num_to_reveal = int(len(secret)*0.2)+1
    return [ secret[i] for i in random.sample(range(len(secret)),num_to_reveal)]  

def reveal(secret, guessed):
    ret=""
    for ch in secret:
        ret += ch if ch in guessed else "_"
    return ret