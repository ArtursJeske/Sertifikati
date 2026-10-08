# MiniTask

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
- Logam ir virsraksts "MiniTask" un sākotnējais izmērs 400x200.

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

### PD03 — uzdevumi saglabājas starp palaišanas reizēm

- **Dati nošķirti no saskarnes.** Programmas darbības laikā uzdevumi atrodas
  Python sarakstā `self.tasks`. `QListWidget` vairs nav datu glabātuve, bet
  tikai šī saraksta attēlojums ekrānā.
- **Saskarnes atjaunošana.** Metode `update_ui()` notīra `QListWidget` un
  uzzīmē to no jauna pēc `self.tasks` satura. Dati vienmēr plūst vienā
  virzienā: `self.tasks` → `QListWidget`.
- **Saglabāšana JSON datnē.** Metode `save_tasks()` ieraksta `self.tasks`
  saturu datnē `tasks.json`, izmantojot UTF-8 kodējumu un `ensure_ascii=False`,
  tāpēc latviešu burti datnē ir salasāmi. `indent=2` padara saturu pārskatāmu.
  Saglabāšana notiek automātiski pēc katra pievienotā uzdevuma.
- **Automātiska ielāde.** Metode `load_tasks()` nolasa `tasks.json` un atjauno
  `self.tasks`. Tā tiek izsaukta `__init__` beigās, tāpēc uzdevumi parādās
  uzreiz pēc lietotnes palaišanas. Atsevišķa poga "Ielādēt" nav nepieciešama.
- **Pirmā palaišana.** Ja `tasks.json` vēl neeksistē, `load_tasks()` noķer
  `FileNotFoundError` ar `try...except` un sāk darbu ar tukšu sarakstu.
  Lietotne atveras bez kļūdas, un datne tiek izveidota brīdī, kad tiek
  saglabāts pirmais uzdevums.

## Datu plūsma

Pievienojot uzdevumu:

```
lietotāja ievade → add_task() → self.tasks → update_ui()  → QListWidget
                                           → save_tasks() → tasks.json
```

Startējot programmu:

```
tasks.json → load_tasks() → self.tasks → update_ui() → QListWidget
```

## Zināmie ierobežojumi

Uzdevumus pašlaik var tikai pievienot — dzēšana un rediģēšana vēl nav
izveidota. Dati tiek glabāti vienkāršā JSON datnē blakus programmai, tāpēc
lietotne der vienam lietotājam vienā datorā.
