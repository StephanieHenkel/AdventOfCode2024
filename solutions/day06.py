from aocd.models import Puzzle
from collections import defaultdict


def load_data(input_data):
    return input_data.splitlines()


def inside_map(map, i, j):
    return 0 <= i < len(map) and 0 <= j < len(map[0])


def move(i, j, cur_dir):
    directions = {
        "up": [-1, 0],
        "down": [+1, 0],
        "right": [0, +1],
        "left": [0, -1]
    }
    di, dj = directions[cur_dir]
    return i+di, j+dj


def view_walk(map, i, j):
    for m in range(len(map)):
        if m != i:
            print(map[m])
        else:
            map[i] = map[i][:j] + "X" + map[i][j+1: ]
            print(map[i])

    print("\n")
    return map


def solve_puzzle_a(map):
    positions = defaultdict(set)
    next_direction = {"up": "right", "down": "left", "right": "down", "left": "up"}

    # find starting position
    for l in range(len(map)):
        if "^" in map[l]:
            i = l
            j = map[l].index("^")
            break

    cur_dir = "up"
    i_new, j_new = i, j
    while inside_map(map, i_new, j_new):
        # check for obstruction
        if map[i_new][j_new] == "#":
            cur_dir = next_direction[cur_dir]
        else:
            # add pos to dict
            i, j = i_new, j_new
            # map = view_walk(map, i, j)
            positions[i].add(j)

        # move further in cur direction
        i_new, j_new = move(i, j, cur_dir)

    return sum([len(row_pos) for row_pos in positions.values()])


def solve_puzzle_b(tbd):

    return


if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=6)
    map = load_data(puzzle.input_data)

    # map = [
    #     "....#.....",
    #     ".........#",
    #     "..........",
    #     "..#.......",
    #     ".......#..",
    #     "..........",
    #     ".#..^.....",
    #     "........#.",
    #     "#.........",
    #     "......#...",
    # ]
    # solve and submit puzzle a
    answer_a = solve_puzzle_a(map)
    print("Number of dictinct guard positions", answer_a)
    puzzle.answer_a = answer_a

    # # solve and submit puzzle b
    # answer_b = solve_puzzle_b(tbd)
    # print("tbd", answer_b)
    # puzzle.answer_b = answer_b
