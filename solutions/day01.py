from aocd.models import Puzzle
from collections import Counter


def load_data(input_data):
    left_list, right_list = [], []
    for line in input_data.splitlines():
        l, r = line.split()
        left_list.append(int(l))
        right_list.append(int(r))
    return left_list, right_list


def solve_puzzle_a(left_list, right_list):
    total_distance = 0

    for l, r in zip(sorted(left_list), sorted(right_list)):
        total_distance += abs(l - r)

    return total_distance


def solve_puzzle_b(left_list, right_list):
    similarity_score = 0

    value_count = Counter(right_list)
    for num in left_list:
        similarity_score += (num * value_count[num])
    return similarity_score


if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=1)
    left_list, right_list = load_data(puzzle.input_data)

    # solve and submit puzzle a
    answer_a = solve_puzzle_a(left_list, right_list)
    print("Total Distance: ", answer_a)
    puzzle.answer_a = answer_a

    # solve and submit puzzle b
    answer_b = solve_puzzle_b(left_list, right_list)
    print("Similarity Score: ", answer_b)
    puzzle.answer_b = answer_b
