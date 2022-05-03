

d=20000   # initial deposit
t=5       # deposit term in year
n=15      # percent per year
p=12      #capitalization period in monthe
s=d*(1+n/100/p)**(t*p)
print ('Account balance', 5, 'deosit years:', round(s, 2))  
