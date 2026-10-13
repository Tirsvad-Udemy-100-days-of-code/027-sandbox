# Brug

🌐 [English](Usage) · **Dansk** · [Bahasa Melayu](Usage-ms)

Når det virtuelle miljø er aktivt, kører `python -m day27 <demo>` én demo.

| Kommando | Hvad den gør |
| --- | --- |
| `python -m day27 examples` | Udskriver resultaterne af `add`, `calculate`, `Car` og `describe_text` |
| `python -m day27` eller `python -m day27 button` | Vindue, hvor knappen kopierer teksten fra indtastningsfeltet til labelen |
| `python -m day27 label` | Vindue med én label |
| `python -m day27 widgets` | Tekstfelt, spinbox, skyder, afkrydsningsfelt, radioknapper og liste |
| `python -m day27 pack` / `place` / `grid` | De tre layoutstyringer |

## Opgavens funktioner

```python
from day27.arguments import Car, add, calculate

add(3, 5, 6, 2, 1, 7, 4, 3)  # 31, vilkårligt antal argumenter
calculate(2, add=3, multiply=5)  # 25
Car(make="Nissan", model="Skyline").colour  # None: en manglende nøgle er sikker
```

## Knap, indtastningsfelt og label

Skriv tekst i indtastningsfeltet, og tryk på **Click Me**. Labelen viser
teksten; et tomt felt viser "Button Got Clicked".

![Efter et klik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/button-entry-after.png)

## Oversigt over widgets

Hver widget melder sin værdi i labelen nederst.

![Widget-oversigt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/widget-showcase.png)

## Grid-layout

Kursets grid-app: label, to knapper og et indtastningsfelt placeret efter
kolonne og række, med afstand. Ét vindue bruger kun én layoutstyring; blandes
`pack` og `grid`, opstår der en fejl.

![Grid-layout](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/raw/branch/main/docs/images/grid-layout.png)
