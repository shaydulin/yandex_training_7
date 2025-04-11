def main():
    n, m = map(int, input().split())
    students_in_groups = list(map(int, input().split()))
    seats_in_classes = list(map(int, input().split()))

    groups_idcs_by_students = sorted(
        range(n),
        key=lambda i: students_in_groups[i]
    )
    classes_idcs_by_seats = sorted(
        range(m),
        key=lambda j: seats_in_classes[j]
    )
    i = 0
    j = 0
    ans = 0
    distribution = [0] * n
    while i < n and j < m:
        group = groups_idcs_by_students[i]
        class_ = classes_idcs_by_seats[j]
        if students_in_groups[group] < seats_in_classes[class_]:
            distribution[group] = class_ + 1
            ans += 1
            j += 1
            i += 1
        else:
            j += 1

    print(ans)
    print(*distribution)


if __name__ == "__main__":
    main()
