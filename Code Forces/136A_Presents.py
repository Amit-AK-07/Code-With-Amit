n = int(input())
p = list(map(int, input().split()))

ans = [0] * n

for giver, reveiver in enumerate(p, start = 1):
    ans[reveiver - 1] = giver

print(" ".join(map(str, ans)))