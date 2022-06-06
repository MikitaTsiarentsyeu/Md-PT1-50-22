s= "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

#turn words to numbers
d = {"five":5, "thirteen":13, "two":2, "eleven":11, "seventeen": 17, "one":1, "ten":10, "four":4, "eight":8, "nineteen":19}

s_new = [d[i] for i in s.split (' ')]  

print (s_new, "these are numbers")

#remove duplicates
s_duplicates_free = list(set(s_new))
print (s_duplicates_free, "there are no duplicates")

#sort ascending

print (sorted(s_duplicates_free) , "there are sort ascending")

#print the product of the first and second numbers, the sum of the second and third, the product of the third and fourth, etc.

s_changed = []

for i in range(len(s_duplicates_free)-1) :
    if i % 2==0:
        s_changed.append (s_duplicates_free[i]*s_duplicates_free[i+1])
    else:
        s_changed.append (s_duplicates_free[i]+s_duplicates_free[i+1])

print (s_changed, "print the product of the first and second numbers, the sum of the second and third, the product of the third and fourth, etc.")

#print the total sum of all odd numbers

odd_sum = sum([x for x in s_duplicates_free if x%2 == 0])
 
print (odd_sum, 'the total sum of all odd numbers') 

