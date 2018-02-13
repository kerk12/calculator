def add(x, y):
    return x+y+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y

# Get the calculation from the user.
type = input("Choose the type of calculation (add, subtract, multiply, divide)\n")

# Get possible calculations
possibles = locals().copy()
method = possibles.get(type)
if not method:
     raise NotImplementedError("Method %s not implemented" % type)


try:
	x = int(input())
	y = int(input())
	print(method(x,y))
except ValueError:
	print("Invalid input")