"""Command line entry point: ``python -m day27 [demo]``.

@file
@brief Prints the ``*args`` and ``**kwargs`` examples or opens a Tkinter demo.
"""

import argparse
import sys
from collections.abc import Callable, Sequence

from day27.arguments import Car, add, calculate, describe_text

EXAMPLES = "examples"
DEMOS = ("label", "button", "widgets", "pack", "place", "grid")


def examples() -> str:
    """Build the text printed by ``python -m day27 examples``.

    @return The example calls and their results, one per line.
    """
    car = Car(make="Nissan", model="Skyline")
    centred = describe_text("Hello", align="center")
    lines = [
        f"add(3, 5, 6, 2, 1, 7, 4, 3) = {add(3, 5, 6, 2, 1, 7, 4, 3)}",
        f"calculate(2, add=3, multiply=5) = {calculate(2, add=3, multiply=5)}",
        f"Car(make='Nissan', model='Skyline').model = {car.model}",
        f"Car(make='Nissan', model='Skyline').colour = {car.colour}",
        f"describe_text('Hello') = {describe_text('Hello')}",
        f"describe_text('Hello', align='center') = {centred}",
    ]
    return "\n".join(lines) + "\n"


def open_demo(name: str) -> None:
    """Build the named Tkinter demo and open it.

    @param name One of ``DEMOS``.
    """
    from day27 import windows  # imported here so ``examples`` needs no Tkinter

    builders: dict[str, Callable[[], windows.Demo]] = {
        "label": windows.create_label_window,
        "button": windows.create_button_entry_window,
        "widgets": windows.create_widget_showcase,
        "pack": windows.create_pack_layout,
        "place": windows.create_place_layout,
        "grid": windows.create_grid_layout,
    }
    windows.run(builders[name]())


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command line.

    @param argv Arguments without the program name; ``sys.argv`` when ``None``.
    @return The process exit code.
    """
    parser = argparse.ArgumentParser(
        prog="python -m day27",
        description="Day 27 sandbox: *args, **kwargs and Tkinter demos.",
    )
    parser.add_argument(
        "demo",
        nargs="?",
        default="button",
        choices=(EXAMPLES, *DEMOS),
        help="'examples' prints the *args/**kwargs examples; the others open a "
        "window (default: button)",
    )
    args = parser.parse_args(argv)
    if args.demo == EXAMPLES:
        sys.stdout.write(examples())
    else:
        open_demo(args.demo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
