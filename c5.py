n = int(input())

ani = []
do = []

for i in range(n):
    ani.append(input())
for j in range(n):
    do.append(int(input()))

daily_descriptions = []
for k in range(n):
    daily_descriptions.append((ani[k], do[k]))

total_food = 0
top_eater = ""
lowest_eater_index = 0
mx = -float('inf')
mn = float('inf')

for i in range(n):
    if do[i] >= 5:
        total_food += do[i]
    if do[i] > 100:
        break

for i in range(n):
    if do[i] < mn:
        mn = do[i]
        lowest_eater_index = i
    if do[i] > mx:
        mx = do[i]
        top_eater = ani[i]

print(daily_descriptions)
print(total_food)
print(top_eater)
print(lowest_eater_index)