"""Template for tests for the COMP1730/6730 assignment.

Co-authors: u6826541, u6833622, u6832190
"""

from sys import argv

import pytest

from assignment import *


# Question 1.
def test_cells_above_height():
    test_map = [
        [0, 1, 0],
        [1, 0.5, 0],
        [0, 0, 0]]
    assert cells_above_height(test_map, 0.5) == 2


def test_area_above_water():
    test_map = [[556, 557, 800],
                [559, 560, 555],
                [554, 553, 555]]
    assert area_above_water(test_map, 557) == 0.000003


# Question 2.
def test_highest_point():
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 20], [2, 3, 10], [3, 4, 10]]]
    correct = ((1, 1), (0, 0), (2, 2), (2, 0))
    for i in range(len(test_maps)):
        assert highest_point(test_maps[i]) == correct[i]
    assert highest_point([[-2, -1, -10], [-2, -3, -10], [-3, -4, -10]]) == (1, 0)


# Question 3.
def test_slope_initial():
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [3.605551275463989, 3.605551275463989, 3.605551275463989, 8.54400374531753]
    for i in range(len(test_maps)):
        assert abs(slope(test_maps[i], 1, 1) - correct[i]) < 1e-6


def test_slope_student():
    # left side edge-cases for slope
    test_maps = [
            [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
            [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
            [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [   [0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [16.278820596099706,7.280109889280518,3.605551275463989,3.605551275463989]
    for i in range(len(test_maps)):
        assert abs(slope(test_maps[i], 0, 1) - correct[i]) < 1e-6
    assert abs(slope(test_maps[3], 0, 0) - 4.47213595499958) < 1e-6
    assert abs(slope(test_maps[3], 2, 0) - 18.0) < 1e-6
    assert abs(slope(test_maps[3], 0, 2) - 2.8284271247461903) < 1e-6
    assert abs(slope(test_maps[3], 2, 2) - 12.0) < 1e-6
    # up side edge-cases for slope
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [18.110770276274835,8.94427190999916,4.47213595499958,10.770329614269007]
    for i in range(len(test_maps)):
        assert abs(slope(test_maps[i], 1, 0) - correct[i]) < 1e-6
    # bottom side edge-cases for slope
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [12.165525060596439,2.8284271247461903,7.280109889280518,7.280109889280518]
    for i in range(len(test_maps)):
        assert abs(slope(test_maps[i], 1, 2) - correct[i]) < 1e-6
    # right side edge-cases for slope
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [13.416407864998739,6.324555320336759,16.1245154965971,14.0]
    for i in range(len(test_maps)):
        assert abs(slope(test_maps[i], 2, 1) - correct[i]) < 1e-6
def test_aspect_initial():
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [0.982793723247329, 0.982793723247329, 0.982793723247329, 0.35877067027057225]
    for i in range(len(test_maps)):
        assert abs(aspect(test_maps[i], 1, 1) - correct[i]) < 1e-6
    # up side edge-cases for slope
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [1.460139105621001,2.677945044588987,1.1071487177940904,0.3805063771123649]
    for i in range(len(test_maps)):
        assert abs(aspect(test_maps[i], 1, 0) - correct[i]) < 1e-6
    # bottom side edge-cases for slope
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [-1.4056476493802699,0.7853981633974483,0.27829965900511133,0.27829965900511133]
    for i in range(len(test_maps)):
        assert abs(aspect(test_maps[i], 1, 2) - correct[i]) < 1e-6
    # right side edge-cases for slope
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [2.677945044588987,1.2490457723982544,1.446441332248135,0.0]
    for i in range(len(test_maps)):
        assert abs(aspect(test_maps[i], 2, 1) - correct[i]) < 1e-6


def test_aspect_student():
    # left side edge cases
    test_maps = [
        [[0, 1, 2], [2, 10, 4], [3, 4, 5]],
        [[10, 1, 2], [2, 3, 4], [3, 4, 5]],
        [[0, 1, 2], [2, 3, 4], [3, 4, 10]],
        [[0, 1, 10], [2, 3, 10], [3, 4, 10]]]
    correct = [0.18534794999569476, -1.2924966677897853, 0.982793723247329, 0.982793723247329]
    for i in range(len(test_maps)):
        assert abs(aspect(test_maps[i], 0, 1) - correct[i]) < 1e-6
    assert abs(aspect(test_maps[3], 0, 0) - 1.1071487177940904) < 1e-6
    assert abs(aspect(test_maps[3], 2, 0) - 0.0) < 1e-6
    assert abs(aspect(test_maps[3], 0, 2) - 0.7853981633974483) < 1e-6
    assert abs(aspect(test_maps[3], 2, 2) - 0.0) < 1e-6

# Question 4
def test_path_initial():
    test_map = (
        (10, 10, 10, 10, 10),
        (10, 8,  7,  6, 10),
        (10, 10, 10, 5, 10),
        (10, 8,  7,  3, 10),
        (10, 10, 10, 10, 10)
    )

    assert find_path(test_map, 1, 1, 0) == [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)] or find_path(test_map, 1, 1, 0) == [(1, 1), (2, 1), (3, 2), (3, 3)]
    assert find_path(test_map, 1, 3, 0) == [(1, 3), (2, 3), (3, 3)]
    assert find_path(test_map, 3, 3, 0) == [(3, 3), ]


def test_path_student():
    # Write your additional tests for the find path function here
    test_map = (
        (10, 10,  5, 10, 10),
        (10,  8, 10,  6,  9),
        (10, 10,  7, 10, 10),
        (10, 10, 10,  8, 10),
        (10, 10, 10, 10, 10))
    test_map2 = (
        (5, 10,  5, 10, 10),
        (4, 10, 10,  6,  9),
        (2,  1,  10, 10, 10),
        (10, 10, 10,  8, 10),
        (10, 10, 10, 10, 10))
    assert find_path(test_map, 1, 1, 0) == [(1,1), (2,0)]
    test_graph = (((10, 10, 10),(10, 10, 10),(10, 10, 11)),
                  ((10, 10,7.5, 10, 10),(10,  8, 10,  7, 6),(10, 10, 10, 10, 10),(10, 10, 10, 10, 10),(10, 10, 10, 10, 10)),
                  ((10, 10, 10, 10, 10),(10,  8, 10, 10,  9),(10, 10,  7, 10, 10),(10, 10, 10,  6,  5),(10, 10, 10,  5,  5)),
                  ((10, 10, 10, 10, 10),(10,  8, 10, 10,  5),(10, 10,  7,  6, 10),(10, 10,  6, 10, 10),( 3,  4, 10, 10, 10)),
                  ((10, 10, 10, 10,  3),(10,  8, 10, 10,  4),(10, 10,  7,  6, 10),(10, 10,  6, 10, 10),(10,  5, 10, 10, 10)),
                  ((10, 10, 10, 10,  10, 5.8,5.7),(10,  8, 10, 10, 5.9,  10, 10),(10, 10,  7,  6,  10,  10, 10),(10, 10,  6,  6,  10,  10, 10),(10,  5, 10, 10, 5.6,  10, 10),( 3, 10, 10, 10,  10, 5.1, 10),(10,0.5, 10, 10,  10,  10,  1),),
                  ((10, 10,  8, 7.9,7.8, 5.9,5.7),(10,  9, 10, 10, 5.9,  10, 10),(10, 10,  8, 10,   4,  10, 10),(10, 10,  7, 10,  10,   3, 0.0001),( 2, 10,  6, 10,  10,  10, 10),(10,  5, 10,  5,  10,  10, 10),(10, 10, 10, 10,   4,   3, 0.00009),))

    test_answer = ([(1, 1)],
                   [(1, 1), (2, 0), (3, 1), (4, 1)],
                   [(1, 1), (2, 2), (3, 3), (4, 3)],
                   [(1, 1), (2, 2), (2, 3), (1, 4), (0, 4)],
                   [(1, 1), (2, 2), (3, 2), (4, 1), (4, 0)],
                   [(1, 1), (2, 2), (2, 3), (1, 4), (0, 5), (1, 6)],
                   [(1, 1), (2, 2), (2, 3), (2, 4), (3, 5), (4, 6), (5, 6), (6, 6)])

    for i in range(len(test_graph)):
        assert find_path(test_graph[i],1,1,0) == test_answer[i] 
        
    test_map3 = ((10, 10, 10, 10,  10, 5.8,1.1),
                 (10,  8, 10, 10, 5.9,  10, 10),
                 (10, 10,  7,  6,  10,  10, 10),
                 (10, 10,  6,  6,  10,  10, 10),
                 (10,  5, 10, 10, 5.6,  10, 10),
                 ( 3, 10, 10, 10,  10, 5.1, 10),
                 (10,0.5, 10, 10,  10,  10,  2),)
    assert find_path(test_map3,1,1,3) == [(1, 1), (2, 2), (2, 3), (1, 4), (0, 5)]
    assert find_path(test_map3,1,1,2.2) == [(1, 1), (2, 2), (2, 3), (1, 4), (0, 5)]
    assert find_path(test_map3,1,1,1) == [(1, 1), (2, 2), (3, 2), (4, 1), (5, 0), (6, 0)]

    

# Question 5

def test_find_buildings():
    # Write your tests for question 5 here
    test_case=( [[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[0,0,1,0,0]] ,
                [[0,0,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0]],
                [[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,0,0]], 
                [[0,0,1,0],[1,1,1,0],[0,0,1,0],[0,0,0,0]],
                [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
                [[1,1,0,0,0],[1,0,1,0,0],[0,1,1,1,0],[0,0,1,0,1],[0,0,0,1,1]])
    answer = ([{(1,0)},{(3,0)},{(2,1)},{(1,2)},{(3,2)},{(2,3)}],
              [{(1,1),(1,2),(2,2),(2,3),(3,3)}],
              [{(1, 0),(1, 1),(1, 2),(2, 0),(2, 2),(3, 0), (3, 1), (3, 2)}], 
              [{(0, 1), (1, 1), (2, 0), (2, 1), (2, 2)}],
              [], 
              [{(0, 0), (0, 1), (1, 0)},{(1, 2), (2, 1), (2, 2), (2, 3), (3, 2)},{(3, 4), (4, 3), (4, 4)}])
    a_map=[[0,1,0,1,0,0],
           [0,0,1,0,0,0],
           [0,1,0,1,0,0],
           [0,0,1,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]   
    assert near_four(0,0,a_map) == [(1,0),(0,1)]
    assert near_four(0,5,a_map) == [(0,4),(1,5)]
    assert near_four(5,0,a_map) == [(4,0),(5,1)]
    assert near_four(5,5,a_map) == [(5,4),(4,5)]
    assert near_four(0,2,a_map) == [(0,1),(1,2),(0,3)]
    assert near_four(2,0,a_map) == [(1,0),(2,1),(3,0)]
    assert near_four(5,2,a_map) == [(5,1),(4,2),(5,3)]
    assert near_four(2,5,a_map) == [(1,5),(2,4),(3,5)]
    assert near_four(2,2,a_map) == [(2,1),(1,2),(2,3),(3,2)]
    for i in range(len(test_case)):
        assert find_buildings(test_case[i]) == answer[i]
# Question 6
def test_line_of_sight():
    # Write your tests for the line of sight function here
    test_map = (( 1, 2, 3, 4, 5,21), 
                ( 6, 7, 8, 9,10,21),
                (11,12,13,14,15,23),
                (16,17,18,19,20,24),
                (25,26,27,28,29,30))
    assert line_of_sight(test_map,test_map,0,0,4,4) == [14, 26, 38]
    assert line_of_sight(test_map,test_map,0,0,3,3) == [14, 26]
    assert line_of_sight(test_map,test_map,0,0,5,2) == [14, 16, 18, 20]
    assert line_of_sight(test_map,test_map,0,0,2,1) == [4, 14]

    assert line_of_sight(test_map,test_map,0,0,3,1) == [4, 16]
    assert line_of_sight(test_map,test_map,3,1,0,0) == [16, 4]
# slope is greater than 0
    assert line_of_sight(test_map,test_map,0,1,3,0) == [14, 6]
    assert line_of_sight(test_map,test_map,3,0,0,1) == [6, 14]
# slope is smaller than 0
    assert line_of_sight(test_map,test_map,0,0,5,0) == [4, 6, 8, 10]
    assert line_of_sight(test_map,test_map,0,0,0,4) == [12, 22, 32]
    assert line_of_sight(test_map,test_map,0,0,1,1) == []
    assert line_of_sight(test_map,test_map,3,0,3,0) == []


def test_is_hiaf_visible():
    # Write your tests for the is_hiaf_visible function here
    test_map = (( 8, 14, 20, 26, 32),
                (10,8.5, 10, 10,  9),
                (10, 10,  9, 10, 10),
                (10, 10, 10,9.5,  5),
                (10, 10, 10,  5, 10))
    assert is_hiaf_visible(test_map,test_map,0,0,4,0) == True
    assert is_hiaf_visible(test_map,test_map,0,0,4,4) == True
    test_map2 = (( 8, 14, 20,26.1, 32),
                 (10,8.5, 10, 10,  9),
                 (10, 10,9.1, 10, 10),
                 (10, 10, 10,9.5,  5),
                 (10, 10, 10,  5, 10))
    assert is_hiaf_visible(test_map2,test_map2,0,0,4,0) == False
    assert is_hiaf_visible(test_map2,test_map2,0,0,4,4) == False
    test_map3 = (( 1,  2,   3,   4,   5,21), 
                 ( 6,5.6,10.2,   9,  10,21),
                 (11, 12,  13,14.8,19.4,23),
                 (16,  2,   2,   3,   7,24),)
    assert is_hiaf_visible(test_map3,test_map3,0,0,5,3) == True
    assert is_hiaf_visible(test_map3,test_map3,0,3,5,3) == True
    


if __name__ == '__main__':
    pytest.main(argv)
