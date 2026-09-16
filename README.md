# Sertifikātu pārvaldnieks

Darbvirsmas lietotne, kas veidota ar Python un PySide6 (Qt).
Autors: Artūrs Jeske

## Uzstādīšana un palaišana

```
pip install -r requirements.txt
python main.py
```

## Funkcionalitāte

### PD01 — projekta pamats

- Izveidots projekta karkass ar `QMainWindow`.
- Logam ir virsraksts "Sertifikātu pārvaldnieks" un sākotnējais izmērs 400x200.

### PD02 — lietotne reaģē uz lietotāja darbībām

- **Jauna uzdevuma ievade.** Lietotājs ieraksta uzdevuma tekstu ievades laukā
  (`QLineEdit`), kurā redzams paskaidrojošs teksts "Ievadi jaunu uzdevumu...".
- **Pievienošana sarakstam.** Poga "Pievienot" (`QPushButton`) pievieno ievadīto
  tekstu uzdevumu sarakstam (`QListWidget`). Uzdevumi sarakstā parādās tādā
  secībā, kādā tie ievadīti.
- **Ievades lauka attīrīšana.** Pēc veiksmīgas pievienošanas ievades lauks tiek
  iztukšots, lai uzreiz varētu rakstīt nākamo uzdevumu.
- **Tukšu uzdevumu validācija.** Tukšs ievades lauks vai teksts, kas sastāv tikai
  no atstarpēm, sarakstā netiek pievienots. Teksta sākuma un beigu atstarpes tiek
  noņemtas ar `strip()`.
- **Elastīgs izkārtojums.** Elementi izvietoti ar izkārtojumiem, nevis fiksētām
  pikseļu koordinātām: ievades lauks un poga atrodas `QHBoxLayout` rindā, bet
  šī rinda un saraksts ir galvenajā `QVBoxLayout`. Mainot loga izmēru, elementi
  pielāgojas jaunajam izmēram.

## Zināmie ierobežojumi

Šajā versijā dati netiek saglabāti diskā. Uzdevumi eksistē tikai tik ilgi,
kamēr programma darbojas, un pēc lietotnes aizvēršanas saraksts atkal ir tukšs.
Datu saglabāšana ir plānota nākamajā attīstības solī.
