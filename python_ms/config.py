"""Contains global constants used by the package"""

import random
import re

# Basic units of time

MILLISECOND = 1
SECOND = 10**3 * MILLISECOND
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
MONTH = 30 * DAY
YEAR = 365 * DAY + 6 * HOUR


# Less common units of time

KILOSECOND = 10**3 * SECOND
MEGASECOND = 10**3 * KILOSECOND
GIGASECOND = 10**3 * MEGASECOND
TERASECOND = 10**3 * GIGASECOND
PETASECOND = 10**3 * TERASECOND
EXASECOND = 10**3 * PETASECOND
ZETTASECOND = 10**3 * EXASECOND
YOTTASECOND = 10**3 * ZETTASECOND
FORTNIGHT = 2 * WEEK
DECADE = 10 * YEAR
CENTURY = 10 * DECADE
MILLENIUM = 10 * CENTURY


# Esoteric units of time

# https://en.wikipedia.org/wiki/List_of_humorous_units_of_measurement#Time
JIFFY = random.randint(1, 10) * MILLISECOND
MILLIDAY = DAY // 1000
MICROCENTURY = 52 * MINUTE + 35 * SECOND + 700 * MILLISECOND
NANOCENTURY = MICROCENTURY // 1000
FRIEDMAN = 6 * MONTH
SCARAMUCCI = 11 * DAY
LUSTRUM = 5 * YEAR
OLYMPIAD = 4 * YEAR
INDICTION = 15 * YEAR
SCORE = 20 * YEAR
JUBILEE = 50 * YEAR
MEGAANNUM = 10**3 * MILLENIUM
AEON = 10**3 * MEGAANNUM


# Regular expressions

TIME_REGEX = re.compile(r'^([+-]?\d+(?:\.\d*)?|\.\d+)\s?([a-zA-Z-]*)$')
