t = int(input())

for _ in range(t):
    a = input().strip()

    if a == 'abc' or a == 'acb' or a == 'bac' or a == 'cba':
        print("YES")
    else:
        print("NO")

