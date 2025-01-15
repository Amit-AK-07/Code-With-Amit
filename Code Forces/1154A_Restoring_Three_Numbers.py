x = list(map(int, input().split()))
x.sort()

a_b_c = max(x)
x.remove(a_b_c)

a_b =x[0]
a_c = x[1]
b_c = x[2]

a = a_b_c - b_c
b = a_b_c - a_c
c = a_b_c - a_b

print(a, b, c)