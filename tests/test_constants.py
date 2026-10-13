"""Tests for the constants module and the package marker."""

import day27
from day27 import constants


def test_package_has_a_version() -> None:
    """The package exposes a version string."""
    assert day27.__version__ == "0.1.0"


def test_window_minimum_size_is_positive() -> None:
    """The minimum window size is a positive number of pixels."""
    assert constants.WINDOW_MIN_WIDTH > 0
    assert constants.WINDOW_MIN_HEIGHT > 0


def test_label_font_has_family_size_and_style() -> None:
    """The label font is a (family, size, style) tuple."""
    family, size, style = constants.LABEL_FONT
    assert family
    assert size > 0
    assert style
