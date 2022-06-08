while True:
    user_input = input("Please enter your time value in the hh:mm format:")

    if len(user_input) != 5:
        print("Incorrect input, it has wrong length")
        continue

    if user_input[2] != ':':
        print("Incorrect input, it has no : symbol")
        continue

    values = user_input.split(':')
    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("Incorrect input, the hours and minutes values must be represented by digits")
        continue

    hours = int(hours)
    minutes = int(minutes)
    
    if hours > 23:
        print("Incorrect input, the hours value must be less than 24")
        continue

    if minutes > 59:
        print("Incorrect input, the minutes value must be less than 60")
        continue

    break

print("the main logic goes here")