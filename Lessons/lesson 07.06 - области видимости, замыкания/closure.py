def maker(n):
    def action(x):
        print(n)
        return x**n
    return action

square = maker(2)
print(square(3))
print(square(4))

cube = maker(3)
forth = maker(4)

degrees = [maker(x) for x in range(1,101)]
for degree in degrees:
    print(degree(2))