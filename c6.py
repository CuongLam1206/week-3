import math


def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def is_binary(x):
    if x < 0:
        return 0
    else:
        return 1


def is_sigmoid(x):
    return 1 / (1 + math.e ** (-x))


def is_elu(x, alp=0.01):
    if x < 0:
        return alp * (math.e ** x - 1)
    else:
        return x


while True:
    x = input(">> Nhập vào số x = ")
    if is_number(x):
        x = float(x)
        break
    else:
        print("x là 1 số.")

acti_functions = {
    'binary': is_binary,
    'sigmoid': is_sigmoid,
    'elu': is_elu
}

while True:
    func = input("Input acti Function ( binary | sigmoid | elu ) : ").lower()
    if func not in acti_functions:
        print(f"{func} is not supported.")
    else:
        res = acti_functions[func](x)
        print(f"{func} : f({x}) = {res}")
        break