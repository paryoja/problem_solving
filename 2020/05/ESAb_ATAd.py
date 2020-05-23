import sys

T, B = map(int, input().split(" "))

trial = 0

# f = open("debug.txt", "w")


def p(x):
    global trial

    print(x)
    sys.stdout.flush()
    trial += 1
    return int(input())


def query_pair(idx):
    x = p(1 + idx)
    y = p(B - idx)
    return [x, y]


def print_result(pair):
    result_array = [0] * B

    for k, v in pair.items():
        result_array[k] = v[0]
        result_array[B - k - 1] = v[1]
    print("".join(map(str, result_array)))

    # f.write("{}\n".format(pair))
    # f.flush()

    sys.stdout.flush()

    if input() == "Y":
        return True
    else:
        return False


for case in range(1, T + 1):
    # f.write("Case #{}\n".format(case))
    trial = 0

    change_detection = False

    unk_list = list(range(5, B // 2))

    data_pair = {0: query_pair(0), 1: query_pair(1), 2: query_pair(2), 3: query_pair(3), 4: query_pair(4)}

    flip = -1
    rev = -1
    for k, v in data_pair.items():
        if v[0] == v[1]:
            # bit flip 찾기용
            flip = k
        else:
            # reverse 찾기용
            rev = k
    # f.write(str(data_pair))
    # f.write("\n")
    # f.flush()
    # f.write("flip {}\n".format(flip))
    # f.write("rev {}\n".format(rev))

    while True:
        # query
        if trial == 150:
            # maximum query
            break

        # 다 찾았는지 확인
        if not unk_list:
            print_result(data_pair)
            break

        if flip != -1:
            flip_bit = p(flip + 1)
            if flip_bit == data_pair[flip][0]:
                to_flip = False
            else:
                to_flip = True

            if to_flip:
                for k, v in data_pair.items():
                    if v[0] == 0:
                        v[0] = 1
                    else:
                        v[0] = 0

                    if v[1] == 0:
                        v[1] = 1
                    else:
                        v[1] = 0
        else:
            p(1)
        # 0 1 -> 1 0, flip x => rev o
        # 0 1 -> 0 1, flip x => rev x
        if rev != -1:

            rev_bit = p(rev + 1)
            if rev_bit == data_pair[rev][0]:
                to_rev = False
            else:
                to_rev = True

            if to_rev:
                for k, v in data_pair.items():
                    t = v[0]
                    v[0] = v[1]
                    v[1] = t
        else:
            p(1)

        for _ in range(4):
            unk = unk_list.pop()
            pair = query_pair(unk)
            if pair[0] == pair[1]:
                flip = unk
            else:
                rev = unk
            data_pair[unk] = pair

            if not unk_list:
                break
