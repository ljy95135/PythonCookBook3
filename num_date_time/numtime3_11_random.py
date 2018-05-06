import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.sample(values, 2))

# shuffle in place
random.shuffle(values)
print(values)

# randint
print(random.randint(0, 10))  # 0-10
print(random.random())  # [0,1)
print(random.getrandbits(100))  # 0,2^100-1
