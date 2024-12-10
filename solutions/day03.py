from aocd.models import Puzzle
import re


def load_data(input_data):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input_data)
    multipliers = [list(map(int, re.findall(r"\d{1,3}", x))) for x in matches]
    return multipliers


def solve_puzzle_a(multipliers):
    final_sum = sum([x * y for [x, y] in multipliers])
    return final_sum


def solve_puzzle_b(memory):
    # tbd
    return


if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=3)
    multipliers = load_data(puzzle.input_data)

    # solve and submit puzzle a
    answer_a = solve_puzzle_a(multipliers)
    print(f"Sum of valid multiplication: {answer_a}")
    puzzle.answer_a = answer_a

    # solve and submit puzzle b
    answer_b = solve_puzzle_b(multipliers)
    print("TBD: ", answer_b)
    # puzzle.answer_b = answer_b
