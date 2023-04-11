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
Our scouts had party yestarday and they had too much milk and cookies. As the result all of them forgot the key. Your task is to help scouts to find the key that they used for encryption. Fortunately they have some messages that are already encoded. However they like order and cleanup. So they sorted all messages and encrytpted messages in alphabethic order. But... it means they do not know what encrypts to what...
Help the scouts to find their key.

Input
The function accepts two arrays.
The messages string array consists of lowercase characters. The strings on the messages array are scout's messages before encrytption.
The secrets string array consists of lowercase characters.
The strings on the secrets array are scout's messages after encrytption.
All strings in the messages and secrets have the same lenght (up to 20 characters).
The number of elements in the messages and secrets is equal and less than 6.
Every string from messages array after encoding is equal to one of elements in the secrets array (i.e. the 1st string from messages array afer encoding is equal to 5th string in the secrets array, the 2nd string from messages array afer encoding is equal to 3th string in the secrets array, etc.).

Output
Return string should consists of lowercase characters only. The pairs of substitution should be ordered by the first letter of substitution. The letters in each pair should be in alphabethic order.

ga => incorret output (error: g is after a )
ag => correct output  
deag => incorrect output  (error: de is after ag)
agde => correct output  
Example
 var messages = [ "dance", "level", "right", "yours" ];
 var secrets =  [ "dkucr", "elghy", "irvri", "tpnes" ];
 searchForKey(messages, secrets);   //=> akerilnuopty
 
// because akerilnuopty can encode all secrets:
// messages[0] = encode( secrets[0], "akerilnuopty")
// messages[1] = encode( secrets[2], "akerilnuopty")
// messages[2] = encode( secrets[1], "akerilnuopty")
// messages[3] = encode( secrets[3], "akerilnuopty")
Suggestion
The key will have 12 letters. The brutal force may not work. 12 letters give us 4 626 053 752 320 000 combinations.
The performance of your solution may be the key to pass the kata.

'''


import itertools

def check_kp_count(key_pair):
    new_base = set()

    # Do ASCII value comparison
    for pair in sorted(list(set(key_pair))):
        if ord(pair[0]) < ord(pair[2]):
            new_base.add(pair)
        else:
            x = pair[::-1]
            new_base.add(x)

    prefix_counts = {}

    for item in new_base:
        prefix = item.split('-')[0]
        if prefix in prefix_counts:
            if prefix_counts[prefix] == 1:
                prefix_counts[prefix] += 1
            else:
                return "False"
        else:
            prefix_counts[prefix] = 1

    x=(''.join(sorted(new_base)).replace('-',''))
    
    return x
    

def evaluate_kp(m, se):
    # Build Key-Pairs
    key_pair = []
    for m, se in zip(m, se):
        for c, s in zip(m, se):
            if c != s:
                key_pair.append(c + "-" + s)

    sorted_kp = sorted(list(set(sorted(key_pair))))
    check_if_valid = check_kp_count(sorted_kp)

    if(len(check_if_valid)==12):
        return check_if_valid
    else:
        return None


def get_kp(combination):
    m = [i[0] for i in combination]
    s = [i[1] for i in combination]
    x = (evaluate_kp(m, s))
    if(x!=None):
        return x
    else:
        return None



def searchForKey(messages, secrets):
    message_perms = list(itertools.permutations(secrets))
    combos = [list(zip(messages, perm)) for perm in message_perms]

    for combination in combos:
        x = get_kp(combination)
        if(x==None):
            continue
        else:
            return x



def main():
    #messages = [ "dance", "level", "right", "yours" ]
    #secrets =  [ "dkucr", "elghy", "irvri", "tpnes" ]

    messages=[ 'fnddurvbsimatjemhtik', 'ovdwhvvmymiwikljfdzi', 'uyhxealadgoemvtxkapk', 'vxpqwcbdzvvwijwmjnwj', 'vzwbzxlxiwanlqhjzlfw', 'wsaejyscqlcmqbuurice' ]
    secrets=[ 'fiddtyvbsnamujcahuno', 'kvdwhvvaranwnoljfdzn', 'trhxcmlmdgkcavuxompo', 'vxpqwebdzvvwnjwajiwj', 'vzwbzxlxnwmilqhjzlfw', 'wsmcjrseqleaqbttynec' ]
    print("Result:",searchForKey(messages,secrets))

if __name__ == "__main__":
    main()

'''----------------------------------------------------------------------------------------------------'''
''' ---------------------'''
'''  Shortened version   '''
''' ---------------------'''

import itertools

def check_kp_count(key_pair):
    new_base = set()

    # Do ASCII value comparison
    for pair in sorted(list(set(key_pair))):
        if ord(pair[0]) < ord(pair[2]):
            new_base.add(pair)
        else:
            x = pair[::-1]
            new_base.add(x)

    prefix_counts = {}

    for item in new_base:
        prefix = item.split('-')[0]
        if prefix in prefix_counts:
            if prefix_counts[prefix] == 1:
                prefix_counts[prefix] += 1
            else:
                return False
        else:
            prefix_counts[prefix] = 1

    x = ''.join(sorted(new_base)).replace('-', '')
    return x
    

def evaluate_kp(messages, secrets):
    # Build Key-Pairs
    key_pair = []
    for m, se in zip(messages, secrets):
        for c, s in zip(m, se):
            if c != s:
                key_pair.append(c + "-" + s)

    sorted_kp = sorted(list(set(sorted(key_pair))))
    check_if_valid = check_kp_count(sorted_kp)

    if len(check_if_valid) == 12:
        return check_if_valid
    else:
        return None


def search_for_key(messages, secrets):
    message_perms = list(itertools.permutations(secrets))
    combos = [list(zip(messages, perm)) for perm in message_perms]

    for combination in combos:
        x = evaluate_kp(*zip(*combination))
        if x is not None:
            return x


def main():
    messages = ['fnddurvbsimatjemhtik', 'ovdwhvvmymiwikljfdzi', 'uyhxealadgoemvtxkapk', 
                'vxpqwcbdzvvwijwmjnwj', 'vzwbzxlxiwanlqhjzlfw', 'wsaejyscqlcmqbuurice']
    secrets = ['fiddtyvbsnamujcahuno', 'kvdwhvvaranwnoljfdzn', 'trhxcmlmdgkcavuxompo', 
               'vxpqwebdzvvwnjwajiwj', 'vzwbzxlxnwmilqhjzlfw', 'wsmcjrseqleaqbttynec']
    
    result = search_for_key(messages, secrets)
    print("Result:", result)

if __name__ == "__main__":
    main()
