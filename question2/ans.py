user_input = input("Enter your numbers: ")
split_input = user_input.split()
nums = []
for item in split_input:
    nums.append(float(item))

maximum = max(nums)
minimum = min(nums)
difference = maximum - minimum

print(f"{difference:.4f}")