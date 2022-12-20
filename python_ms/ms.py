"""Python equivalent of the JavaScript ms package"""

import types
from typing import overload

import python_ms.config as cfg


def common_unit_conversion(unit: str) -> int:
    """
    Returns a suitable multiplier from milliseconds to the desired unit

    Raises ValueError if no suitable conversion is found.
    """

    # pylint: disable=R0911
    match (unit):
        case 'a' | 'y' | 'yr' | 'yrs' | 'year' | 'years':
            return cfg.YEAR
        case 'mon' | 'mth' | 'mths' | 'month' | 'months':
            return cfg.MONTH
        case 'w' | 'wk' | 'wks' | 'week' | 'weeks':
            return cfg.WEEK
        case 'd' | 'day' | 'days':
            return cfg.DAY
        case 'h' | 'hr' | 'hrs' | 'hour' | 'hours':
            return cfg.HOUR
        case 'm' | 'min' | 'mins' | 'minute' | 'minutes':
            return cfg.MINUTE
        case 's' | 'sec' | 'secs' | 'second' | 'seconds':
            return cfg.SECOND
        case '' | 'ms' | 'msec' | 'msecs' | 'millisecond' | 'milliseconds':
            return cfg.MILLISECOND
        case _:
            return uncommon_unit_conversion(unit)


def uncommon_unit_conversion(unit: str) -> int:
    """
    Returns a suitable multiplier from milliseconds to the desired unit

    Raises ValueError if no suitable conversion is found.
    """

    # pylint: disable=R0911
    match (unit):
        case 'mil' | 'mils' | 'millenium' | 'milleniums':
            return cfg.MILLENIUM
        case 'cnt' | 'cnts' | 'ctr' | 'ctrs' | 'century' | 'centuries':
            return cfg.CENTURY
        case 'dc' | 'dcs' | 'decade' | 'decades':
            return cfg.DECADE
        case 'f' | 'fn' | 'fns' | 'fortnight' | 'fortnights':
            return cfg.FORTNIGHT
        case 'Ys' | 'Ysec' | 'Ysecs' | 'yottasecond' | 'yottaseconds':
            return cfg.YOTTASECOND
        case 'Zs' | 'Zsec' | 'Zsecs' | 'zettasecond' | 'zettaseconds':
            return cfg.ZETTASECOND
        case 'Es' | 'Esec' | 'Esecs' | 'exasecond' | 'exaseconds':
            return cfg.EXASECOND
        case 'Ps' | 'Psec' | 'Psecs' | 'petasecond' | 'petaseconds':
            return cfg.PETASECOND
        case 'Ts' | 'Tsec' | 'Tsecs' | 'terasecond' | 'teraseconds':
            return cfg.TERASECOND
        case 'Gs' | 'Gsec' | 'Gsecs' | 'gigasecond' | 'gigaseconds':
            return cfg.GIGASECOND
        case 'Ms' | 'Msec' | 'Msecs' | 'megasecond' | 'megaseconds':
            return cfg.MEGASECOND
        case 'ks' | 'ksec' | 'ksecs' | 'kilosecond' | 'kiloseconds':
            return cfg.KILOSECOND
        case _:
            return esoteric_unit_conversion(unit)


def esoteric_unit_conversion(unit: str) -> int:
    """
    Returns a suitable multiplier from milliseconds to the desired unit

    Raises ValueError if no suitable conversion is found.
    """

    # pylint: disable=R0911
    match (unit):
        case 'aeon' | 'aeons':
            return cfg.AEON
        case 'Mann' | 'Manns' | 'megaannum' | 'megaannums' | 'mega-annum' | 'mega-annums':
            return cfg.MEGAANNUM
        case 'jubilee' | 'jubilees':
            return cfg.JUBILEE
        case 'score' | 'scores':
            return cfg.SCORE
        case 'ind' | 'inds' | 'indiction' | 'indictions':
            return cfg.INDICTION
        case 'olympiad' | 'olympiads':
            return cfg.OLYMPIAD
        case 'lustrum' | 'lustrums':
            return cfg.LUSTRUM
        case 'scara' | 'scaras' | 'scaramucci' | 'scaramuccis':
            return cfg.SCARAMUCCI
        case 'Fm' | 'Fms' | 'fm' | 'fms' | 'friedman' | 'friedmans':
            return cfg.FRIEDMAN
        case 'nc' | 'ncs' | 'ncent' | 'ncents' | 'nanocentury' | 'nanocenturies':
            return cfg.NANOCENTURY
        case 'mc' | 'mcs' | 'mcent' | 'mcents' | 'microcentury' | 'microcenturies':
            return cfg.MICROCENTURY
        case 'md' | 'mds' | 'mday' | 'mdays' | 'milliday' | 'millidays':
            return cfg.MILLIDAY
        case 'jiffy' | 'jiffies':
            return cfg.JIFFY
        case _:
            raise ValueError("Unsupported unit")


def parse_time(time: str) -> int:
    """
    Parses time in string format to milliseconds

    NOTE: The function is case-sensitive in order to accommodate some types.

    Raises ValueError on invalid strings.
    """

    result = cfg.TIME_REGEX.search(time)
    if result is None:
        raise ValueError(f"Parsing error; {time} is not a valid number")

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
    """Converts miliseconds to a time string"""

    forms = ('ms', ' millisecond', ' milliseconds')
    time_unit = cfg.MILLISECOND

    if cfg.DAY <= abs(time):
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


class _ms(types.ModuleType):
    """Implements the module interface"""

    # pylint: disable=R0903

    @overload
    def __call__(self, value: str, long: bool) -> int:
        pass

    @overload
    def __call__(self, value: int, long: bool) -> str:
        pass

    def __call__(self, value: str | int, long: bool = False) -> int | str:
        if isinstance(value, str):
            return parse_time(value)
        if isinstance(value, int):
            return ms_to_string(value, long)

        raise NotImplementedError("This type is not supported")
