from specs import Fraction
import pytest
import specs
@pytest.fixture
def set_up_fractions():
    frac_1_3 = specs.Fraction(1, 3)
    frac_1_2 = specs.Fraction(1, 2)
    frac_n2_3 = specs.Fraction(-2, 3)
    return frac_1_3, frac_1_2, frac_n2_3

def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    with pytest.raises(ZeroDivisionError) as excinfo:
        specs.Fraction(1, 0)
    with pytest.raises(TypeError) as excinfo:
        specs.Fraction(1.5, 3)
    with pytest.raises(TypeError) as excinfo:
        specs.Fraction(1, 1.3)
    frac = specs.Fraction(30, 42)
    assert frac.numer == 5
    assert frac.denom == 7

def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert str(specs.Fraction(5, 1)) == "5"
    assert str(frac_1_3) == "1 / 3"
    assert str(frac_1_2) == "1 / 2"
    assert str(frac_n2_3) == "-2 / 3"

def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.

def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 == specs.Fraction(1, 2)
    assert frac_1_3 == specs.Fraction(2, 6)
    assert frac_n2_3 == specs.Fraction(8, -12)
    assert float(frac_n2_3) == frac_n2_3

def test_fraction_add(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3 + frac_1_2 == specs.Fraction(5, 6)

def test_fraction_sub(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 - frac_1_3 == specs.Fraction(1, 6)

def test_fraction_mul(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 * frac_1_3 == specs.Fraction(1, 6)

def test_function_truediv(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 / frac_1_3 == specs.Fraction(3, 2)
    with pytest.raises(ZeroDivisionError) as excinfo:
        specs.Fraction(0, 3) / specs.Fraction(0, 2)
