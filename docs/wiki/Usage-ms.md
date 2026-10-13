# Penggunaan

🌐 [English](Usage) · [Dansk](Usage-da) · **Bahasa Melayu**

Apabila persekitaran maya aktif, `python -m day27 <demo>` menjalankan satu demo.

| Arahan | Fungsi |
| --- | --- |
| `python -m day27 examples` | Mencetak hasil `add`, `calculate`, `Car` dan `describe_text` |
| `python -m day27` atau `python -m day27 button` | Tetingkap yang butangnya menyalin teks medan input ke label |
| `python -m day27 label` | Tetingkap dengan satu label |
| `python -m day27 widgets` | Teks, spinbox, skala, kotak semak, butang radio dan senarai |
| `python -m day27 pack` / `place` / `grid` | Tiga pengurus susun atur |

## Fungsi tugasan

```python
from day27.arguments import Car, add, calculate

add(3, 5, 6, 2, 1, 7, 4, 3)  # 31, sebarang bilangan hujah
calculate(2, add=3, multiply=5)  # 25
Car(make="Nissan", model="Skyline").colour  # None: kunci yang tiada selamat dibaca
```

## Butang, medan input dan label

Taip teks dalam medan input dan tekan **Click Me**. Label memaparkan teks itu;
medan kosong memaparkan "Button Got Clicked".

![Selepas klik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/button-entry-after.png)

## Paparan widget

Setiap widget melaporkan nilainya dalam label di bahagian bawah.

![Paparan widget](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/widget-showcase.png)

## Susun atur grid

Aplikasi grid kursus: label, dua butang dan medan input diletakkan mengikut
lajur dan baris, dengan lapik. Satu tetingkap hanya menggunakan satu pengurus
susun atur; mencampurkan `pack` dan `grid` menyebabkan ralat.

![Susun atur grid](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/grid-layout.png)
