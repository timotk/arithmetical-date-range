from datetime import datetime
from typing import List, Union


class ArithmeticalDateRange:
    """
    Date Range which can do arithmetic (addition and subtraction).

    Usage:

    Example - Subtraction
    ---------------------
    >>> from datetime import datetime
    >>> from arithmetical_date_range import ArithmeticalDateRange

    >>> a1 = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 3))
    >>> a2 = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 4))

    >>> a1 - a2
    ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-02 00:00:00)

    Example - Addition
    ------------------
    >>> from datetime import datetime
    >>> from arithmetical_date_range import ArithmeticalDateRange

    >>> a1 = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 3))
    >>> a2 = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 4))

    >>> a1 + a2
    ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-04 00:00:00)

    """

    def __init__(self, start: datetime, end: datetime) -> None:
        if not start <= end:
            raise ValueError("Start needs to be before end")

        self.start = start
        self.end = end

    def __sub__(
        self, other: "ArithmeticalDateRange"
    ) -> Union["ArithmeticalDateRange", List["ArithmeticalDateRange"], None]:

        if self.start > other.end:
            return self
        if self.end < other.start:
            return self

        if other.start > self.start:
            start = self.start
            if other.end >= self.end:
                end = other.start
                return ArithmeticalDateRange(start, end)
            if other.end < self.end:
                start1 = self.start
                end1 = other.start
                start2 = other.end
                end2 = self.end
                return [
                    ArithmeticalDateRange(start=start1, end=end1),
                    ArithmeticalDateRange(start=start2, end=end2),
                ]
        if self.start >= other.start:
            if other.end > self.end:
                return None
            if other.end <= self.end:
                return ArithmeticalDateRange(other.end, self.end)
        raise ValueError("An unknown error occured")

    def __add__(self, other: "ArithmeticalDateRange") -> "ArithmeticalDateRange":
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
