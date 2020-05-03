def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        print("Case #{}:".format(i), end="")

        row, col, movement = input().strip().split(" ")
        row = int(row)
        col = int(col)

        current_distance = [row, col]

        time = 1
        picture = -1
        for w in movement:
            if w == "W":
                current_distance[0] -= 1
            elif w == "E":
                current_distance[0] += 1
            elif w == "S":
                current_distance[1] -= 1
            else:
                current_distance[1] += 1

            if time >= abs(current_distance[0]) + abs(current_distance[1]):
                picture = time
                break
            time += 1

        if picture >= 0:
            print(" {}".format(picture))
        else:
            print(" IMPOSSIBLE")


main()
