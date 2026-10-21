"""Unit conversions."""

import ms.config as cfg


def common_unit_conversion(unit: str) -> int:
    """
    Return a suitable multiplier from milliseconds to the desired unit.

    Raises ValueError if no suitable conversion is found.
    """
    result = None

    match unit:
        case "a" | "y" | "yr" | "yrs" | "year" | "years":
            result = cfg.YEAR
        case "mon" | "mth" | "mths" | "month" | "months":
            result = cfg.MONTH
        case "w" | "wk" | "wks" | "week" | "weeks":
            result = cfg.WEEK
        case "d" | "day" | "days":
            result = cfg.DAY
        case "h" | "hr" | "hrs" | "hour" | "hours":
            result = cfg.HOUR
        case "m" | "min" | "mins" | "minute" | "minutes":
            result = cfg.MINUTE
        case "s" | "sec" | "secs" | "second" | "seconds":
            result = cfg.SECOND
        case "" | "ms" | "msec" | "msecs" | "millisecond" | "milliseconds":
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

    match unit:
        case "mil" | "mils" | "millenium" | "milleniums":
            result = cfg.MILLENIUM
        case "cnt" | "cnts" | "ctr" | "ctrs" | "century" | "centuries":
            result = cfg.CENTURY
        case "dc" | "dcs" | "decade" | "decades":
            result = cfg.DECADE
        case "f" | "fn" | "fns" | "fortnight" | "fortnights":
            result = cfg.FORTNIGHT
        case "Ys" | "Ysec" | "Ysecs" | "yottasecond" | "yottaseconds":
            result = cfg.YOTTASECOND
        case "Zs" | "Zsec" | "Zsecs" | "zettasecond" | "zettaseconds":
            result = cfg.ZETTASECOND
        case "Es" | "Esec" | "Esecs" | "exasecond" | "exaseconds":
            result = cfg.EXASECOND
        case "Ps" | "Psec" | "Psecs" | "petasecond" | "petaseconds":
            result = cfg.PETASECOND
        case "Ts" | "Tsec" | "Tsecs" | "terasecond" | "teraseconds":
            result = cfg.TERASECOND
        case "Gs" | "Gsec" | "Gsecs" | "gigasecond" | "gigaseconds":
            result = cfg.GIGASECOND
        case "Ms" | "Msec" | "Msecs" | "megasecond" | "megaseconds":
            result = cfg.MEGASECOND
        case "ks" | "ksec" | "ksecs" | "kilosecond" | "kiloseconds":
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

    match unit:
        case "aeon" | "aeons":
            result = cfg.AEON
        case "Mann" | "Manns" | "megaannum" | "megaannums" | "mega-annum" | "mega-annums":
            result = cfg.MEGAANNUM
        case "jubilee" | "jubilees":
            result = cfg.JUBILEE
        case "score" | "scores":
            result = cfg.SCORE
        case "ind" | "inds" | "indiction" | "indictions":
            result = cfg.INDICTION
        case "olympiad" | "olympiads":
            result = cfg.OLYMPIAD
        case "lustrum" | "lustrums":
            result = cfg.LUSTRUM
        case "scara" | "scaras" | "scaramucci" | "scaramuccis":
            result = cfg.SCARAMUCCI
        case "Fm" | "Fms" | "fm" | "fms" | "friedman" | "friedmans":
            result = cfg.FRIEDMAN
        case "nc" | "ncs" | "ncent" | "ncents" | "nanocentury" | "nanocenturies":
            result = cfg.NANOCENTURY
        case "mc" | "mcs" | "mcent" | "mcents" | "microcentury" | "microcenturies":
            result = cfg.MICROCENTURY
        case "md" | "mds" | "mday" | "mdays" | "milliday" | "millidays":
            result = cfg.MILLIDAY
        case "jiffy" | "jiffies":
            result = cfg.JIFFY
        case _:
            msg = "Unsupported unit"
            raise ValueError(msg)

    return result
