from aocd.models import Puzzle
from collections import Counter


def load_data(input_data):
    unusual_data = []
    for report in input_data.splitlines():
        unusual_data.append(list(map(int, report.split())))
    return unusual_data


def solve_puzzle_a(unusual_data):
    safe_reports = 0

    for report in unusual_data:

        if safety_check(report)[0]:
            safe_reports += 1

    return safe_reports


def safety_check(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    if all([diff in range(-3, 0) for diff in differences]) or all([diff in range(1, 4) for diff in differences]):
        return True, None
    else:
        return False, differences


def solve_puzzle_b(unusual_data):
    safe_reports = 0

    for report in unusual_data:
        safe, differences = safety_check(report)
        if safe:
            safe_reports += 1
        else:
            for i in range(len(report)):
                safe, differences = safety_check(report[:i] + report[i + 1: ])
                if safe:
                    safe_reports += 1
                    break


    return safe_reports


if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=2)
    unusual_data = load_data(puzzle.input_data)

    # solve and submit puzzle a
    answer_a = solve_puzzle_a(unusual_data)
    print(f"Number of Safe Reports: {answer_a}/{len(unusual_data)}")
    puzzle.answer_a = answer_a

    # solve and submit puzzle b
    answer_b = solve_puzzle_b(unusual_data)
    print(f"Number of Safe Reports: {answer_b}/{len(unusual_data)}")
    puzzle.answer_b = answer_b
