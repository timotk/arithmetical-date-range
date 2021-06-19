from datetime import datetime

from arithmetical_date_range import ArithmeticalDateRange


def test_subtract_other_end_is_greater():
    a = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 2, 1),
    )

    assert a - b == expected


def test_subtract_other_is_larger_than_complete_range():
    a = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 3, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    expected = None

    assert a - b == expected


def test_subtract_other_start_is_smaller():
    a = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )
    expected = ArithmeticalDateRange(
        start=datetime(2021, 3, 1),
        end=datetime(2021, 4, 1),
    )

    assert a - b == expected


def test_subtract_other_is_contained():
    a = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 3, 1),
    )

    expected = [
        ArithmeticalDateRange(
            start=datetime(2021, 1, 1),
            end=datetime(2021, 2, 1),
        ),
        ArithmeticalDateRange(
            start=datetime(2021, 3, 1),
            end=datetime(2021, 4, 1),
        ),
    ]

    result = a - b
    assert result[0] == expected[0]
    assert result[1] == expected[1]


def test_subtract_start_is_the_same():
    a = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )

    expected = ArithmeticalDateRange(
        start=datetime(2021, 3, 1), end=datetime(2021, 4, 1)
    )

    assert a - b == expected


def test_subtract_end_is_the_same():
    a = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )

    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 2, 1),
    )

    assert a - b == expected


def test_subtract_multiple_date_ranges():
    a = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 5, 1),
    )
    b1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )

    b2 = ArithmeticalDateRange(
        start=datetime(2021, 4, 1),
        end=datetime(2021, 6, 1),
    )

    expected = ArithmeticalDateRange(
        start=datetime(2021, 3, 1), end=datetime(2021, 4, 1)
    )

    assert a - [b1, b2] == expected


def test_add_other_end_is_greater():
    a = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )

    assert a + b == expected


def test_add_other_is_larger_than_complete_range():
    a = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 3, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )

    assert a + b == b


def test_add_other_start_is_smaller():
    a = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )
    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )

    assert a + b == expected


def test_add_other_is_contained():
    a = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 3, 1),
    )

    assert a + b == a


def test_add_start_is_the_same():
    a = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )

    assert a + b == a


def test_add_end_is_the_same():
    a = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    b = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )

    assert a + b == a


def test_add_multiple_date_ranges():
    a = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    b1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )

    b2 = ArithmeticalDateRange(
        start=datetime(2021, 4, 1),
        end=datetime(2021, 5, 1),
    )

    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1), end=datetime(2021, 5, 1)
    )

    assert a + [b1, b2] == expected
