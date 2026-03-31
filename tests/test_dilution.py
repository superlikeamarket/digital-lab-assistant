import pytest
from lab_assistant.dilution import calculate_dilution


def test_calculate_dilution_valid():
    stock_volume, diluent_volume = calculate_dilution(100, 10, 50)

    assert stock_volume == 5
    assert diluent_volume == 45


def test_calculate_dilution_target_greater_than_stock():
    with pytest.raises(ValueError):
        calculate_dilution(10, 20, 50)


def test_calculate_dilution_zero_stock_concentration():
    with pytest.raises(ValueError):
        calculate_dilution(0, 10, 50)


def test_calculate_dilution_negative_final_volume():
    with pytest.raises(ValueError):
        calculate_dilution(100, 10, -50)