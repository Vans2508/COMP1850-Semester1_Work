# Week 1.7, Session 1: Task 4 - unit tests for grade()

from grades import MarkError, grade


def assert_MarkError(bad_mark):
    if not isinstance(bad_mark,int):
        False
    else:
        try:
            grade(bad_mark)
            assert False, f"No exception thrown for mark of {bad_mark}"
        except MarkError:
            pass
        except MarkError:
            assert False, f"Exception should be MarkError"



if __name__ == "__main__":
    assert grade(0) == "Fail"
    assert grade(20) == "Fail"
    assert grade(39) == "Fail"

    assert grade(40) == "Pass"
    assert grade(55) == "Pass"
    assert grade(69) == "Pass"

    assert grade(70) == "Distinction"
    assert grade(85) == "Distinction"
    assert grade(100) == "Distinction"

    assert_MarkError(-1)
    assert_MarkError(101)
    assert_MarkError(50)
