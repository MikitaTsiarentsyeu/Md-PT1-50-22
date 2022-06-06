

def check_str(Str_c):
   N_up = 0
   N_lo = 0
   for i in range(len(Str_c)-1):
        if Str_c[i].isupper():
          N_up += 1
        if Str_c[i].islower():
          N_lo += 1
   return print(f"{N_up} upper case, {N_lo} lower case")

def is_prime(N):
  Res = True
  Max_d = round(N/2)+1
  for i in range(2,Max_d):
     if N % i == 0:
       Res = False
       break
  return print(Res)

def get_ranges(R):
  Rmod = []
  k = 0
  p = 0
  j = 0
  for i in range(len(R)-1): 
    if R[i+1] == R[i]+1:
      j  += 1
    else:
      if j>0 :
        Rmod.append(str(R[p])+ '-' + str(R[p+j]))
        k += 1
        p = i+1
        j = 0
      else:
        Rmod.append(str(R[p]))
        k += 1
        p = i+1
        j = 0
  if R[len(R)-1] == R[len(R)-2]+1:
    Rmod.append(str(R[p])+ '-' + str(R[p+j]))
  else:
    Rmod.append(str(R[p]))
  return print(Rmod)

#Str_p = input("Please enter your string:") 
#check_str(Str_p)

#Num_c = int(input("Please enter your number:"))
#is_prime(Num_c)

#Rang1 = [2,3,5,8,9,15,80,100]
#get_ranges(Rang1)