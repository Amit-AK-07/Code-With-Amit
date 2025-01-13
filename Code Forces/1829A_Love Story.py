t = int(input())
string = "codeforces"

for _ in range(t):
    str = input().strip()

    count = 0
    for i in range(10):
        if str[i] != string[i]:
            count += 1
    print(count)