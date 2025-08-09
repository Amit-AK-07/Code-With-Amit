def find_number_at_position(n, k):
    odd_count = (n + 1) // 2  # number of odd numbers from 1 to n
    if k <= odd_count:
        return 2 * k - 1
    else:
        return 2 * (k - odd_count)

# Input
n, k = map(int, input().split())
# Output
print(find_number_at_position(n, k))
