import random

count = {}

for _ in range(1000):

    x = random.randint(1, 10000000)

    y = random.randint(1, x)


    for c in str(y)[:1]:
        count[c] = count.get(c, 0) + 1

words = count
sorted_list = sorted([(k, v) for k, v in words.items()], key=lambda x: x[1], reverse=True)

print(sorted_list)