def reverse_seq(n):
    a = []
    for i in reversed(range(1,n+1)):
        a.append(i)
    return a


def reverseseq(n):
    return list(range(n, 0, -1))

def reverseseq(n):
    return [x for x in range(n,0,-1)]


def reverse_seq(a):
    if a > 0:
        return(list(range(a, 0, -1)))
    else:
        return("pick a positive number")


def reverse_seq(n): return list(reversed(range(1,n+1)))

def reverse_seq(n):
    return [x for x in range(1,n+1)][::-1]

def reverse_seq(n):
    return [n-x for x in range(n)]

