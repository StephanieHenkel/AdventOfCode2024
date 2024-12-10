from aocd.models import Puzzle
import re


def load_data(input_data):
    return input_data.splitlines()


def solve_puzzle_a(words):
    xmas_count = 0
    xmas_count += sum(len(re.findall("XMAS", x)) for x in words) # left to right
    xmas_count += sum(len(re.findall("XMAS", x[::-1])) for x in words) # right to left

    up_down_words = ["".join(row) for row in list(zip(*words))]
    xmas_count += sum(len(re.findall("XMAS", x)) for x in up_down_words)  # up to down
    xmas_count += sum(len(re.findall("XMAS", x[::-1])) for x in up_down_words) # down to up

    to_right_diag_words = get_to_right_diag(words)
    xmas_count += sum(len(re.findall("XMAS", x)) for x in to_right_diag_words)  # up to down
    xmas_count += sum(len(re.findall("XMAS", x[::-1])) for x in to_right_diag_words)  # down to up

    to_left_diag_words = get_to_right_diag([word[::-1] for word in words])
    xmas_count += sum(len(re.findall("XMAS", x)) for x in to_left_diag_words)  # up to down
    xmas_count += sum(len(re.findall("XMAS", x[::-1])) for x in to_left_diag_words)  # down to up
    return xmas_count


def get_to_right_diag(words):
    diagonal_words = []
    for col in range(len(words[0]) - 4 + 1):
        i = 0
        j = col
        new_row = ""

        while j < len(words[0]) and i < len(words):
            new_row = new_row + words[i][j]
            i += 1
            j += 1
        diagonal_words.append(new_row)

    for row in range(1, len(words) - 4 + 1):
        i = row
        j = 0
        new_row = ""

        while j < len(words[0]) and i < len(words):
            new_row = new_row + words[i][j]
            i += 1
            j += 1
        diagonal_words.append(new_row)

    return diagonal_words

def solve_puzzle_b(left_list, right_list):
    # TBD
    return


def print_words(words):
    for line in words:
        print(line)

if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=4)
    words = load_data(puzzle.input_data)

    # solve and submit puzzle a
    answer_a = solve_puzzle_a(words)
    print("XMAS count: ", answer_a)
    puzzle.answer_a = answer_a

    # solve and submit puzzle b
    # answer_b = solve_puzzle_b(tbd)
    # print("TBD: ", answer_b)
    # puzzle.answer_b = answer_b
