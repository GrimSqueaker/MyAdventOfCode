import re
from pathlib import Path


def get_uncorrupted_muls(data: str, use_conditionals: bool = False) -> list[tuple[int, int]]:
    regex = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")
    muls = []
    enabled = True
    while match := regex.search(data):
        if use_conditionals and match.group(0).startswith("don"):
            enabled = False
        elif use_conditionals and match.group(0).startswith("do"):
            enabled = True
        elif enabled and match.group(0).startswith("mul"):
            muls.append((int(match.group(1)), int(match.group(2))))
        data = data[match.end() :]
    return muls


def summarize_muls(muls: list[tuple[int, int]]) -> int:
    return sum(m[0] * m[1] for m in muls)


def load_txt_file(filename: str) -> str:
    return Path(filename).read_text(encoding="UTF-8")


def main() -> None:
    data = load_txt_file("AOC2024/day03_input.txt")

    # part 1
    muls = get_uncorrupted_muls(data)
    sum_without_conditionals = summarize_muls(muls)
    print(f"{sum_without_conditionals=}")

    # part 2
    muls = get_uncorrupted_muls(data, True)
    sum_with_conditionals = summarize_muls(muls)
    print(f"{sum_with_conditionals=}")


if __name__ == "__main__":
    main()
