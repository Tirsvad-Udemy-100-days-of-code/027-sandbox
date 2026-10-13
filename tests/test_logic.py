"""Tests for the pure decisions behind the windows."""

from day27 import constants
from day27.logic import (
    checkbutton_text,
    describe_value,
    first_selected,
    label_text_for,
)


def test_label_text_for_returns_entry_text() -> None:
    """Typed text is shown as it is."""
    assert label_text_for("Hello") == "Hello"


def test_label_text_for_returns_clicked_text_when_blank() -> None:
    """Blank text gives the clicked message."""
    assert label_text_for("   ") == constants.BUTTON_CLICKED_TEXT


def test_label_text_for_returns_clicked_text_when_empty() -> None:
    """Empty text gives the clicked message."""
    assert label_text_for("") == constants.BUTTON_CLICKED_TEXT


def test_label_text_for_strips_surrounding_whitespace() -> None:
    """Surrounding whitespace is removed."""
    assert label_text_for("  Hello  ") == "Hello"


def test_checkbutton_text_is_on_when_checked() -> None:
    """State 1 is On."""
    assert checkbutton_text(1) == "On"


def test_checkbutton_text_is_off_when_unchecked() -> None:
    """State 0 is Off."""
    assert checkbutton_text(0) == "Off"


def test_first_selected_returns_item_at_selection() -> None:
    """The first selected index picks the item."""
    assert first_selected(("a", "b", "c"), (1, 2)) == "b"


def test_first_selected_returns_none_when_selection_empty() -> None:
    """Nothing selected gives ``None``."""
    assert first_selected(("a", "b"), ()) is None


def test_describe_value_joins_widget_and_value() -> None:
    """The line reads ``Widget: value``."""
    assert describe_value("Spinbox", 3) == "Spinbox: 3"
