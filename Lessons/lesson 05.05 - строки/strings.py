s = "this is a string"

s = 'this is a string'

s = "some value 'test'"

s = 'some value \'test\''

s = "some value \"test\""

print(s, type(s))

print(type(str(6)))

s = "line 1\tline 2\nline 3"
print(s)

s = """line 1
line 2
line 3"""

print(s)

s = "my very long string"
print(s[0], s[1], s[2], s[3])
#print(s[345678])
print(s[-1], s[-2], s[-3])
print(s[1:7])
print(s[3:-3])
print(s[10:-13])
print(s[::-1])
print(s[::3])

#s[2.5]
#s[0] = 't'

s = "test"
print(id(s))
s = "not test"
print(id(s))
s += " yet"
print(id(s))
print(s)

print("one," + " two, " + "three")

print("AAA"*10)

print(""*10)

x = ""
print(x, type(x), len(x))
print(len("test"))
s[len(s)-1] == s[-1]

print("test" in s)
print("ffghjhk" in s)
print('' in s)

print(s.find('t'), s[s.find('t')])
print(s.find('test'), s[s.find('test')])
print(s.find('hfdydu'))

print(s.replace(' ', "!@#$%^&*").replace("!", "   ").replace("*", " ").replace("@#$%^&", ""))

# print(s.upper().lower())
print(s.upper(), s)
s = s.upper()
print(s)

print(s.lower().split('t'))
print(s.split("TEST"))
s = "1234:adidas-n353rt"
print(s.replace('-', ':').split(':'))

print(' '.join(["some", "test", "value"]))
print('@#$%^&*(^%$#@#$%^&*'.join(["some", "test", "value"]))
print(''.join(["some", "test", "value"]))

s = "some test string"
print(''.join(s.split()))

c, d, p = 'cat', 'dog', 'parrot'
s = "a " + c + ", a " + d + ", a " + p
"a cat"
"a cat, a"
"a cat, a dog"
"a cat, a dog, a "
"a cat, a dog, a parrot"
print(s)

print("a {}, a {}, and a {}".format(c, d, p))
print("a {1}, a {0}, and a {2}".format(c, d, p))
print("a {c}, a {d}, and a {p}".format(c='cat', d='dog', p='parrot'))

print(f"a {c}, a {d}, and a {p}")

print(f"some value = {True if False else False}")