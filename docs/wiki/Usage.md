# Usage

🌐 **English** · [Dansk](Usage-da) · [Bahasa Melayu](Usage-ms)

With the virtual environment active, `python -m day27 <demo>` runs one demo.

| Command | What it does |
| --- | --- |
| `python -m day27 examples` | Prints the results of `add`, `calculate`, `Car` and `describe_text` |
| `python -m day27` or `python -m day27 button` | Window whose button copies the entry text into the label |
| `python -m day27 label` | Window with one label |
| `python -m day27 widgets` | Text, spinbox, scale, checkbutton, radiobutton and listbox |
| `python -m day27 pack` / `place` / `grid` | The three layout managers |

## The assignment's functions

```python
from day27.arguments import Car, add, calculate

add(3, 5, 6, 2, 1, 7, 4, 3)  # 31, any number of arguments
calculate(2, add=3, multiply=5)  # 25
Car(make="Nissan", model="Skyline").colour  # None: a missing key is safe
```

## Button, entry and label

Type text in the entry and press **Click Me**. The label shows the text; an
empty entry shows "Button Got Clicked".

![After a click](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/button-entry-after.png)

## Widget showcase

Each widget reports its value in the label at the bottom.

![Widget showcase](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/widget-showcase.png)

## Grid layout

The course's grid app: label, two buttons and an entry placed by column and
row, with padding. One window uses one layout manager only; mixing `pack` and
`grid` raises an error.

![Grid layout](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/grid-layout.png)
