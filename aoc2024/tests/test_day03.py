from aoc2024.day03 import get_uncorrupted_muls, summarize_muls


def test_get_uncorrupted_muls() -> None:
    example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    muls = get_uncorrupted_muls(example)
    assert muls == [(2, 4), (5, 5), (11, 8), (8, 5)]

    example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    muls = get_uncorrupted_muls(example, True)
    assert muls == [(2, 4), (8, 5)]


def test_summarize_muls() -> None:
    result = summarize_muls([(2, 4), (5, 5), (11, 8), (8, 5)])
    assert result == 161
