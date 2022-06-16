# Task 5 part 1

def summ_arr(l):
    l1 = str(l)
    k = len(l1)
    summ = 0
    for i in range (k):
        try: summ += int(l1[i])
        except: pass
    return summ
#l = [1, 2, [2, 4, [[7, 8], 4, 6]]]        
#print(summ_arr(l))








