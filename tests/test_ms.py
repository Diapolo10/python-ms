"""Tests the ms class"""

import pytest

import python_ms as ms
from python_ms.config import MILLISECOND


def test_ms_string_integer_input():
    """Tests that the ms class works correctly with text input with integers"""

    assert 31_557_600_000 * MILLISECOND == ms('1y')
    assert 2_592_000_000 * MILLISECOND == ms('1 mth')
    assert 604_800_000 * MILLISECOND == ms('1 wk')
    assert 172_800_000 * MILLISECOND == ms('2 days')
    assert 86_400_000 * MILLISECOND == ms('1d')
    assert 36_000_000 * MILLISECOND == ms('10h')
    assert 7_200_000 * MILLISECOND == ms('2 hours')
    assert 60_000 * MILLISECOND == ms('1m')
    assert 5_000 * MILLISECOND == ms('5s')
    assert 100 * MILLISECOND == ms('100')
    assert -259_200_000 * MILLISECOND == ms('-3 days')
    assert -3_600_000 * MILLISECOND == ms('-1h')
    assert -200 * MILLISECOND == ms('-200')


def test_ms_string_integer_input_uncommon():
    """Tests that the ms class works correctly with text input with uncommon integers"""

    assert 31_557_600_000_000 * MILLISECOND == ms('1 millenium')
    assert 3_155_760_000_000 * MILLISECOND == ms('1 century')
    assert 631_152_000_000 * MILLISECOND == ms('2 decades')
    assert 1_209_600_000 * MILLISECOND == ms('1 fortnight')
    assert 1_000_000_000_000_000_000_000_000_000 * MILLISECOND == ms('1Ys')
    assert 1_000_000_000_000_000_000_000_000 * MILLISECOND == ms('1Zs')
    assert 1_000_000_000_000_000_000_000 * MILLISECOND == ms('1Es')
    assert 1_000_000_000_000_000_000 * MILLISECOND == ms('1Ps')
    assert 1_000_000_000_000_000 * MILLISECOND == ms('1Ts')
    assert 1_000_000_000_000 * MILLISECOND == ms('1Gs')
    assert 1_000_000_000 * MILLISECOND == ms('1Ms')
    assert 1_000_000 * MILLISECOND == ms('1ks')


def test_ms_string_integer_input_esoteric():
    """Tests that the ms class works correctly with text input with esoteric integers"""

    assert 31_557_600_000_000_000_000 * MILLISECOND == ms('1 aeon')
    assert 31_557_600_000_000_000 * MILLISECOND == ms('1 mega-annum')
    assert 1_577_880_000_000 * MILLISECOND == ms('1 jubilee')
    assert 631_152_000_000 * MILLISECOND == ms('1 score')
    assert 473_364_000_000 * MILLISECOND == ms('1 indiction')
    assert 252_460_800_000 * MILLISECOND == ms('2 olympiad')
    assert 157_788_000_000 * MILLISECOND == ms('1 lustrum')
    assert 950_400_000 * MILLISECOND == ms('1 scaramucci')
    assert 15_552_000_000 * MILLISECOND == ms('1 friedman')
    assert 3155700 * MILLISECOND == ms('1 microcentury')
    assert 3155 * MILLISECOND == ms('1 nanocentury')
    assert 86400 * MILLISECOND == ms('1 milliday')
    assert 1 * MILLISECOND <= ms('1 jiffy') <= 10 * MILLISECOND


def test_ms_string_float_input():
    """Tests that the ms class works correctly with text input with floats"""

    assert ms('2.5 hrs') == 9_000_000
    assert ms('2.2 hrs') == 7_920_000
    assert ms('.1 hrs') == 360_000
    assert ms('1. hrs') == 3_600_000


def test_ms_int_input():
    """Tests that the ms class works correctly with integer input"""

    assert ms(60_000) == '1m'
    assert ms(2 * 60_000) == '2m'
    assert ms(-3 * 60_000) == '-3m'
    assert ms(ms('10 hours')) == '10h'
    assert ms(ms('1 second')) == '1s'
    assert ms(ms('25 hours')) == '1d'


def test_ms_int_input_long():
    """Tests that the ms class works correctly with integer input when asking long output"""

    assert ms(60_000, long=True) == "1 minute"
    assert ms(2 * 60_000, long=True) == "2 minutes"
    assert ms(-3 * 60000, long=True) == "-3 minutes"
    assert ms(ms('10 hours'), long=True) == "10 hours"
    assert ms(ms('25 hours'), long=True) == "1 day"
    assert ms(5_000, long=True) == "5 seconds"
    assert ms(ms('5s'), long=True) == "5 seconds"
    assert ms(420, long=True) == "420 milliseconds"


def test_ms_unsupported_input():
    """Tests that the ms class behaves as expected with unsupported types"""

    with pytest.raises(NotImplementedError):
        ms(...)


def test_ms_string_invalid():
    """Tests ms class behaviour with an invalid string"""

    with pytest.raises(ValueError):
        ms('!')

    with pytest.raises(ValueError):
        ms('3 thisunitdoesntexist')
