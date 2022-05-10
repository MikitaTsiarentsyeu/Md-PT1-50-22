#simplest implementation
amount, duration, percent, factor = 20000, 5, 15, 12
simplest_total_deposit = round(amount * ((1 + percent / 100 / factor) ** (duration * factor)),2)

print(simplest_total_deposit)

#simple lambda-function for calculation total amount of deposit after 5 years

lambda_total_deposit = lambda amount = 20000, duration = 5, percent= 15, factor = 12: round((amount * (1 + percent / 100 / factor) ** (duration * factor)),2)

print(lambda_total_deposit())



#function with some simple logic:
def input_initial(init, sub_str = ""):
   
    try:
        initial_var = int(input(f"Enter your {init} {sub_str}:\n"))
        return initial_var
    except:
        print('Sorry, wrong value, please try again')
        return input_initial(init)
		
def input_time_unit():
   
    time_unit = input('Enter kind of time unites do you prefer (year, month, day):\n').lower() 
    if time_unit in ["year", "month", "day"]:
        return time_unit
    else:
        print("invalid unit, please try again")
        return input_time_unit()
    

def calculate_second_operand(duration, percent, factor): 
    	   	return (1 + percent / 100 / factor) ** (duration * factor)
     
     
     
def calculation_deposit(amount, degree):
    total = round((amount * degree), 2)
    return total

def calculate_difference(amount, total): 
    return round((total - amount),2)



def print_answer(total, diff, duration): 
    print(f"Your total deposit amount after {duration} years is: {total}\n total interest: {diff}")



def calculation_depence_unit(time_unit, amount, duration, percent):
    if time_unit == "year":
        second_arg_for_total = calculate_second_operand(duration, percent, factor=1)
        total = calculation_deposit(amount, second_arg_for_total)
        diff = calculate_difference(amount, total)
        print_answer(total, diff, duration)
    elif time_unit == "month":
        second_arg_for_total = calculate_second_operand(duration, percent, factor=12)
        total = calculation_deposit(amount, second_arg_for_total)
        diff = calculate_difference(amount, total)
        print_answer(total, diff, duration)
    elif time_unit == "day":
        second_arg_for_total = calculate_second_operand(duration, percent, factor=365)
        total = calculation_deposit(amount, second_arg_for_total)
        diff = calculate_difference(amount, total)
        print_answer(total, diff, duration)
    else:
        print("Sorry, we can't calculate this =(")


def main():
    
    amount = input_initial('amount')
    duration = input_initial('duration', '(int in years)')
    time_unit = input_time_unit()
    percent = input_initial("percent")
    calculation_depence_unit(time_unit, amount, duration, percent)
    continue_calulations =  input("Do you want to calculate another deposit (yes or no): ").lower()
    main() if continue_calulations in  ["yes" , "y", "yep", "ya", "ye"] else None
        	
if __name__ == "__main__":    
    main()