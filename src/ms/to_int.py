"""Converting a time string to milliseconds."""

import ms.config as cfg
from ms.units import common_unit_conversion


def parse_time(time: str) -> int:
    """
    Parse time in string format to milliseconds.

    NOTE: The function is case-sensitive in order to accommodate some types.

    Raises ValueError on invalid strings.
    """
    result = cfg.TIME_REGEX.search(time)
    if result is None:
        msg = f"Parsing error; {time} is not a valid number"
        raise ValueError(msg)

    value = result.group("value")
    unit = result.group("unit")
    multiplier = common_unit_conversion(unit)
    extra = 0

    if "." in value:
        value, decimals, *_ = value.split(".")
        if not value:
            value = "0"
        if not decimals:
            decimals = "0"
        extra = int(decimals) * multiplier // 10 ** len(decimals)

    return int(value) * multiplier + extra
