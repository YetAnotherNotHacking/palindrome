def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome_depth(num):
    depth = 0
    while not is_palindrome(num):
        reverse_num = int(str(num)[::-1])
        num += reverse_num
        depth += 1
        print(f"Palindrome attempt {depth}: {num}")
    return depth

def palindrome_depth_range(start, end):
    results = {}
    for num in range(start, end + 1):
        results[num] = palindrome_depth(num)
    return results

start_num = int(input("Enter the start of the range: "))
end_num = int(input("Enter the end of the range: "))

result = palindrome_depth_range(start_num, end_num)
print("Palindrome depths for the range {} to {}:".format(start_num, end_num))
for num, depth in result.items():
    print("Number:", num, "Depth:", depth)

# Print a second time sorting them by their depth
print("\nPalindrome depths for the range {} to {} sorted by depth:".format(start_num, end_num))
for num, depth in sorted(result.items(), key=lambda x: x[1]):
    print("Number:", num, "Depth:", depth)

# Show highest palindrome depth and num
max_depth = max(result.items(), key=lambda x: x[1])
print("\nNumber with the highest palindrome depth is {} with a depth of {}".format(max_depth[0], max_depth[1]))

