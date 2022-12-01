f = open("dayoo.txt", "r")
calories = []
calorie = 0
for x in f:
    if x == '\n' or x == '':
        calories.append(calorie)
        calorie = 0
    elif x.isnumeric:
        calorie += int(x)
calories.sort()
print(max(calories))
top_three = calories[-1] + calories[-2] + calories[-3]
print(top_three)