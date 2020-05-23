def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        print("Case #{}: ".format(i), end="")

        chunk, customer = map(int, input().strip().split(" "))

        chunk_size = list(map(int, input().strip().split(" ")))

        if len(chunk_size) == 1:
            print(customer - 1)
            continue

        multiply_map = {}
        multiply_set = set()
        for i, x in enumerate(chunk_size):
            for j, y in enumerate(chunk_size):
                if i == j:
                    continue
                if y % x == 0:
                    if i in multiply_map:
                        m_l = multiply_map[i]
                    else:
                        m_l = {}
                        multiply_map[i] = m_l
                    div = y // x

                    freq = m_l.get(div, 0) + 1
                    m_l[div] = freq
        # print(multiply_map)
        if not multiply_map:
            # multiple이 없어 -> 그냥 하나 자르는 거랑 같음
            print(customer - 1)
            continue

        if customer == 2:
            stop = False
            for k, v in multiply_map.items():
                if 1 in v:
                    print("0")
                    stop = True
                    break
            if not stop:
                print("1")
            continue
        # print(multiply_map)
        if customer == 3:
            sum_to_2 = 0
            for k, v in multiply_map.items():
                if 1 in v:
                    if v[1] >= 2:
                        sum_to_2 = 2

                if 2 in v:
                    sum_to_2 = max(sum_to_2, 1)

            if sum_to_2 == 0:
                for k, v in multiply_map.items():
                    if 1 in v:
                        for idx, size in enumerate(chunk_size):
                            if k != idx:
                                if chunk_size[k] < size:
                                    sum_to_2 = 1

            print(customer - 1 - sum_to_2)

        # print(multiply_map)


main()
