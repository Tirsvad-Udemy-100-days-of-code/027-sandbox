"""Constants shared by the day 27 modules.

@file
@brief Window, widget, layout and default-argument settings. Nothing else defines them.
"""

## @brief Title of the label, button and layout windows.
WINDOW_TITLE: str = "My First GUI Program"

## @brief Title of the widget showcase window.
SHOWCASE_TITLE: str = "Widget Examples"

## @brief Minimum window width in pixels.
WINDOW_MIN_WIDTH: int = 500

## @brief Minimum window height in pixels.
WINDOW_MIN_HEIGHT: int = 300

## @brief Minimum width and height of the widget showcase window in pixels.
SHOWCASE_MIN_SIZE: tuple[int, int] = (500, 500)

## @brief Text the label shows when the window opens.
DEFAULT_LABEL_TEXT: str = "I Am a Label"

## @brief Text the label shows after its text was set once.
NEW_LABEL_TEXT: str = "New Text"

## @brief Text the label shows when the entry is empty on a button click.
BUTTON_CLICKED_TEXT: str = "Button Got Clicked"

## @brief Font of the label: family, size in points and style.
LABEL_FONT: tuple[str, int, str] = ("Arial", 24, "bold")

## @brief Text on the button that copies the entry text into the label.
BUTTON_TEXT: str = "Click Me"

## @brief Text on the second button of the grid layout.
NEW_BUTTON_TEXT: str = "New Button"

## @brief Width of the entry in characters.
ENTRY_WIDTH: int = 10

## @brief Horizontal and vertical padding around the grid layout window in pixels.
WINDOW_PADDING: tuple[int, int] = (100, 200)

## @brief Padding around the label of the grid layout in pixels.
LABEL_PADDING: int = 50

## @brief Column and row of the label in the grid layout.
GRID_LABEL: tuple[int, int] = (0, 0)

## @brief Column and row of the button in the grid layout.
GRID_BUTTON: tuple[int, int] = (1, 1)

## @brief Column and row of the second button in the grid layout.
GRID_NEW_BUTTON: tuple[int, int] = (2, 0)

## @brief Column and row of the entry in the grid layout.
GRID_ENTRY: tuple[int, int] = (3, 2)

## @brief X and Y of the first label in the place layout.
PLACE_FIRST: tuple[int, int] = (0, 0)

## @brief X and Y of the second label in the place layout.
PLACE_SECOND: tuple[int, int] = (100, 200)

## @brief Initial text of the widget showcase entry.
ENTRY_INITIAL_TEXT: str = "Some text to begin with."

## @brief Initial text of the widget showcase text box.
TEXT_INITIAL: str = "Example of multi-line text entry."

## @brief Smallest and largest value of the spinbox.
SPINBOX_RANGE: tuple[int, int] = (0, 10)

## @brief Smallest and largest value of the scale.
SCALE_RANGE: tuple[int, int] = (0, 100)

## @brief Items of the listbox.
LIST_ITEMS: tuple[str, ...] = ("Apple", "Pear", "Orange", "Banana")

## @brief Default values of the optional arguments of the text writer.
DEFAULT_MOVE: bool = False

## @brief Default alignment of the text writer.
DEFAULT_ALIGN: str = "left"

## @brief Default font of the text writer: family, size and style.
DEFAULT_FONT: tuple[str, int, str] = ("Arial", 8, "normal")
