from aocd.models import Puzzle
import re


def solve_puzzle_a(memory):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
    multipliers = [list(map(int, re.findall(r"\d{1,3}", x))) for x in matches]
    final_sum = sum([x * y for [x, y] in multipliers])
    return final_sum


def solve_puzzle_b(memory):
    dont_split = memory.split("don't()")
    do_multiply = ""
    if puzzle.input_data.find("don't") != 0:
        do_multiply = do_multiply + dont_split.pop(0)

    do_multiply = do_multiply + "".join([x[x.find("do()") + 4:] for x in dont_split if x.find("do()") != -1])
    final_sum = solve_puzzle_a(do_multiply)

    return final_sum


if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=3)
    memory = puzzle.input_data

    # solve and submit puzzle a
    answer_a = solve_puzzle_a(memory)
    print(f"Sum of valid multiplications: {answer_a}")
    puzzle.answer_a = answer_a

    # solve and submit puzzle b
    answer_b = solve_puzzle_b(memory)
    print("Sum of valid multiplications: ", answer_b)
    puzzle.answer_b = answer_b
