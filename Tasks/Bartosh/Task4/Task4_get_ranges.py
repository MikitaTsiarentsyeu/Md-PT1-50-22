def get_ranges (l):

    l_range = []

    for i in range(0, len(l)):
        if i ==0:
            l_range.append(str(l[i])) 
        elif i == (len(l)-1) and l[i]-l[i-1]>1:
            l_range.append(str(l[i]))
            break
        elif i == (len(l)-1) and l[i]-l[i-1]==1:
            l_range.append('-')
            l_range.append(str(l[i]))
            break
        elif l[i]-l[i-1]==1 and l[i+1]-l[i]==1:
            continue
        elif l[i]-l[i-1]==1 and l[i+1]-l[i]>1:
            l_range.append('-')
            l_range.append(str(l[i]))
            l_range.append(', ')
        elif l[i]-l[i-1]>1 and l[i+1]-l[i]>1:
            l_range.append(', ')
            l_range.append(str(l[i]))
            l_range.append(', ')
        elif l[i]-l[i-1]>1 and l[i+1]-l[i]==1: 
            l_range.append(str(l[i]))
        
    res = (''.join(l_range))    
    return res