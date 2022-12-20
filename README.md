# Python-ms

A Python equivalent to the JavaScript ms package.

This port of the original project supports some additional string-to-ms
conversions, but otherwise the functionality is identical. This version
also uses integers for everything to avoid rounding errors with
floating-point numbers when using large values.

Using the project's unit tests as examples is recommended, as they cover
everything.

## Installation

The project is available via PyPI:

```sh
pip install python_ms
```

## Examples

### Convert from strings

```python
import python_ms as ms

ms('2 days')  # 172_800_000
ms('1d')      # 86_400_000
ms('10h')     # 36_000_000
ms('2.5 hrs') # 9_000_000
ms('2h')      # 7_200_000
ms('1m')      # 60_000
ms('5s')      # 5_000
ms('1y')      # 31_557_600_000
ms('100')     # 100
ms('-3 days') # -259_200_000
ms('-1h')     # -3_600_000
ms('-200')    # -200
```

### Convert from milliseconds

```python
import python_ms as ms

ms(60_000)          # "1m"
ms(2 * 60_000)      # "2m"
ms(-3 * 60_000)     # "-3m"
ms(ms('10 hours'))  # "10h"
```

### Time format written out

```python
import python_ms as ms

ms(60_000, long=True)          # "1 minute"
ms(2 * 60_000, long=True)      # "2 minutes"
ms(-3 * 60_000, long=True)     # "-3 minutes"
ms(ms('10 hours'), long=True)  # "10 hours"
```

## Features

- Has no dependencies aside from the standard library
- If a number is supplied to `python_ms`, a string with a unit is returned
- If a string that contains the number is supplied, it returns it as a number (e.g.: it returns `100` for `'100'`)
- If you pass a string with a number and a valid unit, the number of equivalent milliseconds is returned

## Related Packages

- [ms](https://github.com/vercel/ms) - The original JavaScript `ms` package

## Caught a Bug?

1. [Fork](https://help.github.com/articles/fork-a-repo/) this repository to your own GitHub account and then [clone](https://help.github.com/articles/cloning-a-repository/) it to your local device
2. Install `poetry` (if it isn't alreeady installed)
3. Run `poetry install` in the project directory. This fetches development dependencies like `pytest` and sets up everything for you to start debugging

As always, you can run the tests using: `poetry run pytest`
