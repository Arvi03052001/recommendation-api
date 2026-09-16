# ============================================
# Three tests. That's all.
#
# Run:   python tests/test_core.py
#
# A "test" just calls your function and checks the answer.
# Nothing magic. You could write these yourself.
# ============================================

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import filter_by_year
from data.movies import MOVIES


def test_1_finds_movies_from_2017():
    # there are 2 movies from 2017: Get Out and Coco
    result = filter_by_year(MOVIES, 2017)
    assert len(result) == 2


def test_2_gives_back_whole_movies_not_titles():
    # each item should be a dictionary, not just a title string
    result = filter_by_year(MOVIES, 2017)
    assert isinstance(result[0], dict)


def test_3_empty_when_no_movies_that_year():
    # no movies from 1850
    result = filter_by_year(MOVIES, 1850)
    assert result == []


# ============================================
if __name__ == "__main__":
    tests = [
        ("test 1  finds movies from 2017", test_1_finds_movies_from_2017),
        ("test 2  gives back whole movies", test_2_gives_back_whole_movies_not_titles),
        ("test 3  empty list when none found", test_3_empty_when_no_movies_that_year),
    ]

    passed = 0
    print()
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS   {name}")
            passed += 1
        except AssertionError:
            print(f"  FAIL   {name}")
        except Exception as e:
            print(f"  ERROR  {name}")
            print(f"         -> {type(e).__name__}: {e}")

    print()
    print(f"  {passed} out of 3 passing")
    if passed == 3:
        print("  All green. Nice work.")
    print()
