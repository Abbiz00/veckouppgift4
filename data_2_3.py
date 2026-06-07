def my_loop (start,end,y):
    count = 0
    for i in range(start, end):
        y *= 2
        print (y)
        count +=1
        if start >= end:
            return None
    return None

