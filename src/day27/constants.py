"""Constants shared by the day 27 modules.

@file
@brief Window, label, button and entry settings. Nothing else defines them.
"""

## @brief Title of every top-level window.
WINDOW_TITLE: str = "My First GUI Program"

## @brief Minimum window width in pixels.
WINDOW_MIN_WIDTH: int = 500

## @brief Minimum window height in pixels.
WINDOW_MIN_HEIGHT: int = 300

## @brief Text the label shows when the window opens.
DEFAULT_LABEL_TEXT: str = "I Am a Label"

## @brief Font of the label: family, size in points and style.
LABEL_FONT: tuple[str, int, str] = ("Arial", 24, "bold")

## @brief Text on the button that copies the entry text into the label.
BUTTON_TEXT: str = "Click Me"

## @brief Width of the entry in characters.
ENTRY_WIDTH: int = 10
