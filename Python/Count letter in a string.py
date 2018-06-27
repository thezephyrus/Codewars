def strCount(string, letter):
    return string.count(letter)

str_count = lambda strng, letter: strng.count(letter)

def str_count(strng, letter):
    count =0
    for i in range(0,len(strng)):
        if strng[i] == letter:
            count = count +1
    return count


def str_count(strng, letter):
    count = 0
    for i in strng:
        if i == letter:
            count += 1
    return count


str_count=lambda x,y:x.count(y)#(strng, letter):
