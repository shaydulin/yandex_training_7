def main():
    data = open("input.txt").readlines()

    prev_snowmen = [None]
    last_action = [1]
    snowmen_mass = [0]

    # balls = [[]]

    for i in range(1, len(data)):
        j, m = map(int, data[i].split())
        if m:
            prev_snowmen.append(j if last_action[j] else prev_snowmen[j])
            snowmen_mass.append(snowmen_mass[j] + m)
            last_action.append(1)

            # balls.append(balls[j].copy())
            # balls[-1].append(m)
        else:
            last_action.append(0)
            prev_snowmen.append(prev_snowmen[j] if last_action[j] else prev_snowmen[prev_snowmen[j]])
            snowmen_mass.append(snowmen_mass[prev_snowmen[-1]])

            # balls.append(balls[j].copy())
            # balls[-1].pop()

    print(sum(snowmen_mass))


if __name__ == "__main__":
    main()
