"""Tests for the command line entry point."""

import pytest

from day27 import __main__ as cli


def test_examples_contains_expected_results() -> None:
    """The printed examples show the lecture results."""
    text = cli.examples()
    assert "= 31" in text
    assert "= 25" in text
    assert ".model = Skyline" in text
    assert ".colour = None" in text


def test_main_prints_examples_and_returns_zero(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """``examples`` writes the examples and exits with 0."""
    assert cli.main(["examples"]) == 0
    assert capsys.readouterr().out == cli.examples()


def test_main_exits_when_demo_unknown(capsys: pytest.CaptureFixture[str]) -> None:
    """An unknown demo name is rejected by argparse."""
    with pytest.raises(SystemExit):
        cli.main(["nope"])
    assert "invalid choice" in capsys.readouterr().err


def test_main_opens_button_demo_without_arguments(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """No argument opens the button demo."""
    opened: list[str] = []
    monkeypatch.setattr(cli, "open_demo", opened.append)
    assert cli.main([]) == 0
    assert opened == ["button"]
