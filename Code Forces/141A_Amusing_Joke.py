guest_name = input().strip()
host_name = input().strip()
letters_in_pile = input().strip()

combined_name = guest_name + host_name

if sorted(combined_name) == sorted(letters_in_pile):
    print("YES")
else:
    print("NO")