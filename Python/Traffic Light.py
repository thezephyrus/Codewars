def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "red":
        return "green"
    else:
        return "red"

        
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."


update_light = {"green":"yellow", "yellow":"red", "red":"green"}.get

def update_light(current):
    light_order = {'red':'green', 'yellow':'red', 'green':'yellow'}
    
    return light_order[current]        

update_light = lambda c,l=["yellow","green","red"]: l[l.index(c)-1]

def update_light(current):
    return 'yellow' if current == 'green' else ('green' if current == 'red' else 'red')

