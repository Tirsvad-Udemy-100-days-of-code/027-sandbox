"""Pure decisions behind the Tkinter windows.

@file
@brief Text and value handling that needs no window, so tests can cover it.
"""

from collections.abc import Sequence

from day27 import constants


def label_text_for(entry_text: str) -> str:
    """Choose the label text after the button was clicked.

    @param entry_text The text in the entry.
    @return The entry text, or the clicked message when the entry is blank.
    """
    stripped = entry_text.strip()
    return stripped if stripped else constants.BUTTON_CLICKED_TEXT


def checkbutton_text(state: int) -> str:
    """Describe the state of a checkbutton.

    @param state 1 when checked, 0 when not.
    @return ``On`` or ``Off``.
    """
    return "On" if state else "Off"


def first_selected(items: Sequence[str], selection: Sequence[int]) -> str | None:
    """Return the first selected list item.

    @param items All items of the list.
    @param selection Selected indexes, as ``Listbox.curselection()`` gives.
    @return The first selected item, or ``None`` when nothing is selected.
    """
    return items[selection[0]] if selection else None


def describe_value(widget: str, value: object) -> str:
    """Describe the value a widget reported.

    @param widget The widget name.
    @param value The reported value.
    @return A line such as ``Spinbox: 3``.
    """
    return f"{widget}: {value}"
