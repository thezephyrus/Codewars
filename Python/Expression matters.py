def expression_matter(a, b, c):
    sum_all = a + b + c
    prod_all = a * b * c
    sum_12 = a + b
    sum_23 = b + c
    prod_12 = a * b
    prod_23 = b * c
    p23_a1 = prod_23 + a
    p12_a3 = prod_12 + c
    s12_a3 = sum_12 * c
    s23_a1 = sum_23 * a
    return max(sum_all, prod_all, p23_a1, p12_a3, s12_a3, s23_a1 )


def expression_matter(a, b, c):
    l = ['{} * ({} + {})', '{} * {} * {}', '{} + {} * {}', '({} + {}) * {}','{} + {} + {}']
    return max(eval(sequance.format(a, b, c)) for sequance in l)


def expression_matter(a, b, c):
    test = []
    test.append(a + b + c)
    test.append((a + b) * c)
    test.append(a + (b * c))
    test.append(a * (b + c))
    test.append(a * b * c)
    
    return max(test)


def expression_matter(a, b, c):
    #from itertools import permutations
    ls = [a*b*c, a+b+c, (a+b)*c, a+b*c, a*b+c,a*(b+c)]
    
    #perm = list(permutations([a, b, c]))
    #for i in perm:
     # x = (a+b)*c
  #  y = a+b*c
  #  ls.append(x)
   # ls.append(y)
        
    ls.sort(reverse=True)
    return ls[0] # highest achievable result

def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))

