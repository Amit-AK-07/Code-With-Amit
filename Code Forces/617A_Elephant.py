x = int(input())
elephant_step = x // 5

if x % 5 != 0:
    elephant_step += 1
print(elephant_step)