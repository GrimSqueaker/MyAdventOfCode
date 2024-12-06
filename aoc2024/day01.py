from functools import reduce
from operator import add
from pathlib import Path
from textwrap import dedent


def compute_total_distance(list1: list, list2: list) -> int:
    # sort the lists and compute pairwise difference
    # sums = map(lambda x, y: max(x, y) - min(x, y), sorted(list1), sorted(list2))
    sums = [max(x, y) - min(x, y) for (x, y) in zip(sorted(list1), sorted(list2))]

    # return the sum of the distance
    return reduce(add, sums, 0)


def compute_similiarity_score(list1: list, list2: list) -> int:
    # compute histogram of list2
    max_hist = max([*list1, *list2])
    histogram = [0] * (max_hist + 1)
    for i in list2:
        histogram[i] = histogram[i] + 1

    similiarity = [x * histogram[x] for x in list1]
    return reduce(add, similiarity, 0)


def load_txt_file(filename: str) -> str:
    return Path(filename).read_text(encoding="UTF-8")


def read_lists_from_string(file_contents: str) -> tuple[list, list]:
    # load input from file and split into lists
    list1 = []
    list2 = []
    for line in file_contents.splitlines():
        numbers = [int(x) for x in line.split()]
        list1.append(numbers[0])
        list2.append(numbers[1])

    return (list1, list2)


def main() -> None:
    # example
    example = dedent(
        """\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3"""
    )
    list1, list2 = read_lists_from_string(example)

    total_distance_example = compute_total_distance(list1, list2)
    print(f"{total_distance_example=}")
    similarity_example = compute_similiarity_score(list1, list2)
    print(f"{similarity_example=}")

    # real data
    real_data = load_txt_file("2024/day01_input.txt")
    list1, list2 = read_lists_from_string(real_data)
    total_distance_real_data = compute_total_distance(list1, list2)
    print(f"{total_distance_real_data=}")
    similarity_real_data = compute_similiarity_score(list1, list2)
    print(f"{similarity_real_data=}")


if __name__ == "__main__":
    main()
