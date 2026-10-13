# Bermula

🌐 [English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

## Anda perlukan

- Python 3.13 atau lebih baharu dengan `venv`, `pip` dan `tkinter`.
- Doxygen, hanya jika anda mahu membina dokumentasi sumber.

## Persediaan

Cipta persekitaran maya setempat bernama `.venv`, naik taraf `pip`, kemudian
pasang projek bersama alat pembangunan.

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

## Sahkan ia berfungsi

```bash
python -m pytest
python -m day27 examples
```

Seterusnya: [Penggunaan](Usage-ms).
