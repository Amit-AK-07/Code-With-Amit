t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    possible = True

    for i in range(1, n):
        if abs(a[i] - a[i - 1] > 1):
            possible = False
            break
    
    print("YES" if possible else "NO")
