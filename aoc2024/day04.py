from pathlib import Path


def get_letter_at_position(lines: list[str], row: int, col: int) -> str:
    rows = len(lines)
    cols = len(lines[0])

    if 0 <= row < rows and 0 <= col < cols:
        return lines[row][col]

    return ""


def find_xmas(text: str) -> int:
    # find the word "XMAS" in the text: horizontal, vertical, or diagonal and backwards
    count = 0
    matrix = text.splitlines()
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

    for r in range(rows):
        for c in range(cols):
            # look in all 8 directions
            for d in directions:
                word = ""
                for i in range(4):
                    word = word + get_letter_at_position(matrix, r + i * d[0], c + i * d[1])

                if word == "XMAS":
                    print(f"{r=} {c=} {d=}")
                    count += 1

    return count


def find_cross_mas(text: str) -> int:
    # find the word "MAS" in the text in the shape of an X - even backwards
    count = 0
    matrix = text.splitlines()
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            if get_letter_at_position(matrix, r, c) == "A":
                diag = "".join(
                    [get_letter_at_position(matrix, r + 1, c + 1), get_letter_at_position(matrix, r - 1, c - 1)]
                )
                anti_diag = "".join(
                    [get_letter_at_position(matrix, r + 1, c - 1), get_letter_at_position(matrix, r - 1, c + 1)]
                )

                print(f"check {r=} {c=} {diag=} {anti_diag=}")

                if all(d in ("MS", "SM") for d in (diag, anti_diag)):
                    print(f"{r=} {c=}")
                    count += 1

    return count


def load_txt_file(filename: str) -> str:
    return Path(filename).read_text(encoding="UTF-8")


def main() -> None:
    data = load_txt_file("aoc2024/day04_input.txt")

    # part 1
    count_xmas = find_xmas(data)
    print(f"{count_xmas=}")

    # part 2
    count_cross_mas = find_cross_mas(data)
    print(f"{count_cross_mas=}")


if __name__ == "__main__":
    main()
