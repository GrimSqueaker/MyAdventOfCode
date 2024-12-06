from pathlib import Path
from textwrap import dedent


def get_number_of_safe_reports(reports: list, dampen: bool = False) -> int:
    # a report is safe if all levels are either increasing or decreasing and the distance between the levels is 1 to 3
    safe_reports = 0
    for report in reports:
        if is_safe_report(report):
            safe_reports = safe_reports + 1
        elif dampen:
            dampened_reports = [report[:i] + report[i + 1 :] for i in range(len(report))]
            if any(is_safe_report(dampened_report) for dampened_report in dampened_reports):
                safe_reports = safe_reports + 1

    return safe_reports


def is_safe_report(levels: list) -> bool:
    # a report is safe if all levels are either increasing or decreasing and the distance between the levels is 1 to 3
    differences = [x - y for (x, y) in zip(levels[1:], levels[:-1])]
    all_positive = all(1 <= d <= 3 for d in differences)
    all_negative = all(-3 <= d <= -1 for d in differences)
    if all_negative or all_positive:
        return True

    return False


def load_txt_file(filename: str) -> str:
    return Path(filename).read_text(encoding="UTF-8")


def read_reports_from_string(file_contents: str) -> list:
    # every line consists of numbers called levels, a line is called a report
    reports = []
    for line in file_contents.splitlines():
        levels = [int(x) for x in line.split()]
        reports.append(levels)

    return reports


def main() -> None:
    # example
    example = dedent(
        """\
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9"""
    )
    list1 = read_reports_from_string(example)

    safe_reports_example = get_number_of_safe_reports(list1)
    print(f"{safe_reports_example=}")
    dampened_example = get_number_of_safe_reports(list1, dampen=True)
    print(f"{dampened_example=}")

    # real data
    real_data = load_txt_file("2024/day02_input.txt")
    reports = read_reports_from_string(real_data)
    safe_reports_real_data = get_number_of_safe_reports(reports)
    print(f"{safe_reports_real_data=}")
    safe_dampened_reports_real_data = get_number_of_safe_reports(reports, True)
    print(f"{safe_dampened_reports_real_data=}")


if __name__ == "__main__":
    main()
