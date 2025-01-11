n = int(input())

for _ in range(n):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        print(s[0] + str(len(s[1:-1])) + s[-1])

