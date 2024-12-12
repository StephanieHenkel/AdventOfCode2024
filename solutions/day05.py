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


def solve_puzzle_b(tbd):

    return


if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=5)
    # sample = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47\n"
    ordering_dict, updates = load_data(puzzle.input_data)

    # solve and submit puzzle a
    answer_a = solve_puzzle_a(ordering_dict, updates)
    print("Sum of middle number of valid updates: ", answer_a)
    puzzle.answer_a = answer_a

    # # solve and submit puzzle b
    # answer_b = solve_puzzle_b(tbd)
    # print("tbd: ", answer_b)
    # puzzle.answer_b = answer_b
