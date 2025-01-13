t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    n = [a, b, c]
    n.sort()

    print(n[1])