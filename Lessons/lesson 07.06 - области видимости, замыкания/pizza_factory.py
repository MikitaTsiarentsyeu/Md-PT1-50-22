def prepare():
    print("STARTING OF THE PIZZAMAKING PROCESS")
    print("preparing a base")
    print("adding a sauce")

def add_ingridient(ingridient):
    print(f"adding {ingridient}")

def grind_cheese():
    print("griding cheese")

def bake(time):
    print(f"baking the pizza for {time} minutes")

def done():
    print("slicing...")
    print("boxing...")
    print("DONE!")

# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(10)
#     done()

# def make_double_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(10)
#     done()

# def make_4_cheeses():
#     prepare()
#     add_ingridient("chedder")
#     add_ingridient("mozarella")
#     add_ingridient("alfredo")
#     add_ingridient("blue cheese")
#     grind_cheese()
#     bake(15)
#     done()

def pizza_factory(ingridients, time):
    def maker():
        prepare()
        for i in ingridients:
            add_ingridient(i)
        grind_cheese()
        if time > 0:
            bake(time)
        done()
    return maker

make_pepperoni = pizza_factory(["pepperoni"], 15)
make_double_pepperoni = pizza_factory(["pepperoni", "pepperoni"], 15)
make_4_cheeses = pizza_factory(["chedder", "mozarella", "alfredo", "blue cheese"], 10)

make_pepperoni()
make_double_pepperoni()
make_4_cheeses()