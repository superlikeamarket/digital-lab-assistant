import pytest
from lab_assistant.cfu import calculate_cfu


def test_calculate_cfu_with_decimal_dilution():
    cfu = calculate_cfu(132, 0.1, "0.0001")
    assert cfu == pytest.approx(13200000)


def test_calculate_cfu_with_exponent_dilution():
    cfu = calculate_cfu(132, 0.1, "-4")
    assert cfu == pytest.approx(13200000)


def test_calculate_cfu_with_power_format():
    cfu = calculate_cfu(132, 0.1, "10^-4")
    assert cfu == pytest.approx(13200000)


def test_calculate_cfu_negative_colonies():
    with pytest.raises(ValueError):
        calculate_cfu(-5, 0.1, "0.0001")


def test_calculate_cfu_zero_volume():
    with pytest.raises(ValueError):
        calculate_cfu(132, 0, "0.0001")


def test_calculate_cfu_invalid_dilution():
    with pytest.raises(ValueError):
        calculate_cfu(132, 0.1, "banana")