s = input()

upper_count = sum(1 for a in s if a.isupper())
lower_count = sum(1 for a in s if a.islower())

if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())