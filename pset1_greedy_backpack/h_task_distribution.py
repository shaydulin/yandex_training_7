def main():
    n = int(input())

    tasks = [[], []]
    ans = 0
    for _ in range(n):
        # res if task starts at vasya's day,
        # res if task starts at not vasya's day
        # task len is odd or even
        vasya, not_vasya, day_change = analyze(input())
        if vasya == not_vasya and not day_change:
            ans += vasya
        else:
            tasks[day_change].append((vasya, not_vasya))
    # print(tasks)

    # process tasks with odd lengths
    # even-length tasks do not affect
    # oddity of odd-length ones
    # sort tasks by the difference between results 
    # if task starts at vasya's day and not vasya's day
    # take tasks from both ends of list
    # it is possible to get the best result by swapping pair of them if necessary
    # choose the best between t1 + t2 and t2 + t1
    tasks_ = tasks[1]
    tasks_.sort(key=lambda task: task[1] - task[0])
    l, r = 0, len(tasks_) - 1
    while l < r:
        ans += tasks_[l][0] + tasks_[r][1]
        l += 1
        r -= 1
    if l == r:
        ans += tasks_[l][0]
    # process tasks with even lengths
    # if there is task with odd length it is possible
    # to process even-length tasks before odd-length ones or after
    # starting with the best odd or even day
    ans += sum(max(task) for task in tasks[0]) if tasks_ else sum(task[0] for task in tasks[0])
    print(ans)


def analyze(task):
    return (
        sum(task[i] == "S" for i in range(0, len(task), 2)),
        sum(task[i] == "S" for i in range(1, len(task), 2)),
        len(task) % 2,
    )


if __name__ == "__main__":
    main()
