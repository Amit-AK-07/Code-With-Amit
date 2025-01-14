y = int(input())
y += 1

while True:
    year = str(y)

    if len(set(year)) == len(year):
        print(y)
        break
    y += 1
