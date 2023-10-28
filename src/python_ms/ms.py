"""Python equivalent of the JavaScript ms package."""

from __future__ import annotations

import types
from typing import overload

import python_ms.config as cfg


def common_unit_conversion(unit: str) -> int:
    """
    Return a suitable multiplier from milliseconds to the desired unit.

    Raises ValueError if no suitable conversion is found.
    """
    result = None

    match (unit):
        case 'a' | 'y' | 'yr' | 'yrs' | 'year' | 'years':
            result = cfg.YEAR
        case 'mon' | 'mth' | 'mths' | 'month' | 'months':
            result = cfg.MONTH
        case 'w' | 'wk' | 'wks' | 'week' | 'weeks':
            result = cfg.WEEK
        case 'd' | 'day' | 'days':
            result = cfg.DAY
        case 'h' | 'hr' | 'hrs' | 'hour' | 'hours':
            result = cfg.HOUR
        case 'm' | 'min' | 'mins' | 'minute' | 'minutes':
            result = cfg.MINUTE
        case 's' | 'sec' | 'secs' | 'second' | 'seconds':
            result = cfg.SECOND
        case '' | 'ms' | 'msec' | 'msecs' | 'millisecond' | 'milliseconds':
            result = cfg.MILLISECOND
        case _:
            result = uncommon_unit_conversion(unit)

    return result


def uncommon_unit_conversion(unit: str) -> int:
    """
    Return a suitable multiplier from milliseconds to the desired unit.

    Raises ValueError if no suitable conversion is found.
    """
    result = None

    match (unit):
        case 'mil' | 'mils' | 'millenium' | 'milleniums':
            result = cfg.MILLENIUM
        case 'cnt' | 'cnts' | 'ctr' | 'ctrs' | 'century' | 'centuries':
            result = cfg.CENTURY
        case 'dc' | 'dcs' | 'decade' | 'decades':
            result = cfg.DECADE
        case 'f' | 'fn' | 'fns' | 'fortnight' | 'fortnights':
            result = cfg.FORTNIGHT
        case 'Ys' | 'Ysec' | 'Ysecs' | 'yottasecond' | 'yottaseconds':
            result = cfg.YOTTASECOND
        case 'Zs' | 'Zsec' | 'Zsecs' | 'zettasecond' | 'zettaseconds':
            result = cfg.ZETTASECOND
        case 'Es' | 'Esec' | 'Esecs' | 'exasecond' | 'exaseconds':
            result = cfg.EXASECOND
        case 'Ps' | 'Psec' | 'Psecs' | 'petasecond' | 'petaseconds':
            result = cfg.PETASECOND
        case 'Ts' | 'Tsec' | 'Tsecs' | 'terasecond' | 'teraseconds':
            result = cfg.TERASECOND
        case 'Gs' | 'Gsec' | 'Gsecs' | 'gigasecond' | 'gigaseconds':
            result = cfg.GIGASECOND
        case 'Ms' | 'Msec' | 'Msecs' | 'megasecond' | 'megaseconds':
            result = cfg.MEGASECOND
        case 'ks' | 'ksec' | 'ksecs' | 'kilosecond' | 'kiloseconds':
            result = cfg.KILOSECOND
        case _:
            result = esoteric_unit_conversion(unit)

    return result


def esoteric_unit_conversion(unit: str) -> int:
    """
    Return a suitable multiplier from milliseconds to the desired unit.

    Raises ValueError if no suitable conversion is found.
    """
    result = None

    match (unit):
        case 'aeon' | 'aeons':
            result = cfg.AEON
        case 'Mann' | 'Manns' | 'megaannum' | 'megaannums' | 'mega-annum' | 'mega-annums':
            result = cfg.MEGAANNUM
        case 'jubilee' | 'jubilees':
            result = cfg.JUBILEE
        case 'score' | 'scores':
            result = cfg.SCORE
        case 'ind' | 'inds' | 'indiction' | 'indictions':
            result = cfg.INDICTION
        case 'olympiad' | 'olympiads':
            result = cfg.OLYMPIAD
        case 'lustrum' | 'lustrums':
            result = cfg.LUSTRUM
        case 'scara' | 'scaras' | 'scaramucci' | 'scaramuccis':
            result = cfg.SCARAMUCCI
        case 'Fm' | 'Fms' | 'fm' | 'fms' | 'friedman' | 'friedmans':
            result = cfg.FRIEDMAN
        case 'nc' | 'ncs' | 'ncent' | 'ncents' | 'nanocentury' | 'nanocenturies':
            result = cfg.NANOCENTURY
        case 'mc' | 'mcs' | 'mcent' | 'mcents' | 'microcentury' | 'microcenturies':
            result = cfg.MICROCENTURY
        case 'md' | 'mds' | 'mday' | 'mdays' | 'milliday' | 'millidays':
            result = cfg.MILLIDAY
        case 'jiffy' | 'jiffies':
            result = cfg.JIFFY
        case _:
            msg = 'Unsupported unit'
            raise ValueError(msg)

    return result


def parse_time(time: str) -> int:
    """
    Parse time in string format to milliseconds.

    NOTE: The function is case-sensitive in order to accommodate some types.

    Raises ValueError on invalid strings.
    """
    result = cfg.TIME_REGEX.search(time)
    if result is None:
        msg = f'Parsing error; {time} is not a valid number'
        raise ValueError(msg)

    value, unit = result.groups()
    multiplier = common_unit_conversion(unit)
    extra = 0

    if '.' in value:
        value, decimals, *_ = value.split('.')
        if not value:
            value = '0'
        if not decimals:
            decimals = '0'
        extra = int(decimals) * multiplier // 10**len(decimals)

    return int(value) * multiplier + extra


def ms_to_string(time: int, long: bool = False) -> str:
    """Convert miliseconds to a time string."""
    forms = ('ms', ' millisecond', ' milliseconds')
    time_unit = cfg.MILLISECOND

    if abs(time) >= cfg.DAY:
        forms = ('d', ' day', ' days')
        time_unit = cfg.DAY
    elif cfg.HOUR <= abs(time) < cfg.DAY:
        forms = ('h', ' hour', ' hours')
        time_unit = cfg.HOUR
    elif cfg.MINUTE <= abs(time) < cfg.HOUR:
        forms = ('m', ' minute', ' minutes')
        time_unit = cfg.MINUTE
    elif cfg.SECOND <= abs(time) < cfg.MINUTE:
        forms = ('s', ' second', ' seconds')
        time_unit = cfg.SECOND

    final_time = time // time_unit
    form_idx = 0
    if long:
        form_idx += 1
        form_idx += final_time not in {1, -1}
    form = forms[form_idx]
    return f"{final_time}{form}"


class _ms(types.ModuleType):  # noqa: N801
    """Implement the module interface."""

    @overload
    def __call__(self: _ms, value: str, long: bool) -> int:
        pass

    @overload
    def __call__(self: _ms, value: int, long: bool) -> str:
        pass

    def __call__(self: _ms, value: str | int, long: bool = False) -> int | str:
        if isinstance(value, str):
            return parse_time(value)
        if isinstance(value, int):
            return ms_to_string(value, long)

        msg = 'This type is not supported'
        raise NotImplementedError(msg)
