# Arithmetical - Add and subtract (partially) overlapping Python date ranges

## Usage

#### Subtraction
You have two date ranges (`a` and `b`) and you want to subtract `b` from `a`:
```
a:     <---------->
b:          <---------->
a - b: <--->
```

In code:
```python
>>> from datetime import datetime
>>> from arithmetical_date_range import ArithmeticalDateRange

>>> a = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 3))
>>> b = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 4))

>>> a - b
ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-02 00:00:00)

```


#### Addition
Or you want to add `b` to `a`:
```
a:     <---------->
b:          <---------->
a + b: <--------------->
```

In code:
```python
>>> from datetime import datetime
>>> from arithmetical_date_range import ArithmeticalDateRange

>>> a = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 3))
>>> b = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 4))

>>> a + b
ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-04 00:00:00)

```

Or you want to cut a part out of `a` using `b`:
```
a:     <---------------------------->
b:           <--------------->
a - b: <---->                 <----->
```

In code:
```python
>>> from datetime import datetime
>>> from arithmetical_date_range import ArithmeticalDateRange

>>> a = ArithmeticalDateRange(start=datetime(2021, 1, 1), end=datetime(2021, 1, 4))
>>> b = ArithmeticalDateRange(start=datetime(2021, 1, 2), end=datetime(2021, 1, 3))

>>> a - b
[ArithmeticalDateRange(2021-01-01 00:00:00, 2021-01-02 00:00:00), ArithmeticalDateRange(2021-01-03 00:00:00, 2021-01-04 00:00:00)]

```
