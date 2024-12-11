from aocd.models import Puzzle
import re


def load_data(input_data):
    return input_data.splitlines()


def solve_puzzle_a(words):
    total_count = 0

    for i in range(len(words[0])):
        for j in range(len(words)):
            if words[i][j] == "X":
                # go up
                total_count += move(words, i, j, match_word="XMAS", direction=go_up)
                # go down
                total_count += move(words, i, j, match_word="XMAS", direction=go_down)
                # go right
                total_count += move(words, i, j, match_word="XMAS", direction=go_right)
                # go left
                total_count += move(words, i, j, match_word="XMAS", direction=go_left)
                # go right down
                total_count += move(words, i, j, match_word="XMAS", direction=lambda i, j: go_right(*go_down(i, j)))
                # go right up
                total_count += move(words, i, j, match_word="XMAS", direction=lambda i, j: go_right(*go_up(i, j)))
                # go left down
                total_count += move(words, i, j, match_word="XMAS", direction=lambda i, j: go_left(*go_down(i, j)))
                # go left up
                total_count += move(words, i, j, match_word="XMAS", direction=lambda i, j: go_left(*go_up(i, j)))

    return total_count


def go_up(i, j):
    return i - 1, j


def go_down(i, j):
    return i + 1, j


def go_right(i, j):
    return i, j + 1


def go_left(i, j):
    return i, j - 1


def in_boundaries(words, i, j):
    return 0 <= j < len(words[0]) and 0 <= i < len(words)


def move(words, i, j, match_word="XMAS", direction=go_up):
    count = 1
    i, j = direction(i, j)

    while in_boundaries(words, i, j) and count < len(match_word):
        if words[i][j] != match_word[count]:
            return 0
        else:
            count += 1
            i, j = direction(i, j)

    if count == len(match_word):
        return 1
    else:
        return 0


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
