from textwrap import dedent

from aoc2024.day04 import find_cross_mas, find_xmas, get_letter_at_position

EXAMPLE = dedent(
    """\
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX"""
)


def test_get_letter_at_position() -> None:
    example = dedent(
        """\
        MMMS
        MSAM
        AMXS
        MASX"""
    ).splitlines()
    assert get_letter_at_position(example, 0, 0) == "M"
    assert get_letter_at_position(example, 2, 0) == "A"
    assert get_letter_at_position(example, 4, 0) == ""
    assert get_letter_at_position(example, 3, 4) == ""
    assert get_letter_at_position(example, 3, 3) == "X"
    assert get_letter_at_position(example, -1, -1) == ""


def test_find_xmas() -> None:
    count = find_xmas(EXAMPLE)
    assert count == 18


def test_find_cross_mas() -> None:
    count = find_cross_mas(EXAMPLE)
    assert count == 9
