import pytest
from lab_assistant.dilution import calculate_dilution


def test_calculate_dilution_with_default_units():
    stock_volume, diluent_volume = calculate_dilution("10", "2", "0.5")
    assert stock_volume == pytest.approx(0.1)
    assert diluent_volume == pytest.approx(0.4)


def test_calculate_dilution_with_explicit_units():
    stock_volume, diluent_volume = calculate_dilution("10 g/L", "2 g/L", "500 mL")
    assert stock_volume == pytest.approx(0.1)
    assert diluent_volume == pytest.approx(0.4)


def test_calculate_dilution_target_greater_than_stock():
    with pytest.raises(ValueError):
        calculate_dilution("10", "20", "50")


def test_calculate_dilution_zero_stock_concentration():
    with pytest.raises(ValueError):
        calculate_dilution("0", "10", "50")


def test_calculate_dilution_negative_final_volume():
    with pytest.raises(ValueError):
        calculate_dilution("100", "10", "-50")
