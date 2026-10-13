"""Tests for the Tkinter windows; skipped when no display is available."""

import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest

pytest.importorskip("tkinter", exc_type=ImportError)

import tkinter as tk  # noqa: E402  # must follow the importorskip guard

from day27 import constants, windows  # noqa: E402  # same reason


def _display_available() -> bool:
    try:
        root = tk.Tk()
    except tk.TclError:
        return False
    root.destroy()
    return True


needs_display = pytest.mark.skipif(
    not _display_available(), reason="no display available"
)


@pytest.fixture
def opened() -> Iterator[list[windows.Demo]]:
    """Collect demos and destroy their windows after the test."""
    demos: list[windows.Demo] = []
    yield demos
    for demo in demos:
        demo.window.destroy()


def _build(opened: list[windows.Demo], demo: windows.Demo) -> windows.Demo:
    opened.append(demo)
    return demo


def test_import_opens_no_window() -> None:
    """Importing the module in a fresh interpreter creates no root window."""
    source_dir = Path(windows.__file__).resolve().parent.parent
    code = (
        "import tkinter, day27.windows;"
        "raise SystemExit(0 if tkinter._default_root is None else 1)"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        env={"PYTHONPATH": str(source_dir)},
        check=False,
    )
    assert result.returncode == 0


@needs_display
def test_label_window_has_title_and_minimum_size(
    opened: list[windows.Demo],
) -> None:
    """The window carries the title and minimum size from the constants."""
    window = _build(opened, windows.create_label_window()).window
    assert window.title() == constants.WINDOW_TITLE
    assert window.minsize() == (
        constants.WINDOW_MIN_WIDTH,
        constants.WINDOW_MIN_HEIGHT,
    )


@needs_display
def test_label_text_ends_as_new_text(opened: list[windows.Demo]) -> None:
    """The last of the three ways to set the text wins."""
    label = _build(opened, windows.create_label_window()).widgets["label"]
    assert label.cget("text") == constants.NEW_LABEL_TEXT


@needs_display
def test_button_copies_entry_text_to_label(opened: list[windows.Demo]) -> None:
    """Clicking the button shows the entry text in the label."""
    demo = _build(opened, windows.create_button_entry_window())
    entry = demo.widgets["entry"]
    assert isinstance(entry, tk.Entry)
    entry.insert(0, "Hello")
    button = demo.widgets["button"]
    assert isinstance(button, tk.Button)
    button.invoke()
    assert demo.widgets["label"].cget("text") == "Hello"


@needs_display
def test_button_shows_clicked_text_when_entry_blank(
    opened: list[windows.Demo],
) -> None:
    """A blank entry gives the clicked message."""
    demo = _build(opened, windows.create_button_entry_window())
    button = demo.widgets["button"]
    assert isinstance(button, tk.Button)
    button.invoke()
    assert demo.widgets["label"].cget("text") == constants.BUTTON_CLICKED_TEXT


@needs_display
def test_showcase_builds_all_widgets(opened: list[windows.Demo]) -> None:
    """The showcase offers every named widget."""
    demo = _build(opened, windows.create_widget_showcase())
    expected = {
        "entry",
        "text",
        "spinbox",
        "scale",
        "checkbutton",
        "radiobutton1",
        "radiobutton2",
        "listbox",
        "result",
    }
    assert set(demo.widgets) == expected


@needs_display
def test_showcase_checkbutton_reports_on(opened: list[windows.Demo]) -> None:
    """Invoking the checkbutton reports its new state."""
    demo = _build(opened, windows.create_widget_showcase())
    checkbutton = demo.widgets["checkbutton"]
    assert isinstance(checkbutton, tk.Checkbutton)
    checkbutton.invoke()
    assert demo.widgets["result"].cget("text") == "Checkbutton: On"


@needs_display
def test_pack_layout_uses_pack(opened: list[windows.Demo]) -> None:
    """Every widget is managed by ``pack``."""
    demo = _build(opened, windows.create_pack_layout())
    assert {w.winfo_manager() for w in demo.widgets.values()} == {"pack"}


@needs_display
def test_place_layout_uses_place(opened: list[windows.Demo]) -> None:
    """Every widget is managed by ``place``."""
    demo = _build(opened, windows.create_place_layout())
    assert {w.winfo_manager() for w in demo.widgets.values()} == {"place"}


@needs_display
def test_grid_layout_uses_only_grid(opened: list[windows.Demo]) -> None:
    """Every child of the window is managed by ``grid``."""
    demo = _build(opened, windows.create_grid_layout())
    managers = {w.winfo_manager() for w in demo.window.winfo_children()}
    assert managers == {"grid"}


@needs_display
def test_grid_layout_places_widgets_from_constants(
    opened: list[windows.Demo],
) -> None:
    """Column and row of each widget come from the constants."""
    demo = _build(opened, windows.create_grid_layout())
    expected = {
        "label": constants.GRID_LABEL,
        "button": constants.GRID_BUTTON,
        "new_button": constants.GRID_NEW_BUTTON,
        "entry": constants.GRID_ENTRY,
    }
    for name, (column, row) in expected.items():
        info = demo.widgets[name].grid_info()
        assert (int(info["column"]), int(info["row"])) == (column, row)
