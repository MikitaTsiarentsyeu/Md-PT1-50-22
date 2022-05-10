def Deposit():
    Dep = int(input("Input start deposit: "))
    Term = int(input("Input term in yers: "))
    Percent = int(input("Input percent: "))
    if Term > 5:
        print("Maximum term is 5 years. Input correct term")
    elif Term <= 0:
        print("Input correct term")
    elif Dep < 0:
        print("The deposit cannot be nagative.Input correct deposit")
    else:
        Term = Term*12
        i = 0
        while i < Term: 
            Dep = round(Dep+Dep*Percent/(12*100), 2)
            i += 1
            print("Number of months: ",i,", deposit: ", Dep, "BYN")
    return Deposit
Deposit()