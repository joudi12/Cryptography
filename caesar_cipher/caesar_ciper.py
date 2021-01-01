import nltk
nltk.download('words')
words_list= nltk.corpus.words.words()

def encrypt(msg, key):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result=''
    key=key%26
    msg = msg.lower()
    for character in msg:
        if character  not in alphabet:
            result+= character
        else:
            index = alphabet.index(character)
            result += alphabet[(index + key) % len(alphabet)]
    return result 


def decrypt(msg,key):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result=''
    key=key%26
    msg = msg.lower()
    for character in msg:
        if character  not in alphabet:
            result+= character
        else:
            index = alphabet.index(character)
            result += alphabet[(index - key) % len(alphabet)]
    return result 


def is_english(msg):
    words = msg.split()
    word_count = 0

    for word in words:
        if word in words_list:
            word_count += 1    
    if (word_count/len(words)) > 0.5:
        return word_count
    else: 
        return 0


def cipher_breaker(msg):
    max = 0
    max_english_sentence = ''
    for key in range(26):
        decrypted = decrypt(msg ,key)
        count_words = is_english(decrypted)
        if count_words > max:
            max_english_sentence = decrypted
    return max_english_sentence    


if __name__ == "__main__":
    msg = encrypt('abcdefghijklmnopqrstuvwxyz',3) 
    print(msg)   
    msg1 = decrypt('juhdw mre mrxglc',3)
    print(msg1) 
    print(cipher_breaker(msg1))    