"""Python equivalent of the JavaScript ms package."""

import importlib.metadata
from typing import overload

from ms.to_int import parse_time
from ms.to_string import ms_to_string

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"


@overload
def ms(value: str) -> int: ...


@overload
def ms(value: int, *, long: bool = False) -> str: ...


def ms(value: str | int, *, long: bool = False) -> int | str:
    """
    Convert time in string format to milliseconds or vice versa.

    NOTE: The function is case-sensitive in order to accommodate some types.
          E.g. "1 ms" is a millisecond, but "1 Ms" is a megasecond.

    Arguments:
        value (str | int): The time value to convert. If a string is provided, it will be converted to milliseconds.
                           If an integer is provided, it will be converted to a time string.
        long (bool, optional): If True and the value is an integer, the output will be in long format
                               (e.g., "1 minute" instead of "1m"). Ignored if the value is a string. Defaults to False.

    Raises:
        ValueError: If the string is not a valid time format.
        TypeError: If the input type is not supported.

    Returns:
        int: If the input is a string, returns the time in milliseconds.
        str: If the input is an integer, returns the time in string format.

    """
    if isinstance(value, str):
        return parse_time(value)
    if isinstance(value, int):
        return ms_to_string(value, long=long)

    msg = "This type is not supported"
    raise TypeError(msg)
