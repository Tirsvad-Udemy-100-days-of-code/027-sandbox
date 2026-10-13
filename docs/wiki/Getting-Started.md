# Getting started

🌐 **English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

## You need

- Python 3.13 or newer with `venv`, `pip` and `tkinter`.
- Doxygen, only to build the source documentation.

## Set up

Create a local virtual environment named `.venv`, upgrade `pip`, then install
the project with its development tools.

**Windows PowerShell**

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

**Linux Debian**

```bash
sudo apt install python3 python3-venv python3-tk doxygen
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

**macOS**

```bash
brew install python@3.13 python-tk@3.13 doxygen
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Check that it works

```bash
python -m pytest
python -m day27 examples
```

Next: [Usage](Usage).
