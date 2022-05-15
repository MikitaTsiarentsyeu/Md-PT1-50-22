import datetime
from num2words import num2words as n2w

current_time = datetime.datetime.now().strftime('%H:%M').split(':')

def result(hours, minutes):
    if minutes == 0:
        return(f'{n2w(hours-12)} o\'clock') if hours > 12 else (f'{n2w(hours)} o\'clock')
    elif minutes < 30 or 30 < minutes < 45:
        return(f'{n2w(minutes)} minutes past {n2w(hours-12)}') if hours > 12\
            else(f'{n2w(minutes)} minutes past {n2w(hours)}')
    elif minutes == 30:
        return (f'half past {n2w(hours - 12)}') if hours > 12 else (f'half past {n2w(hours)}')
    else:
        return (f'{n2w(60-minutes)} minutes to {n2w(hours-11)}') if hours > 12\
            else (f'{n2w(60-minutes)} minutes to {n2w(hours+1)}')

choice = input('Enter your time in HH:MM format or enter "NOW" for local time ')
if choice == 'NOW':
    hours, minutes = int(current_time[0]), int(current_time[1])
    print(result(hours, minutes))
elif 0 <= int(choice.split(':')[0]) <= 24 and 0 <= int(choice.split(':')[1]) <= 59:
    hours, minutes = int(choice.split(':')[0]), int(choice.split(':')[1])
    print(result(hours, minutes))
else:
    print('Enter correct information')