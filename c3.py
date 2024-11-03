def Evaluate(x):
    if x >= 190:
        return "Xuat sac"
    elif x >= 150:
        return "Gioi"
    elif x >= 100:
        return "Kha"
    return "Yeu"


n = int(input())

res = []

for i in range(n):
    name = input()
    point_1 = int(input())
    point_2 = int(input())
    x = point_1 + point_2
    print (f"{i+1} {name} {x} {Evaluate(x)}")