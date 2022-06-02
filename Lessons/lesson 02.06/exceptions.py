l = [1,2,3,4,5]

try:
    for i in range(6):
        try:
            print(k[i])
        except (NameError, IndexError):
            if i == 5:
                raise SystemError("The index was too high")
            print("the inner NameError except")
            continue
        finally:
            print("hello from inner finally")
    print("some logic after the enumeration")
except IndexError as e:
    print(type(e))
    print("the index was incorrect")
except NameError:
    print("the outer NameError except")
except SystemError as e:
    print(e)
except:
    print("something went wrong")
finally:
    print("hello from outer finally")

# raise MemoryError

# with open("test.txt", 'w') as f: pass

# try:
#     f = open("test.txt", 'w')
# finally:
#     f.close()

print("the logic goes on")


