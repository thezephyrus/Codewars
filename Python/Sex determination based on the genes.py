def chromosome_check(sperm):
    if 'Y' not in sperm:
        return 'Congratulations! You\'re going to have a daughter.'
    else:
        return 'Congratulations! You\'re going to have a son.'


def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')


def chromosome_check(sperm):
    return "Congratulations! You're going to have a %s." % ('son', 'daughter')[sperm[1] == 'X']


def chromosome_check(sperm):
    gender = {"XY" : "son", "XX" : "daughter"}
    
    return "Congratulations! You're going to have a {}.".format(gender[sperm])


def chromosome_check(sperm):
    gender = 'son' if 'Y' in sperm else 'daughter'
    return "Congratulations! You're going to have a {}.".format(gender)        