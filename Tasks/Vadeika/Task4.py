"""Task4."""

# Function1
row = 'The quick Brown Fox'


def check_str(arg_str):

    enum_uppper, enum_lower = [sum(i.isupper() for i in arg_str), sum(i.islower() for i in arg_str)]
    print(f"check_str('{row}') ->'{enum_uppper} upper case, {enum_lower} lower case'")


check_str(row)


# Function2
num = 787  # Enter number


def is_prime(num):
    while True:
        if num <= 0:
            print('Enter a number greater than zero')
            break
        else:
            var = 0
            for i in range(2, num // 2 + 1):
                if (num % i == 0):
                    var = var + 1
            if (var <= 0):
                print(f'is_prime({num}) -> True')
                break
            else:
                print(f'is_prime({num}) -> False')
                break


is_prime(num)

# Function3

def get_ranges(arr):
    numbers = []
    for item in arr:
        if item == arr[0] or numbers[-1] == ", " or item == arr[-1]:
            numbers.append(str(item))
            if item == arr[-1]:
                continue
            if item == arr[arr.index(item) + 1] - 1:
                numbers.append("-")
            if item != arr[arr.index(item) + 1] - 1:
                numbers.append(", ")
        elif item != arr[arr.index(item) + 1] - 1:
            numbers.append(str(item))
            numbers.append(", ")

    return "".join(numbers)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
