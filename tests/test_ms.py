"""Tests the ms class"""

import pytest

# from python_ms.ms import _ms as ms
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

    assert 9_000_000 == ms('2.5 hrs')
    assert 7_920_000 == ms('2.2 hrs')
    assert 360_000 == ms('.1 hrs')
    assert 3_600_000 == ms('1. hrs')


def test_ms_int_input():
    """Tests that the ms class works correctly with integer input"""

    assert '1m' == ms(60_000)
    assert '2m' == ms(2 * 60_000)
    assert '-3m' == ms(-3 * 60_000)
    assert '10h' == ms(ms('10 hours'))
    assert '1s' == ms(ms('1 second'))
    assert '1d' == ms(ms('25 hours'))


def test_ms_int_input_long():
    """Tests that the ms class works correctly with integer input when asking long output"""

    assert "1 minute" == ms(60_000, long=True)
    assert "2 minutes" == ms(2 * 60_000, long=True)
    assert "-3 minutes" == ms(-3 * 60000, long=True)
    assert "10 hours" == ms(ms('10 hours'), long=True)
    assert "1 day" == ms(ms('25 hours'), long=True)
    assert "5 seconds" == ms(5_000, long=True)
    assert "5 seconds" == ms(ms('5s'), long=True)
    assert "420 milliseconds" == ms(420, long=True)


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
