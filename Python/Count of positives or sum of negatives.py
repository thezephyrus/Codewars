def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    print(len(arr))
    if (len(arr) == 0):
        return []
        
    for x in arr:
        if x == 0:
            sum+= 0
            count+= 0
        elif x > 0:
            count+= 1
        else:
            sum+= x
        x+=1
    return [count,sum]  