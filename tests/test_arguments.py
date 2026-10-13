"""Tests for the ``*args`` and ``**kwargs`` examples."""

import pytest

from day27 import constants
from day27.arguments import Car, add, calculate, describe_text


def test_add_returns_sum_of_several_numbers() -> None:
    """The lecture example adds eight numbers."""
    assert add(3, 5, 6, 2, 1, 7, 4, 3) == 31


def test_add_returns_zero_without_arguments() -> None:
    """No numbers add up to zero."""
    assert add() == 0


def test_add_accepts_floats() -> None:
    """Floats are added like integers."""
    assert add(0.5, 0.25) == pytest.approx(0.75)


def test_calculate_adds_then_multiplies() -> None:
    """The lecture example: (2 + 3) * 5."""
    assert calculate(2, add=3, multiply=5) == 25


def test_calculate_returns_number_when_keys_missing() -> None:
    """Missing keys use the neutral values 0 and 1."""
    assert calculate(2) == 2


def test_calculate_uses_only_multiply_when_add_missing() -> None:
    """A missing ``add`` is treated as 0."""
    assert calculate(2, multiply=5) == 10


def test_calculate_uses_only_add_when_multiply_missing() -> None:
    """A missing ``multiply`` is treated as 1."""
    assert calculate(2, add=3) == 5


def test_car_keeps_given_attributes() -> None:
    """Given keywords become attributes."""
    car = Car(make="Nissan", model="Skyline", colour="Blue", seats=4)
    assert (car.make, car.model, car.colour, car.seats) == (
        "Nissan",
        "Skyline",
        "Blue",
        4,
    )


def test_car_model_is_skyline_when_given() -> None:
    """The lecture example reads the model."""
    assert Car(make="Nissan", model="Skyline").model == "Skyline"


def test_car_colour_is_none_when_missing() -> None:
    """A missing key is ``None``, not an error."""
    assert Car(make="Nissan", model="Skyline").colour is None


def test_car_attributes_are_none_without_arguments() -> None:
    """All four attributes default to ``None``."""
    car = Car()
    assert (car.make, car.model, car.colour, car.seats) == (None, None, None, None)


def test_describe_text_uses_defaults_when_only_text_given() -> None:
    """Defaults come from the constants."""
    family, size, style = constants.DEFAULT_FONT
    assert describe_text("Hi") == (
        f"'Hi': move={constants.DEFAULT_MOVE}, "
        f"align={constants.DEFAULT_ALIGN}, font={family} {size} {style}"
    )


def test_describe_text_overrides_default_by_keyword() -> None:
    """A keyword replaces its default."""
    result = describe_text("Hi", align="center", move=True)
    assert "align=center" in result
    assert "move=True" in result
