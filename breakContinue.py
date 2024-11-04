# Break statement

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

# Continue Statement - Skips a loop
devices = ["laptop", "phone", "tablet"]
for x in devices:
    if x == "laptop":
        continue
    print(x)