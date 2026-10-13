"""Variable-length and default arguments from the day 27 lectures.

@file
@brief ``add(*args)``, ``calculate(n, **kwargs)``, ``Car(**kw)`` and a writer
with default argument values. Contains no Tkinter code.
"""

from day27 import constants


def add(*args: float) -> float:
    """Add any number of positional arguments.

    @param args The numbers to add, collected in a tuple.
    @return The sum; 0 when no number is given.
    """
    total: float = 0
    for number in args:
        total += number
    return total


def calculate(n: float, **kwargs: float) -> float:
    """Add and multiply a number by keyword arguments.

    The lecture solution reads ``kwargs["add"]`` and ``kwargs["multiply"]``.
    A missing key is read with ``dict.get`` and its neutral value, so
    ``calculate(2)`` returns 2.

    @param n The starting number.
    @param kwargs ``add`` (default 0) is added first, then the result is
        multiplied by ``multiply`` (default 1).
    @return The calculated number.
    """
    n += kwargs.get("add", 0)
    n *= kwargs.get("multiply", 1)
    return n


class Car:
    """A car described by optional keyword arguments.

    @brief Reads its attributes with ``dict.get``, so a missing key is ``None``
    instead of an error.
    """

    def __init__(self, **kw: str | int) -> None:
        """Create a car.

        @param kw Any of ``make``, ``model``, ``colour`` and ``seats``.
        """
        self.make: str | int | None = kw.get("make")
        self.model: str | int | None = kw.get("model")
        self.colour: str | int | None = kw.get("colour")
        self.seats: str | int | None = kw.get("seats")


def describe_text(
    text: str,
    move: bool = constants.DEFAULT_MOVE,
    align: str = constants.DEFAULT_ALIGN,
    font: tuple[str, int, str] = constants.DEFAULT_FONT,
) -> str:
    """Describe how a text would be written, like ``turtle.write``.

    Only ``text`` is required; the others have default values the caller may
    omit or override by keyword.

    @param text The text to write (required).
    @param move Whether the pen moves to the end of the text.
    @param align ``left``, ``center`` or ``right``.
    @param font Font family, size and style.
    @return A one-line description of the call.
    """
    family, size, style = font
    return f"{text!r}: move={move}, align={align}, font={family} {size} {style}"
