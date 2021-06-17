from datetime import datetime

from arithmetical_date_range import ArithmeticalDateRange


def test_subtract_other_end_is_greater():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 2, 1),
    )

    assert m1 - m2 == expected


def test_subtract_other_is_larger_than_complete_range():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 3, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    expected = None

    assert m1 - m2 == expected


def test_subtract_other_start_is_smaller():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )
    expected = ArithmeticalDateRange(
        start=datetime(2021, 3, 1),
        end=datetime(2021, 4, 1),
    )

    assert m1 - m2 == expected


def test_subtract_other_is_contained():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    m2 = ArithmeticalDateRange(
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

    result = m1 - m2
    assert result[0] == expected[0]
    assert result[1] == expected[1]


def test_subtract_start_is_the_same():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )

    expected = ArithmeticalDateRange(
        start=datetime(2021, 3, 1), end=datetime(2021, 4, 1)
    )

    assert m1 - m2 == expected


def test_subtract_end_is_the_same():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )

    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 2, 1),
    )

    assert m1 - m2 == expected


def test_add_other_end_is_greater():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )

    assert m1 + m2 == expected


def test_add_other_is_larger_than_complete_range():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 3, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )

    assert m1 + m2 == m2


def test_add_other_start_is_smaller():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )
    expected = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )

    assert m1 + m2 == expected


def test_add_other_is_contained():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 3, 1),
    )

    assert m1 + m2 == m1


def test_add_start_is_the_same():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 3, 1),
    )

    assert m1 + m2 == m1


def test_add_end_is_the_same():
    m1 = ArithmeticalDateRange(
        start=datetime(2021, 1, 1),
        end=datetime(2021, 4, 1),
    )
    m2 = ArithmeticalDateRange(
        start=datetime(2021, 2, 1),
        end=datetime(2021, 4, 1),
    )

    assert m1 + m2 == m1
