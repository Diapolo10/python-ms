"""Python equivalent of the JavaScript ms package"""

from enum import IntEnum
import re

TIME_REGEX = re.compile(r'([+-]?\d*\.?\d*)\s?([a-zA-Z]*)')


class UnitMultiplier(IntEnum):
    """Multipliers for different units of time"""

    MILLISECOND = 1
    SECOND = 10**3
    MINUTE = 60 * 10**3
    HOUR = 60 * 60 * 10**3
    DAY = 24 * 60 * 60 * 10**3
    WEEK = 7 * 24 * 60 * 60 * 10**3
    MONTH = 30 * 24 * 60 * 60 * 10**3
    YEAR = 365 * 24 * 60 * 60 * 10**3


def unit_conversion(unit: str) -> int:
    """
    Returns a suitable multiplier from milliseconds to the desired unit

    Raises ValueError if no suitable conversion is found.
    """

    # pylint: disable=R0911
    match (unit.lower()):
        case ['y' | 'yr' | 'yrs' | 'year' | 'years']:
            return UnitMultiplier.YEAR
        case ['mon' | 'mth' | 'mths' | 'month' | 'months']:
            return UnitMultiplier.MONTH
        case ['w' | 'week' | 'weeks']:
            return UnitMultiplier.WEEK
        case ['d' | 'day' | 'days']:
            return UnitMultiplier.DAY
        case ['h' | 'hr' | 'hrs' | 'hour' | 'hours']:
            return UnitMultiplier.HOUR
        case ['m' | 'min' | 'mins' | 'minute' | 'minutes']:
            return UnitMultiplier.MINUTE
        case ['s' | 'sec' | 'secs' | 'second' | 'seconds']:
            return UnitMultiplier.SECOND
        case ['ms' | 'msec' | 'msecs' | 'millisecond' | 'milliseconds']:
            return UnitMultiplier.MILLISECOND
        case _:
            raise ValueError("Unsupported unit")


def parse_time(time: str) -> int:
    """Parses time in string format to milliseconds"""

    result = TIME_REGEX.search(time)
    if result is None:
        raise ValueError(f"Parsing error; {time} is not a valid number")

    value, unit = result.groups()  # NOTE: Handle floats
    multiplier = unit_conversion(unit)
    return int(value) * multiplier


# class ms:
#     """Implements the interface"""
