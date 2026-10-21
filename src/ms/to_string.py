"""Converting milliseconds to a time string."""

import ms.config as cfg


def ms_to_string(time: int, *, long: bool = False) -> str:
    """Convert miliseconds to a time string."""
    forms = ("ms", " millisecond", " milliseconds")
    time_unit = cfg.MILLISECOND

    if abs(time) >= cfg.DAY:
        forms = ("d", " day", " days")
        time_unit = cfg.DAY
    elif cfg.HOUR <= abs(time) < cfg.DAY:
        forms = ("h", " hour", " hours")
        time_unit = cfg.HOUR
    elif cfg.MINUTE <= abs(time) < cfg.HOUR:
        forms = ("m", " minute", " minutes")
        time_unit = cfg.MINUTE
    elif cfg.SECOND <= abs(time) < cfg.MINUTE:
        forms = ("s", " second", " seconds")
        time_unit = cfg.SECOND

    final_time = time // time_unit
    form_idx = 0
    if long:
        form_idx += 1
        form_idx += final_time not in {1, -1}
    form = forms[form_idx]
    return f"{final_time}{form}"
