import math

import networkx
import matplotlib.pyplot as plt


def point_vs_vector(point, vector):
    check = (point[0] - vector[0][0]) * (vector[1][1] - vector[0][1]) - (point[1] - vector[0][1]) * (
            vector[1][0] - vector[0][0])
    if check == 0:
        return 0
    if check > 0:
        return 1
    if check < 0:
        return -1


def check_distance(point, triangle):
    v1 = triangle[0]
    v2 = triangle[1]
    v3 = triangle[2]

    def distance_to_segment(point_, vector_):
        p = vector_[1][1] - vector_[0][1]
        q = vector_[0][0] - vector_[1][0]
        r = -vector_[0][0] * p + vector_[0][1] * -q
        return abs(p * point[0] + q * point[1] + r) / math.sqrt(p * p + q * q)

    print(distance_to_segment(point, [v1, v2]))
    print(distance_to_segment(point, [v2, v3]))
    print(distance_to_segment(point, [v1, v3]))

    if distance_to_segment(point, [v1, v2]) <= 0.01 or distance_to_segment(point,
                                                                          [v2, v3]) <= 0.01 or distance_to_segment(point,
                                                                                                                  [v1,
                                                                                                                   v3]) <= 0.01:
        return True
    return False


def point_vs_triangle(point, triangle):
    v1 = triangle[0]
    v2 = triangle[1]
    v3 = triangle[2]
    if round((v3[0] - v1[0]) / (v2[0] - v1[0]), 6) == round((v3[1] - v1[1]) / (v2[1] - v1[1]), 6):
        raise Exception('ex')
    check1 = point_vs_vector(point, [v1, v2])
    check2 = point_vs_vector(point, [v2, v3])
    check3 = point_vs_vector(point, [v3, v1])
    print(check1, check2, check3)
    if check1 == check2 == check3:
        if check_distance(point, triangle):
            return 0
        return 1
    if (check1 or check2 or check3 == 0) and check1 + check2 + check3 == 2:
        return 0
    if check_distance(point, triangle) and (check1 and check2 and check3 != 0):
        return 0
    return -1


if __name__ == '__main__':
    # G = networkx.Graph()
    # G.add_node('1')
    # G.add_node('2')
    # G.add_node('3')
    # G.add_node('4')
    # G.add_node('5')
    # G.add_edges_from([('1', '2'), ('2', '3'), ('3', '1'), ('5', '2'), ('2', '4')])
    # networkx.draw(G=G)
    # plt.show()
    # print(point_vs_vector([0, 1], [[0, 0], [1, 1]]))
    print(point_vs_triangle([15.1, -3.9], [[25, 3], [-74, -66], [41, -36]]))
