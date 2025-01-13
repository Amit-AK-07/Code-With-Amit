t = int(input())

for _ in range(t):
    ratings = int(input())

    if ratings >= 1900:
        print("Division 1")

    elif ratings >= 1600 and ratings <= 1899:
        print("Division 2")

    elif ratings >= 1400 and ratings <= 1599:
        print("Division 3")

    else:
        print("Division 4")
