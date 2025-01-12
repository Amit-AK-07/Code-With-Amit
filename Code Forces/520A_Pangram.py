n = int(input())
s = input()

albhabets = set("abcdefghijklmnopqrstuvwxyz")
s_set = set(s.lower())

if albhabets.issubset(s_set):
    print("YES")
else:
    print("NO")