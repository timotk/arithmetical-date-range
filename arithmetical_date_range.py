from datetime import datetime
from typing import List, Union


class ArithmeticalDateRange:
    """
    Date Range which can do arithmetic (addition and subtraction).

    Example - Subtraction
    ---------------------
    >>> from datetime import datetime
    >>> from arithmetical_date_range import ArithmeticalDateRange

    >>> a = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 3))
    >>> b = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 4))

    >>> a - b
    ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-02 00:00:00)


    Example - Addition
    ------------------
    >>> from datetime import datetime
    >>> from arithmetical_date_range import ArithmeticalDateRange

    >>> a = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 3))
    >>> b = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 4))

    >>> a + b
    ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-04 00:00:00)


    Example - Addition of multiple date ranges
    ------------------------------------------
    >>> from datetime import datetime
    >>> from arithmetical_date_range import ArithmeticalDateRange

    >>> a = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 3))
    >>> b1 = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 2))
    >>> b2 = ArithmeticalDateRange(start=datetime(2021, 1, 3), end=datetime(2021, 1, 4))

    >>> a + [b1, b2]
    ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-04 00:00:00)


    Example - Subtraction of multiple date ranges
    ------------------------------------------
    >>> from datetime import datetime
    >>> from arithmetical_date_range import ArithmeticalDateRange

    >>> a = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 3))
    >>> b1 = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 2))
    >>> b2 = ArithmeticalDateRange(start=datetime(2021, 1, 3), end=datetime(2021, 1, 4))

    >>> a - [b1, b2]
    ArithmeticalDateRange(2021-01-02 00:00:00, 2021-01-03 00:00:00)
    """

    def __init__(self, start: datetime, end: datetime) -> None:
        if not start <= end:
            raise ValueError("Start needs to be before end")

        self.start = start
        self.end = end

    def __sub__(
        self, other: "ArithmeticalDateRange"
    ) -> Union["ArithmeticalDateRange", List["ArithmeticalDateRange"], None]:
        if isinstance(other, list):
            result = self
            for adr in other:
                result -= adr
            return result

        if self.start > other.end:
            return self
        if self.end < other.start:
            return self

        if other.start > self.start:
            if other.end >= self.end:
                return ArithmeticalDateRange(self.start, other.start)
            if other.end < self.end:
                return [
                    ArithmeticalDateRange(start=self.start, end=other.start),
                    ArithmeticalDateRange(start=other.end, end=self.end),
                ]
        if self.start >= other.start:
            if other.end > self.end:
                return None
            if other.end <= self.end:
                return ArithmeticalDateRange(other.end, self.end)
        raise ValueError("An unknown error occured")

    def __add__(
        self, other: "ArithmeticalDateRange"
    ) -> Union["ArithmeticalDateRange", List["ArithmeticalDateRange"]]:
        if isinstance(other, list):
            result = self
            for adr in other:
                result += adr
            return result

        if other.start <= self.start and other.end >= self.end:
            return other
        if other.start > self.start and other.end < self.end:
            return self
        if other.start <= self.start and other.end < self.end:
            return ArithmeticalDateRange(start=other.start, end=self.end)
        if other.start > self.start and other.end >= self.end:
            return ArithmeticalDateRange(start=self.start, end=other.end)

        raise ValueError("An unknown error occured")

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArithmeticalDateRange):
            raise NotImplementedError
        return self.start == other.start and self.end == other.end

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.start}, {self.end})"
