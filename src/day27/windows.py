"""Tkinter windows from the day 27 lectures.

@file
@brief Windows with a label, a button and an entry, a widget showcase and the
``pack``, ``place`` and ``grid`` layouts. Each ``create_*`` function builds a
window and returns it without opening it; ``run`` opens it. Importing this
module opens no window.
"""

import tkinter as tk
from dataclasses import dataclass

from day27 import constants
from day27.logic import (
    checkbutton_text,
    describe_value,
    first_selected,
    label_text_for,
)


@dataclass(frozen=True)
class Demo:
    """A built window and its named widgets.

    @brief Lets a test or a caller reach the widgets of a window.
    """

    window: tk.Tk
    widgets: dict[str, tk.Widget]


def _new_window(title: str, min_size: tuple[int, int]) -> tk.Tk:
    """Create a window with a title and a minimum size.

    @param title The window title.
    @param min_size Minimum width and height in pixels.
    @return The new window, not yet open.
    """
    window = tk.Tk()
    window.title(title)
    window.minsize(width=min_size[0], height=min_size[1])
    return window


def _default_size() -> tuple[int, int]:
    """Return the minimum size of the standard window.

    @return Minimum width and height in pixels.
    """
    return (constants.WINDOW_MIN_WIDTH, constants.WINDOW_MIN_HEIGHT)


def create_label_window() -> Demo:
    """Build a window with one label (lecture: windows and labels).

    The text is set three ways: in the constructor, through the dictionary key
    and through ``config``.

    @return The window and its ``label``.
    """
    window = _new_window(constants.WINDOW_TITLE, _default_size())
    label = tk.Label(
        window, text=constants.DEFAULT_LABEL_TEXT, font=constants.LABEL_FONT
    )
    label["text"] = "Set through a dictionary key"
    label.config(text=constants.NEW_LABEL_TEXT)
    label.pack()
    return Demo(window, {"label": label})


def create_button_entry_window() -> Demo:
    """Build a window whose button copies the entry text into the label.

    @return The window with its ``label``, ``entry`` and ``button``.
    """
    window = _new_window(constants.WINDOW_TITLE, _default_size())
    label = tk.Label(
        window, text=constants.DEFAULT_LABEL_TEXT, font=constants.LABEL_FONT
    )
    label.pack()
    entry = tk.Entry(window, width=constants.ENTRY_WIDTH)
    entry.pack()

    def button_clicked() -> None:
        label.config(text=label_text_for(entry.get()))

    button = tk.Button(window, text=constants.BUTTON_TEXT, command=button_clicked)
    button.pack()
    return Demo(window, {"label": label, "entry": entry, "button": button})


def create_widget_showcase() -> Demo:
    """Build a window with the other Tkinter widgets.

    Each widget reports its value in the ``result`` label.

    @return The window and its widgets.
    """
    window = _new_window(constants.SHOWCASE_TITLE, constants.SHOWCASE_MIN_SIZE)
    result = tk.Label(window, text="")

    def report(widget: str, value: object) -> None:
        result.config(text=describe_value(widget, value))

    tk.Label(window, text=constants.NEW_LABEL_TEXT).pack()
    entry = tk.Entry(window, width=30)
    entry.insert(tk.END, constants.ENTRY_INITIAL_TEXT)
    entry.pack()
    text = tk.Text(window, height=5, width=30)
    text.focus()
    text.insert(tk.END, constants.TEXT_INITIAL)
    text.pack()

    spin_low, spin_high = constants.SPINBOX_RANGE
    spinbox = tk.Spinbox(
        window,
        from_=spin_low,
        to=spin_high,
        width=5,
        command=lambda: report("Spinbox", spinbox.get()),
    )
    spinbox.pack()

    scale_low, scale_high = constants.SCALE_RANGE
    scale = tk.Scale(
        window,
        from_=scale_low,
        to=scale_high,
        command=lambda value: report("Scale", value),
    )
    scale.pack()

    checked_state = tk.IntVar()
    checkbutton = tk.Checkbutton(
        window,
        text="Is On?",
        variable=checked_state,
        command=lambda: report("Checkbutton", checkbutton_text(checked_state.get())),
    )
    checkbutton.pack()

    radio_state = tk.IntVar()
    radiobuttons = [
        tk.Radiobutton(
            window,
            text=f"Option{value}",
            value=value,
            variable=radio_state,
            command=lambda: report("Radiobutton", radio_state.get()),
        )
        for value in (1, 2)
    ]
    for radiobutton in radiobuttons:
        radiobutton.pack()

    listbox = tk.Listbox(window, height=4)
    for item in constants.LIST_ITEMS:
        listbox.insert(tk.END, item)

    def listbox_used(_event: object) -> None:
        selected = first_selected(
            constants.LIST_ITEMS,
            listbox.curselection(),  # type: ignore[no-untyped-call]  # typeshed lacks a return type
        )
        report("Listbox", selected)

    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()
    result.pack()
    return Demo(
        window,
        {
            "entry": entry,
            "text": text,
            "spinbox": spinbox,
            "scale": scale,
            "checkbutton": checkbutton,
            "radiobutton1": radiobuttons[0],
            "radiobutton2": radiobuttons[1],
            "listbox": listbox,
            "result": result,
        },
    )


def create_pack_layout() -> Demo:
    """Build a window laid out with ``pack`` (stacked, or by ``side``).

    @return The window and its labels.
    """
    window = _new_window(constants.WINDOW_TITLE, _default_size())
    top = tk.Label(window, text="Top (default)")
    top.pack()
    left = tk.Label(window, text="Left")
    left.pack(side=tk.LEFT)
    right = tk.Label(window, text="Right")
    right.pack(side=tk.RIGHT)
    return Demo(window, {"top": top, "left": left, "right": right})


def create_place_layout() -> Demo:
    """Build a window laid out with ``place`` (exact x and y).

    @return The window and its labels.
    """
    window = _new_window(constants.WINDOW_TITLE, _default_size())
    first = tk.Label(window, text="At the first position")
    first.place(x=constants.PLACE_FIRST[0], y=constants.PLACE_FIRST[1])
    second = tk.Label(window, text="At the second position")
    second.place(x=constants.PLACE_SECOND[0], y=constants.PLACE_SECOND[1])
    return Demo(window, {"first": first, "second": second})


def create_grid_layout() -> Demo:
    """Build the course's grid app: ``grid`` with padding.

    Only ``grid`` is used in the window, because mixing ``pack`` and ``grid``
    in one container raises an error.

    @return The window with its ``label``, ``button``, ``new_button`` and
        ``entry``.
    """
    window = _new_window(constants.WINDOW_TITLE, _default_size())
    window.config(padx=constants.WINDOW_PADDING[0], pady=constants.WINDOW_PADDING[1])
    label = tk.Label(
        window, text=constants.DEFAULT_LABEL_TEXT, font=constants.LABEL_FONT
    )
    label.config(padx=constants.LABEL_PADDING, pady=constants.LABEL_PADDING)
    label.grid(column=constants.GRID_LABEL[0], row=constants.GRID_LABEL[1])
    entry = tk.Entry(window, width=constants.ENTRY_WIDTH)
    entry.grid(column=constants.GRID_ENTRY[0], row=constants.GRID_ENTRY[1])

    def button_clicked() -> None:
        label.config(text=label_text_for(entry.get()))

    button = tk.Button(window, text=constants.BUTTON_TEXT, command=button_clicked)
    button.grid(column=constants.GRID_BUTTON[0], row=constants.GRID_BUTTON[1])
    new_button = tk.Button(window, text=constants.NEW_BUTTON_TEXT)
    new_button.grid(
        column=constants.GRID_NEW_BUTTON[0], row=constants.GRID_NEW_BUTTON[1]
    )
    return Demo(
        window,
        {"label": label, "button": button, "new_button": new_button, "entry": entry},
    )


def run(demo: Demo) -> None:
    """Open the window and listen for user input until it is closed.

    @param demo The built window.
    """
    demo.window.mainloop()
