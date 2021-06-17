# Arithmetical - Add and subtract (partially) overlapping Python date ranges

## Usage

#### Subtraction
```python
>>> from datetime import datetime
>>> from arithmetical_date_range import ArithmeticalDateRange

>>> a1 = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 3))
>>> a2 = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 4))

>>> a1 - a2
ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-02 00:00:00)

```

#### Addition
```python
>>> from datetime import datetime
>>> from arithmetical_date_range import ArithmeticalDateRange

>>> a1 = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 3))
>>> a2 = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 4))

>>> a1 + a2
ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-04 00:00:00)

```
