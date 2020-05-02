import math

# global_step = 0


def to_binary_index(num):
    index = []
    idx = 0

    while num:
        if num % 2:
            index.append(idx)
        idx += 1
        num = num // 2

    # prisnt(index)
    return index, idx


def print_position(position):
    print(position[0], end=" ")
    print(position[1])


def sidewalk(left, position, step):
    # global global_step
    for _ in range(step):
        # global_step += 1
        print_position(position)

        if left:
            position[0] += 1
        else:
            position[0] += 1
            position[1] += 1
    return position


def cross_line(position, index, left):
    # global global_step
    # global_step += int(math.pow(2, index))
    # print("cross", position)
    print_position(position)
    for _ in range(index):
        if left:
            position[1] += 1
        else:
            position[1] -= 1
        print_position(position)

    return position


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        print("Case #{}:".format(i))

        number = int(input())

        position = [1, 1]

        if number < 30:
            sidewalk(True, position, number)
        else:
            index_list, max_index = to_binary_index(number - 30)
            leftover = 30

            left = True
            for x in range(max_index):
                if x in index_list:
                    position = cross_line(position, x, left)
                    left = not left

                    position[0] += 1
                    if not left:
                        position[1] += 1

                else:
                    position = sidewalk(left, position, 1)
                    leftover -= 1
                    # print(leftover)
            # print("left", leftover)
            # print(global_step)
            sidewalk(left, position, leftover)
        # print(global_step)


if __name__ == "__main__":
    main()
