def correct(string):
    x = string.replace('5','S')
    x = x.replace('0','O')
    x = x.replace('1','I')
    return x


 def correct(string):
    return string.translate(str.maketrans("501", "SOI"))


def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')

def correct(string):
  return ''.join({'0':'O', '5':'S', '1':'I'}.get(c, c) for c in string)


def correct(s):
    mapping = str.maketrans({'0': 'O', '1': 'I', '5': 'S'})
    return s.translate(mapping)

def correct(string):
    output = ""
    for letter in string:
        if letter == '5':
            output += 'S'
        elif letter == '0':
            output += 'O'
        elif letter == '1':
            output += 'I'
        else:
            output += letter
    return output

    