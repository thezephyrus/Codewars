'''
Digital Cypher assigns a unique number to each letter of the alphabet:

 a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
In the encrypted word we write the corresponding numbers instead of the letters. For example, the word scout becomes:

 s  c  o  u  t
19  3 15 21 20
Then we add to each number a digit from the key (repeated if necessary). For example if the key is 1939:

   s  c  o  u  t
  19  3 15 21 20
 + 1  9  3  9  1
 ---------------
  20 12 18 30 21
  
   m  a  s  t  e  r  p  i  e  c  e
  13  1 19 20  5 18 16  9  5  3  5
+  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  14 10 22 29  6 27 19 18  6  12 8
Task
Write a function that accepts a message string and an array of integers code. As the result, return the key that was used to encrypt the message. The key has to be shortest of all possible keys that can be used to code the message: i.e. when the possible keys are 12 , 1212, 121212, your solution should return 12.

Input / Output:
The message is a string containing only lowercase letters.
The code is an array of positive integers.
The key output is a positive integer.
Examples
find_the_key("scout", [20, 12, 18, 30, 21]) # -->  1939
find_the_key("masterpiece", [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]) # -->  1939
find_the_key("nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20]) # -->  12

'''
def smallest_repeated_substring(s):
    print("checking substrings")
    n = len(s)
    for length in range(1, n+1): # checking for substrings of length 1 or more...
        for i in range(n-length+1):
            substring = s[i:i+length]
            if substring*(n//length) + substring[:n%length] == s:
                return substring
                break
            else:
                continue
            break

def find_the_key(word,code):
    alphabet_dict = {char: i+1 for i, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
    base = [alphabet_dict.get(char, 0) for char in word]
    
    result=[]
    for i in range(len(word)):
        result.append(code[i]-base[i])
    pattern=''.join(map(str, result))
    return int(smallest_repeated_substring(pattern))


'''
We iterate through all possible substring lengths from 1 to the length of s. 
For each substring length, we iterate through all possible starting positions for that substring.
We extract the substring using slicing and check if it can be repeated to form s. 
We repeat the substring n//length times, and then add the remainder of n divided by length characters 
from the start of the substring, if there is any. If the resulting string matches s,
we have found the smallest repeated substring, and we print it. We use a break statement to exit the loops 
once we have found the smallest repeated substring.
'''