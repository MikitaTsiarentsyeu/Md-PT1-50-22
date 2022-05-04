D = 20000
#  D - initial deposit amount,BYN
n = 15
# n - deposit percentage (year),%
T = 60
# T - deposite term, month
L = 12
# L - monthly capitalization
S = D*((1+(n/100/L))**T)
# S - total amount
print("Total amount:", round(S,2),"BYN")

