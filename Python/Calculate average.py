def find_average(array):
    sum =0
    print (len(array))
    if len(array) == 0:
        return 0
    else:    
        for i in range(len(array)):
            sum=sum+array[i]
        return (sum/len(array));