t = int(input())

for _ in range(t):
    x_coordinates = set()
    y_coordinates = set()

    for i in range(4):
        x, y = map(int, input().split())
        x_coordinates.add(x)
        y_coordinates.add(y)

    length = max(abs(max(x_coordinates) - min(x_coordinates)), abs(max(y_coordinates) - min(y_coordinates)))
    area = length ** 2

    print(area)