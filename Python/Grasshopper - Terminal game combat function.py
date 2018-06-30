def combat(health, damage):
    return health - damage if health - damage > 0 else 0

def combat(health, damage):
    return max(0, health-damage)


def combat(health, damage):
    if damage > health:
        return 0
    return health - damage

def combat(health, damage):
    return [0, health-damage][damage < health]


combat = lambda h,d: (h>d)*(h-d)

