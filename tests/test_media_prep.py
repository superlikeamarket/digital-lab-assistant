import pytest
from lab_assistant.media_prep import calculate_mass_from_concentration

def test_media_prep_default_units():
    mass = calculate_mass_from_concentration("40", "0.5")
    assert mass == pytest.approx(20)

def test_media_prep_with_units():
    mass = calculate_mass_from_concentration("40 g/L", "500 mL")
    assert mass == pytest.approx(20)

def test_calculate_mass_invalid_unit():
    with pytest.raises(ValueError):
        calculate_mass_from_concentration("40", "500 kg")


def test_calculate_mass_negative_volume():
    with pytest.raises(ValueError):
        calculate_mass_from_concentration("40", "-5 mL")


def test_calculate_mass_bad_format():
    with pytest.raises(ValueError):
        calculate_mass_from_concentration("40", "500mL")