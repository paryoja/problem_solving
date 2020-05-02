def round(data, row, col, white_list):
    deleted_list = []
    interest = 0
    for r in range(row):
        for c in range(col):
            position = (r, c)

            current = data[r][c]
            if current == 0:
                white_list.add(position)
                continue
            interest += current
            if position in white_list:
                continue

            competitor = 0
            count = 0

            # search upward
            for x in range(r - 1, -1, -1):
                if data[x][c] != 0:
                    competitor += data[x][c]
                    count += 1
                    break

            # search down
            for x in range(r + 1, row, 1):
                if data[x][c] != 0:
                    competitor += data[x][c]
                    count += 1
                    break

            # search left
            for y in range(c - 1, -1, -1):
                if data[r][y] != 0:
                    competitor += data[r][y]
                    count += 1
                    break

            # search down
            for y in range(c + 1, col, 1):
                if data[r][y] != 0:
                    competitor += data[r][y]
                    count += 1
                    break

            # print(r, c, competitor, count)
            if count:
                if current * count < competitor:
                    deleted_list.append(position)
                    white_list.add(position)

    # pprint.pprint(data)
    # print(interest)

    for position in deleted_list:
        data[position[0]][position[1]] = 0

    if deleted_list:
        return True, interest
    else:
        return False, interest


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        row, col = input().strip().split(" ")
        row = int(row)
        col = int(col)

        data = []
        for r in range(row):
            data.append(list(map(int, input().strip().split())))

        # print(data)
        white_list = set()
        interest = 0
        while True:
            need, inter = round(data, row, col, white_list)

            interest += inter
            if not need:
                break

        print("Case #{}: {}".format(i, interest))


if __name__ == "__main__":
    main()
