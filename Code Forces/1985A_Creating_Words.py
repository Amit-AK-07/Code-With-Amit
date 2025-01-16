t = int(input())

for _ in range(t):
    a, b = input().strip().split()

    if len(a) == 3 and len(b) == 3:
        a, b = b[0] + a[1:], a[0] + b[1:]
        print(a, b)

