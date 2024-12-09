from aocd.models import Puzzle


def load_data(input_data):
    list_1, list_2 = [], []
    for line in input_data.splitlines():
        l, r = line.split()
        list_1.append(int(l))
        list_2.append(int(r))
    return list_1, list_2


def solve_puzzle_a(data):
    total_distance = 0
    left_list = sorted(data[0])
    right_list = sorted(data[1])
    for l, r in zip(left_list, right_list):
        total_distance += abs(l - r)

    return total_distance


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=1)
    data = load_data(puzzle.input_data)
    answer_a = solve_puzzle_a(data)
    print(answer_a)
    puzzle.answer_a = answer_a
