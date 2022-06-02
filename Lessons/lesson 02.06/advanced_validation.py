actions = "+-*/"

def calculate():
    try:
        while True:
            try:
                x = int(input("Enter x:\n"))
                break
            except ValueError: 
                print("The input was incorrect, cannot convert to a number, please try again")
                continue

        while True:
            try:
                y = int(input("Enter y:\n"))
                break
            except ValueError: 
                print("The input was incorrect, cannot convert to a number, please try again")
                continue

        while True:
            try:
                choice = input(f"Enter action ({','.join(actions)}):\n")
                if choice not in actions:
                    raise RuntimeError("The action is incorrect, please choose from the actions list")
                break
            except RuntimeError as e:
                print(e)
                continue
            except: 
                print("Something was wrong")
                continue
        
        if choice == '+':
            return x+y
        elif choice == '-':
            return x-y
        elif choice == '*':
            return x*y
        elif choice == '/':
            return x/y
    except ZeroDivisionError:
        return "The division by zero is not possible"
    except:
        print("something went wrong")


print(calculate())