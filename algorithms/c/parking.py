

def solution(E, L):
    enter_hours = int(E[0:2])
    enter_mins = int(E[3:])
    leave_hours = int(L[0:2])
    leave_mins = int(L[3:])

    hours = leave_hours - enter_hours
    if leave_mins > enter_mins:
        hours += 1
    cost = 0

    if hours:
        cost = 5
        if hours > 1:
            cost += (hours - 1) * 4

    return cost


def solution1(E, L):
    hours = int(L[0:2]) - int(E[0:2])
    if int(L[3:]) > int(E[3:]):
        hours += 1
    return 5 + (hours - 1) * 4


if __name__ == '__main__':
    print()
    print(solution("10:00", "13:21"))
    print(solution("09:42", "11:42"))
    print()
    print(solution1("10:00", "13:21"))
    print(solution1("09:42", "11:42"))