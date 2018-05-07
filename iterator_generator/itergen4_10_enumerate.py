my_list = ['a', 'b', 'c']
print(enumerate(my_list))
for idx, val in enumerate(my_list):
    print(idx, val)  # 0-2

for idx, val in enumerate(my_list, start=1):
    print(idx, val)  # 1-3
