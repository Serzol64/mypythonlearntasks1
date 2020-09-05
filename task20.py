def all_unique(numbers):
    task = len(numbers) == len(set(numbers))

    if task: print("Все запрашиваемые числа уникальны в последовательности;-)")
    else: print("Все запрашиваемые числа неуникальны в последовательности;-(")

nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))
print(result)

all_unique(nums)