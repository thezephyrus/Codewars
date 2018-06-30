def abbrevName(name):
    a= str.split(name,' ')
    b=[]
    for i in range(0, len(a)):
        x=a[i]
        b.append(str.capitalize(x[0]))
    return ('.'.join(b))


def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


def abbrevName(name):
    first_initial = name[0]
    for letter in range(len(name)):
        if name[letter]  == ' ':
            last_initial = name[letter + 1]
          
    return (first_initial.upper() + "." + last_initial.upper())

def abbrevName(name):
    return name.split(' ')[0][0].upper()+'.'+name.split(' ')[1][0].upper()


def abbrevName(name):
    x = name
    y = name.split()
    return y[0][0].upper() + "." + y[1][0].upper()

abbrevName = lambda name: ".".join(e[0].upper() for e in name.split())

def abbrevName(name):
    '''
    This function works with middle names too.
    Read the inside first, then work your way out.
    1. Split the name string into an array, separated by spaces.
    2. Map the array created by (1) into an array of first letters only.
    3. Convert the map object to a list.
    4. Join the array into a string, separated by periods.
    5. Change the string created by (4) into an uppercase string.
    '''
    return (".".join(list(map(lambda x: x[0], name.split(" "))))).upper()

def abbrevName(name):
    name = name.split(' ')
    print(name)
    first = name[0][0].upper()
    second = name[1][0].upper()
    return((first + '.' + second))

