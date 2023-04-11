'''
The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is "GA-DE-RY-PO-LU-KI".

 g => a
 a => g
 d => e
 e => d
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
Our scouts had party yestarday and they had too much milk and cookies. As the result all of them forgot the key. Your task is to help scouts to find the key that they used for encryption. Fortunately they have some messages that are already encoded.

Input
The function accepts has two arrays.
The messages string array consists of lowercase characters and whitespace characters. The strings on the messages array are scout's messages before encrytption.
The secrets string array consists of lowercase characters and whitespace characters. The strings on the messages array are scout's messages after encrytption.

Output
Return string should consists of lowercase characters only. The pairs of substitution should be ordered by the first letter of substitution. The letters in each pair should be in alphabethic order.

ga => incorret output (error: g is after a )
ag => correct output  
deag => incorrect output  (error: de is after ag)
agde => correct output  
Example
string[] messages = { "dance on the table", "hide my beers", "scouts rocks" };
string[] secretes = { "egncd pn thd tgbud" ,"hked mr bddys" ,"scplts ypcis" };
FindTheKey(messages, secretes);   //=> agdeikluopry

'''

def find_the_key(messages,secrets):
    
    # Build key-pairs from the differences seen between messaages & secrets
    key_pair=[]
    for message,secret in zip(messages,secrets):
        for c,s in zip(message,secret):
            x=c+"-"+s
            if (c!=s):
                key_pair.append(x)
            else:
                continue

    # Remove key-pair duplicates and prepare for ordering
    base = sorted(list(set(key_pair)))

    # Do ASCII value comparison and store ordered pairs in the set
    new_base=set()
    
    for pair in base:
        x=''
        if (ord(pair[0])<ord(pair[2])):
            new_base.add(pair)
        else:
            x=pair[::-1]
            new_base.add(x)
    return (''.join(sorted(new_base)).replace('-',''))

'''-------------------------------------------------------------------------------------'''
'''                     Another shortened solution                                      '''
'''-------------------------------------------------------------------------------------'''

def find_the_key(messages, secrets):
    # Generate unique key pairs from the differences between messages and secrets
    key_pairs = set()
    for message, secret in zip(messages, secrets):
        for c, s in zip(message, secret):
            if c != s:
                key_pairs.add((min(c, s), max(c, s)))

    # Sort the key pairs and concatenate the characters to form the key
    sorted_pairs = sorted(key_pairs, key=lambda x: (ord(x[0]), ord(x[1])))
    key = ''.join([pair[0] + pair[1] for pair in sorted_pairs])

    return key
