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
