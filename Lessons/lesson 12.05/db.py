db = {9103976271:("Reina Meinhard", "Memphis", "Tennessee"),
4199392609:("Stephanie Bruce", "Greensboro", "North Carolina"),
9099459979:("Ermes Angela", "Dallas", "Texas"),
6123479367:("Lorenza Takuya", "Indianapolis", "Indiana"),
7548993768:("Margarete Quintin", "Raleigh", "North Carolina")}

"the number was not found"

"Margarete Quintin from Raleigh, Nort Carolina"

number = int(input("please enter your number:"))

if number in db:
    print(f"{db[number][0]} from {db[number][1]}, {db[number][2]}")
else:
    print("the number was not found")

val = db.get(number)
if val:
    print(f"{val[0]} from {val[1]}, {val[2]}")
else:
    print("the number was not found")

print(f"{db[number][0]} from {db[number][1]}, {db[number][2]}") if number in db else print("the number was not found")