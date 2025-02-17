print("Ushbu dastur sizga sonni tartiblab beradi juftlarini o'gga toqlari chapda")

nums = list(map(int, input("son kiriting space bilan >>> ").split()))

nums_t = sorted(nums, key=lambda x: 1 if x % 2 == 0 else 0)
nums_t_ = sorted(nums, key=lambda x: x + 100  if x % 2 == 0 else x)
print("bu juf", *nums_t_)
print(*nums_t)


sum_juft = sum(x for x in nums if x % 2 == 0)
print(sum_juft)

print("hello world")
print((i for i in range(10000000000000)))

"""
----------------------------salom----------------------------
"""
