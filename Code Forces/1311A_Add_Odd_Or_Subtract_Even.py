t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    if a == b:
        print(0)
    elif a < b:
        print(1 if (b - a) % 2 == 1 else 2)
    else:
        print(1 if (a - b) % 2 == 0 else 2)