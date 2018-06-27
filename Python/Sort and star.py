def two_sort(lst):
    return '***'.join(min(lst))

def two_sort(array):
    array.sort()
    return str.join('***',array[0])

def two_sort(a):
    a = sorted(a)
    result = a[0]
    result = result.replace("", "***")
    return result [3:-3]

two_sort = lambda a: "***".join(sorted(a)[0])

