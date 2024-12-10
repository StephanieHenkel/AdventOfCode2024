from aocd.models import Puzzle


def load_data(input_data):
    unusual_data = []
    for report in input_data.splitlines():
        unusual_data.append(list(map(int, report.split())))
    return unusual_data


def solve_puzzle_a(unusual_data):
    safe_reports = 0

    for report in unusual_data:
        cur_lvl_change = 0
        old_lvl = report[0]
        safe = True
        for cur_lvl in report[1:]:
            if abs(old_lvl - cur_lvl) > 3 or cur_lvl == old_lvl:
                safe = False
                break
            elif cur_lvl > old_lvl:
                if (cur_lvl_change * 1) == -1:
                    safe = False
                    break
                else:
                    cur_lvl_change = 1
            else:
                if (cur_lvl_change * -1) == -1:
                    safe = False
                    break
                else:
                    cur_lvl_change = -1
            old_lvl = cur_lvl
        if safe:
            safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    # get data
    puzzle = Puzzle(year=2024, day=2)
    unusual_data = load_data(puzzle.input_data)

    # solve and submit puzzle a
    answer_a = solve_puzzle_a(unusual_data)
    print(f"Number of Safe Reports: {answer_a}/{len(unusual_data)}")
    puzzle.answer_a = answer_a
