from aocd.models import Puzzle
from collections import defaultdict


def load_data(input_data):
    ordering_str, updates_str = input_data.split("\n\n")
    ordering_dict = defaultdict(list)
    for order in ordering_str.splitlines():
        first, second = list(map(int, order.split("|")))
        ordering_dict[first].append(second)

    updates = [list(map(int, u.split(","))) for u in updates_str.splitlines()]
    return ordering_dict, updates


def solve_puzzle_a(ordering_dict, updates):
    valid_middle_p_nr_total = 0
    # check if ordering of update is valid
    for update in updates:
        seen = set()
        valid = True
        for page in update:
            # check if any of the pages that should only come afterwards had been seen before
            if any([after_p in seen for after_p in ordering_dict[page]]):
                valid = False
                break
            seen.add(page)

        # if yes, then get middle page number and add it
        if valid:
            valid_middle_p_nr_total += update[len(update) // 2]

    return valid_middle_p_nr_total


def solve_puzzle_b(ordering_dict, updates):
    valid_middle_p_nr_total = 0
    # check if ordering of update is valid
    for update in updates:
        seen = []
        valid = True
        for page in update:
            added = False
            # check if any of the pages that should only come afterwards had been seen before
            for after_p in ordering_dict[page]:
                if after_p in seen:
                    valid = False
                    added = True
                    if page in seen:
                        if seen.index(page) > seen.index(after_p):
                            seen.pop(seen.index(page))
                            seen.insert(seen.index(after_p), page)
                    else:
                        seen.insert(seen.index(after_p), page)
            if not added:
                seen.append(page)

        # if yes, then get middle page number and add it
        if not valid:
            valid_middle_p_nr_total += seen[len(seen) // 2]

    return valid_middle_p_nr_total


if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=5)
    ordering_dict, updates = load_data(puzzle.input_data)

    # solve and submit puzzle a
    answer_a = solve_puzzle_a(ordering_dict, updates)
    print("Sum of middle number of valid updates: ", answer_a)
    puzzle.answer_a = answer_a

    # solve and submit puzzle b
    answer_b = solve_puzzle_b(ordering_dict, updates)
    print("Sum of middle number of new valid updates: ", answer_b)
    puzzle.answer_b = answer_b
