def find_min_y_with_common_digit(x):
    x_digits = set(str(x))
    for y in range(1001):  # Since x can go up to 1000, y will also be within this range
        if x_digits & set(str(y)):  # Check for common digit
            return y
    return -1  # Should never reach here

t = int(input())
for _ in range(t):
    x = int(input())
    print(find_min_y_with_common_digit(x))
