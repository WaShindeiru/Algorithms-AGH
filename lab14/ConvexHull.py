class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def rotation(p1, p2, p3):
# 0 - współliniowe
# 1 - prawoskrętne
# 2 - lewoskrętne

    value = (p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)

    if value == 0:
        return 0

    return 1 if value > 0 else 2


def left_index(points):
    min_index = 0

    for i in range(1, len(points)):
        if points[min_index].x > points[i].x:
            min_index = i

        elif points[min_index].x == points[i].x:
            if points[min_index].y > points[i].y:
                min_index = i

    return min_index


def JarvisAlgorithm(list_of_nodes):
    size = len(list_of_nodes)
    list_of_points = [Point(x, y) for x, y in list_of_nodes]
    hull_indexes = list()

    p = min_index = left_index(list_of_points)

    while True:
        hull_indexes.append(p)

        q = p + 1
        if q == size:
            q = 0

        for i in range(size):
            if rotation(list_of_points[p], list_of_points[q], list_of_points[i]) == 1:
                q = i

        if q == min_index:
            break

        p = q

    return [list_of_nodes[i] for i in hull_indexes]


def JarvisAlgorithm_second_rev(list_of_nodes):
    size = len(list_of_nodes)
    list_of_points = [Point(x, y) for x, y in list_of_nodes]
    hull_indexes = list()

    p = min_index = left_index(list_of_points)

    while True:
        hull_indexes.append(p)

        q = p + 1
        if q == size:
            q = 0

        for i in range(size):
            rotation_value = rotation(list_of_points[p], list_of_points[q], list_of_points[i])
            if rotation_value == 1:
                q = i

            elif rotation(list_of_points[p], list_of_points[i], list_of_points[q]) == 0:
                p_point = list_of_points[p]
                i_point = list_of_points[i]
                q_point = list_of_points[q]

                if abs(q_point.x - p_point.x) <= abs(i_point.x - p_point.x) and abs(q_point.y - p_point.y) <= abs(i_point.y - p_point.y):
                    q = i

        if q == min_index:
            break

        p = q

    return [list_of_nodes[i] for i in hull_indexes]

def main():
    # First algorithm
    first = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    second = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]

    first_result = JarvisAlgorithm(first)
    second_result = JarvisAlgorithm(second)

    print(first_result)
    print(second_result)

    # Second algorithm
    second_first_result = JarvisAlgorithm_second_rev(first)
    second_second_result = JarvisAlgorithm_second_rev(second)
    print(second_first_result)
    print(second_second_result)
    print()

    third = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

    third_first_result = JarvisAlgorithm(third)
    third_second_result = JarvisAlgorithm_second_rev(third)
    print(third_first_result)
    print(third_second_result)


if __name__ == "__main__":
    main()