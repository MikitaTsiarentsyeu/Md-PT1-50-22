def list_sum(l, num=0):
    num = num+sum([x for x in l if isinstance(x, int)]) 
    l = ([x for x in l if isinstance(x, list)])
    if len(l)==0:
        return num
    else:
        num = list_sum(l[0], num)
        return list_sum(l[1:], num)



    
 
    


