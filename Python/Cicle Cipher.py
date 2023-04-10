'''
Imagine a circle. To encode the word codewars, we could split the circle into 8 parts (as codewars has 8 letters):

Then add the letters in a clockwise direction:Then remove the circle:
If we read the result from left to right, we get csordaew.

Decoding is the same process in reverse. If we decode csordaew, we get codewars.

Examples:
encode "codewars" -> "csordaew"
decode "csordaew" -> "codewars"
encode "white" -> "wehti"
decode "wehti" -> "white"

'''


def encode(s: str) -> str:
    n = len(s)
    # Even length case
    if n % 2 == 0:
        left = s[:n//2]
        right = s[n//2:]
        right = right[::-1]
        return ''.join([l+r for l,r in zip(left, right)])
    # Odd length case
    else:
        middle = s[n//2]
        left = s[:n//2]
        right = s[n//2+1:]
        right = right[::-1]
        return ''.join([l+r for l,r in zip(left, right)]) + middle


    
    
def decode(s:str) -> str:
    result=[]
    p1=[]
    p2=[]
    p3=[]
    n=len(s)

    # Even length case
    if n%2==0:
        for i in range(len(s)):
            if i%2!=0:
                p1.append(s[i])
            else:
                p2.append(s[i])
        p3=p1[::-1]
        result=p2+p3
        return(''.join(result))
    # Odd length case
    else:
        middle_char=[]
        middle_char.append(s[-1]) # middle char is the last char of the string
        s2=s[:-1]
        for i in range(len(s2)):
            if i%2!=0:
                p1.append(s[i])
            else:
                p2.append(s[i])
        p3=p1[::-1]
        p2=p2+middle_char
        result=p2+p3
        return(''.join(result))
        

# ---------------------------------------------------------------------------------------- #

'''
Other approach from solutions
'''        
def encode(s):
    return "".join(s[((i+1)//2)*(-1)**i] for i in range(len(s)))


def decode(s):
    return s[::2] + s[1::2][::-1]

# ---------------------------------------------------------------------------------------- #

from itertools import cycle
from collections import deque


def encode(s:str) -> str:
    dq = deque(s)
    return ''.join( meth() for _,meth in zip(s, cycle( (dq.popleft, dq.pop) )) )
    
    
def decode(s:str) -> str:
    return s[::2] + s[1::2][::-1]

# ---------------------------------------------------------------------------------------- #
def encode(s):
    s = list(s)
    end_word = ""
    while len(s):
        end_word += s.pop(0)
        if len(s):
            end_word += s.pop(-1)
    return end_word
    
    
def decode(s):
    s = list(s)
    end_word = ""
    a = 0
    while a<len(s):
        end_word += s.pop(a)
        a+=1
    return end_word + "".join(s[::-1])

# ---------------------------------------------------------------------------------------- #