# I've decided to add a little bit of interactive:)

def is_float_digit(n: str) -> bool:
     try:
         float(n)
         return True
     except ValueError:
         return False

print("""Hi! I'm Bank. I would like to propose you investments.
Just let me ask you about few details and I'll come back to you with interesting proposal;)
Well, let's move on...""")

Deposit=input("What is the summ of your deposit (BYN):\n")
Rate=input("What is the banking rate of your dream (%):\n")
Period=input("How many years would you like to trust me with your money? (years):\n")

if is_float_digit(Deposit) == False or is_float_digit(Rate) == False or is_float_digit(Period) == False:
    print("""Please, give me just figures. No spaces, no letters, no other signes. Only numbers and points.
Please, reboot the script to continue our conversation.""")

else:
    Deposit=float(Deposit)
    Rate=float(Rate)
    Period=float(Period)

    Result=Deposit * (1 + (Rate/100) / 12) ** (Period*12)
    Result=round(Result, 2)
    print("Cool! I will give you back", Result, "BYN in", Period, "years.")

input()

