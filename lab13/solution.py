import time


def string_compare(P: str, T: str, i: int, j: int) -> int:
    if i == 0:
        return j

    if j == 0:
        return i

    zamian = string_compare(P, T, i-1, j-1) + (P[i] != T[j])
    wstawien = string_compare(P, T, i, j-1) + 1
    usuniec = string_compare(P, T, i-1, j) + 1

    lowest_cost = min(zamian, wstawien, usuniec)

    return lowest_cost


def string_compare_dynamic(P: str, T: str, i: int, j: int):
    tab = [[0 for _ in range(j+1)] for __ in range(i+1)]
    for _ in range(j+1):
        tab[0][_] = _

    for _ in range(i + 1):
        tab[_][0] = _

    parent_tab = [['X' for _ in range(j + 1)] for __ in range(i+1)]

    for _ in range(1, j+1, 1):
        parent_tab[0][_] = 'I'

    for _ in range(1, i+1, 1):
        parent_tab[_][0] = 'D'

    for i_ in range(1, i+1, 1):
        for j_ in range(1, j+1, 1):
            zamian = tab[i_-1][j_-1] + (P[i_] != T[j_])
            was_changed = P[i_] != T[j_]
            wstawien = tab[i_][j_-1] + 1
            usuniec = tab[i_-1][j_] + 1

            lowest_cost = min(zamian, wstawien, usuniec)

            tab[i_][j_] = lowest_cost

            if zamian == lowest_cost:
                if was_changed:
                    parent_tab[i_][j_] = 'S'
                else:
                    parent_tab[i_][j_] = 'M'

            elif wstawien == lowest_cost:
                parent_tab[i_][j_] = 'I'

            elif usuniec == lowest_cost:
                parent_tab[i_][j_] = 'D'

    history_list = list()

    i_, j_ = i, j
    while parent_tab[i_][j_] != 'X':
        history_list.append(parent_tab[i_][j_])

        if parent_tab[i_][j_] in ('S', 'M'):
            i_ -= 1
            j_ -= 1

        elif parent_tab[i_][j_] == 'I':
            j_ -= 1

        elif parent_tab[i_][j_] == 'D':
            i_ -= 1

    history_list.reverse()

    return tab[i][j], "".join(history_list)


# d)
def find_string(P: str, T: str, i: int, j: int):
    tab = [[0 for _ in range(j+1)] for __ in range(i+1)]
    # for _ in range(j+1):
    #     tab[0][_] = _

    for _ in range(i + 1):
        tab[_][0] = _

    parent_tab = [['X' for _ in range(j + 1)] for __ in range(i+1)]

    # for _ in range(1, j+1, 1):
    #     parent_tab[0][_] = 'X'

    for _ in range(1, i+1, 1):
        parent_tab[_][0] = 'D'

    zamian = 0
    for i_ in range(1, i+1, 1):
        for j_ in range(1, j+1, 1):
            if P[i_] != T[j_]:
                zamian = tab[i_-1][j_-1] + 1
            else:
                zamian = tab[i_-1][j_-1]
            was_changed = P[i_] != T[j_]
            wstawien = tab[i_][j_-1] + 1
            usuniec = tab[i_-1][j_] + 1

            lowest_cost = min(zamian, wstawien, usuniec)

            tab[i_][j_] = lowest_cost

            if zamian == lowest_cost:
                if was_changed:
                    parent_tab[i_][j_] = 'S'
                else:
                    parent_tab[i_][j_] = 'M'

            elif wstawien == lowest_cost:
                parent_tab[i_][j_] = 'I'

            elif usuniec == lowest_cost:
                parent_tab[i_][j_] = 'D'

    history_list = list()

    i__ = len(P) - 1
    j__ = 0

    for k in range(1, len(T), 1):
        if tab[i__][k] < tab[i__][j__]:
            j__ = k

    i_, j_ = i, j
    while parent_tab[i_][j_] != 'X':
        history_list.append(parent_tab[i_][j_])

        if parent_tab[i_][j_] in ('S', 'M'):
            i_ -= 1
            j_ -= 1

        elif parent_tab[i_][j_] == 'I':
            j_ -= 1

        elif parent_tab[i_][j_] == 'D':
            i_ -= 1

    history_list.reverse()

    return j__ - len(P) + 2

# e)
def longest_sequence(P: str, T: str, i: int, j: int):
    tab = [[0 for _ in range(j+1)] for __ in range(i+1)]
    for _ in range(j+1):
        tab[0][_] = _

    for _ in range(i + 1):
        tab[_][0] = _

    parent_tab = [['X' for _ in range(j + 1)] for __ in range(i+1)]

    for _ in range(1, j+1, 1):
        parent_tab[0][_] = 'I'

    for _ in range(1, i+1, 1):
        parent_tab[_][0] = 'D'

    for i_ in range(1, i+1, 1):
        for j_ in range(1, j+1, 1):
            if P[i_] != T[j_]:
                zamian = tab[i_-1][j_-1] + 10000
            else:
                zamian = tab[i_-1][j_-1]
            was_changed = P[i_] != T[j_]
            wstawien = tab[i_][j_-1] + 1
            usuniec = tab[i_-1][j_] + 1

            lowest_cost = min(zamian, wstawien, usuniec)

            tab[i_][j_] = lowest_cost

            if zamian == lowest_cost:
                if was_changed:
                    parent_tab[i_][j_] = 'S'
                else:
                    parent_tab[i_][j_] = 'M'

            elif wstawien == lowest_cost:
                parent_tab[i_][j_] = 'I'

            elif usuniec == lowest_cost:
                parent_tab[i_][j_] = 'D'

    history_list = list()
    word = list()

    i_, j_ = i, j
    while parent_tab[i_][j_] != 'X':
        history_list.append(parent_tab[i_][j_])

        if parent_tab[i_][j_] in ('S', 'M'):
            if parent_tab[i_][j_] == 'M':
                word.append(P[i_])
            i_ -= 1
            j_ -= 1

        elif parent_tab[i_][j_] == 'I':
            j_ -= 1

        elif parent_tab[i_][j_] == 'D':
            i_ -= 1

    word.reverse()

    return "".join(word)

def main():
    # a)
    P = ' kot'
    T = ' pies'
    print(string_compare(P, T, len(P) - 1, len(T) - 1))

    # print("Programowanie dynamiczne: ")
    P = ' bialy autobus'
    T = ' czarny autokar'
    print(string_compare_dynamic(P, T, len(P) - 1, len(T) - 1)[0])

    # c)
    P = ' thou shalt not'
    T = ' you should not'
    value, history = string_compare_dynamic(P, T, len(P) - 1, len(T) - 1)
    print(history)

    # d)
    P = ' ban'
    T = ' mokeyssbanana'
    print(find_string(P, T, len(P) - 1, len(T) - 1))

    # e)
    P = ' democrat'
    T = ' republican'
    print(longest_sequence(P, T, len(P) - 1, len(T) - 1))

    # f)
    P = ' 243517698'
    T = "".join(sorted(list(P)))
    print(longest_sequence(P, T, len(P) - 1, len(T) - 1))

if __name__ == "__main__":
    main()