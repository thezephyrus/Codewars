'''
The Cipher
Take every letter in the one-word message and replace it with its place in the alphabet.:
For each number in the list, multiply it by 3 and subtract 5. Repeat this process n times.
Task
Implement two functions, encrypt() and decrypt().

encrypt() (details):
Input:
word - a word
n - the key
Output:
word encrypted with The Cipher
Examples:
n = 2: "abc" >> [1, 2, 3] >> [-2, 1, 4] >> [-11, -2, 7]
n = 6: "test" >> [12760, 1825, 12031, 12760]
n = 3: "hi" >> [151, 178]
decrypt() (details):
Input:
encrypted_word - A word that got encrypted with The Cipher
n - the key
Output:
encrypted_word, decrypted
Examples:
n = 2: [16, 25, 34] >> [7, 10, 13] >> "def"
n = 5: [1339, 610, 2311, 2311, 3040] >> "hello"
Notes
All the inputs in the test cases are valid, i. e. for encrypt() only lowercase letters and for decrypt() only lists that were actually encrypted by my own encrypt() function. If n is negative, just treat it as if it were 0

'''

def encrypt(word, n):
    alphabet_dict = {char: i+1 for i, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
    base = [alphabet_dict.get(char, 0) for char in word]
    for i in range(n):
        result = [(x * 3) - 5 for x in base]
        base = result

    return base[-len(word):] if n > 0 else base


def decrypt(encrypted_word, n):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = {char: i+1 for i, char in enumerate(alphabets)}

    base=[]
    for i in range(len(encrypted_word)):
        base.append(encrypted_word[i])
    
    if n>0:
        for i in range(n):
            result = []
            for x in range(len(base)):
                v=(base[x]+5)//3
                result.append(v)
            base=result
        decrypted_word = ''.join([alphabets[i-1] for i in result])
        return decrypted_word
    else:
        decrypted_word = ''.join([alphabets[i-1] for i in base])
        return decrypted_word