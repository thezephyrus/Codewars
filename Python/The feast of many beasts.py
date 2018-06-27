def feast(beast, dish):
    return beast[0]==dish[0] and dish[-1]==beast[-1]


def feast(beast, dish):
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])

feast = lambda beast, dish: beast[0].lower()==dish[0].lower() and beast[-1].lower()==dish[-1].lower()

feast = lambda b, d: (b[0], b[-1]) == (d[0], d[-1])    

def feast(beast, dish):
    if(beast[0]==dish[0] and beast[len(beast)-1]==dish[len(dish)-1]):
        return True
    else: 
        return False
    pass