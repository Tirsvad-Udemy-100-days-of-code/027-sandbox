# Pembangunan

🌐 [English](Development) · [Dansk](Development-da) · **Bahasa Melayu**

## Struktur

```text
src/day27/        arguments, logic, windows, constants, __main__
tests/            ujian pytest
docs/             dokumen projek, semakan, tangkapan skrin dan sumber wiki
.gitea/workflows/ integrasi berterusan
Doxyfile          konfigurasi Doxygen
pyproject.toml    konfigurasi projek dan alat
```

Pemalar berada dalam `src/day27/constants.py`. Keputusan yang tidak memerlukan
tetingkap berada dalam `src/day27/logic.py`, supaya ujian meliputinya tanpa
paparan.

## Semakan

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m mypy src tests
python -m yamllint .yamllint.yml .gitea/workflows
```

Ujian GUI dilangkau apabila tiada paparan atau `tkinter`.

## Integrasi berterusan

`.gitea/workflows/ci.yml` menjalankan semakan di atas pada Python 3.13 untuk
setiap pull request dan setiap push ke `main`.

## Dokumentasi sumber

```bash
doxygen Doxyfile
```

Buka `docs/api/html/index.html`.

## Cara projek dijalankan

Projek ini mengikut rangka kerja SQA dan QC dalam `framework/`: kes perniagaan,
analisis pihak berkepentingan, pelan projek dan tiga pencapaian, masing-masing
disemak sebelum kod ditulis. Lihat `docs/` dalam repositori.
