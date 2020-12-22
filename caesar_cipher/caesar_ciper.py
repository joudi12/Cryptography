import nltk
nltk.download('words')

words_list= nltk.corpus.words.words()
def encrypt (msg,key):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    key=key%26

    for character in msg:
        if character ==" " or character == ',' :
            result+= character
        elif character.isupper():
            index=alphabet_upper.find(character)
            result+= alphabet_upper[index+key]
        else:
            index=alphabet.find(character)
            result+= alphabet[index+key]
    return result

def decrypt(msg,key):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    key=key%26

    for character in msg:
        if character ==" " or character == ',' :
            result+= character
        
        elif character.isupper():
            index=alphabet_upper.find(character)
            result+= alphabet_upper[index-key]
        else:
            index=alphabet.find(character)
            result+= alphabet[index-key]
    return result

def is_english(msg):
    words = msg.split()
    word_count = 0

    for word in words:
        if word in words_list:
            word_count += 1
        return word_count


def cipher_breaker(msg):
    max = 0
    max_english_sentence = ''
    msg =msg.lower()
    for key in range(26):
        decrypted = decrypt(msg ,key)
        count_words = is_english(decrypted)

        if count_words > max:
            max_english_sentence = decrypted

    return max_english_sentence    

if __name__ == "__main__":
    msg = encrypt('Great job Joudi',3) 
    print(msg)   
    msg1 = decrypt('Juhdw mre Mrxgl',3)
    print(msg1) 
    print(cipher_breaker(msg))    