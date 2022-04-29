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
		initial_var = int(input(f"Enter your {init} {sub_str}: "))
		return initial_var
	except:
		print('Sorry, wrong value, please try again')
		return input_initial(init)
		
def input_time_unit():
	time_unit = input('What kind of time unites do you prefer (year, month, day)?  ').lower() 
	if time_unit in ["year", "month", "day"]:
		return time_unit
	else:
		print("invalid unit, please try again")
		return input_time_unit()
	   	
def calculation_deposit(amount, duration, percent, factor):
    total = round((amount * (1 + percent / 100 / factor) ** (duration * factor)), 2)
    diff = round((total - amount), 2)
    print("Your total deposit amount after {} years is: {}\n total interest: {}".format(duration, total, diff))
    

def main():
    amount = input_initial('amount')
    duration = input_initial('duration', '(int in years)')
    time_unit = input_time_unit()
    percent = input_initial("percent")
    if time_unit == "year":
        factor = 1
        calculation_deposit(amount, duration, percent, factor)
    elif time_unit == "month":
        factor = 12
        calculation_deposit(amount, duration, percent, factor)
    elif time_unit == "day":
        factor = 365
        calculation_deposit(amount, duration, percent, factor)
    else:
        print("Sorry, we cant calculate this =(")
        
    continue_calulations =  input("Do you want to calculate another deposit (yes or no): ").lower()
        
    main() if continue_calulations in  ["y" , "yes", "yep", "ya", "ye"] else None
        	
 
        
if __name__ == "__main__":    
    main()