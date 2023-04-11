'''
The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is "GA-DE-RY-PO-LU-KI".

 G => A
 g => a
 a => g
 A => G
 D => E
  etc.
The letters, which are not on the list of substitutes, stays in the encrypted text without changes.

Other keys often used by Scouts:

PO-LI-TY-KA-RE-NU
KA-CE-MI-NU-TO-WY
KO-NI-EC-MA-TU-RY
ZA-RE-WY-BU-HO-KI
BA-WO-LE-TY-KI-JU
RE-GU-LA-MI-NO-WY
Task
Your task is to help scouts to encrypt and decrypt thier messages. Write the Encode and Decode functions.

Input/Output
The function should have two parameters.
The message input string consists of lowercase and uperrcase characters and whitespace character.
The key input string consists of only lowercase characters.
The substitution has to be case-sensitive.

Example
 Encode("ABCD", "agedyropulik");             // => GBCE 
 Encode("Ala has a cat", "gaderypoluki");    // => Gug hgs g cgt 
 Decode("Dkucr pu yhr ykbir","politykarenu") // => Dance on the table
 Decode("Hmdr nge brres","regulaminowy")  // => Hide our beers

'''
def key_builder(key_pairs):
    key_dict={}
    pairs=[]

    for i in range(0,len(key_pairs)-1,2):
        x=key_pairs[i],key_pairs[i+1]
        pairs.append(x)
        i=i+1

    for p1, p2 in pairs:
        key_dict[p1.upper()] = p2.upper()
        key_dict[p1.lower()] = p2.lower()
        key_dict[p2.lower()] = p1.lower()
        key_dict[p2.upper()] = p1.upper()

    return key_dict
 
def encode(message,key):
    code_dict=key_builder(key)
    return ("".join(code_dict.get(c, c) for c in message))

def decode(message,key):
    code_dict=key_builder(key) 
    return ("".join(code_dict.get(c, c) for c in message))