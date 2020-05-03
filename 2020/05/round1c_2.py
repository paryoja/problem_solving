def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        print("Case #{}: ".format(i), end="")

        max_range = pow(10, int(input())) - 1

        first = set()
        words = {}

        for case in range(10000):
            query, random = input().strip().split(" ")
            if len(random) >= 2:
                first.add(random[1])
            for c in random[:1]:
                words[c] = words.get(c, 0) + 1

        for c in first:
            if c not in words:
                zero = c
                break
        sorted_list = sorted([(k, v) for k, v in words.items()], key=lambda x: x[1], reverse=True)
        print("{}{}".format(zero, "".join([k[0] for k in sorted_list])))


main()
