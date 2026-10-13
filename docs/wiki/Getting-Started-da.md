# Kom i gang

🌐 [English](Getting-Started) · **Dansk** · [Bahasa Melayu](Getting-Started-ms)

## Du skal bruge

- Python 3.13 eller nyere med `venv`, `pip` og `tkinter`.
- Doxygen, kun hvis du vil bygge kildedokumentationen.

## Opsætning

Opret et lokalt virtuelt miljø med navnet `.venv`, opgradér `pip`, og installér
derefter projektet med udviklingsværktøjerne.

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

## Kontrollér, at det virker

```bash
python -m pytest
python -m day27 examples
```

Næste: [Brug](Usage-da).
