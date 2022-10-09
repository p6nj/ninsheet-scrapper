# Web Scripts
## Intro
This repo is for miscellaneous web crawlers, for now it's used to store scripts to download sheet music on <a href='https://www.ninsheetmusic.org/'>NinSheetMusic.org</a> and sort them.
The NSM-downloader is entirely functionnal and the sorter will take no time.

I may also optimise the downloader to add a real GUI and download the whole website.

## Downloader
### Principle
The purpose of this downloader is to get every sheet music from one of the videogame series of the website.
Providing a serie name in the URL format (`SuperMario`, `Kirby`...) in argument will download all sheets from the serie, from all its games, with the correct names and file structure.
**You will need to provide the path to your sheet music root folder in the variable `SheetPath`, the first variable in the script (first line).** Mine is `Documents/sheet music/ninsh/`. Note that the final `/` doesn't matter.

```
NinSheetMusic Downloader
usage:
    NSM-downloader [SERIE]
where SERIE is the serie name, like SuperMario, Megaman...
You can find these names in the end of the serie page  URL.
```
### Example
If you type `python3 NSM-downloader SuperMario`, you will get this file structure in your sheet music root folder:
```
├── Super Mario
│   ├── Captain Toad: Treasure Tracker
│   │   └── Retro Ramp-Up.pdf
│   ├── Dr. Mario
│   │   ├── Chill.pdf
│   │   ├── Fever.pdf
│   │   ├── Title Screen.pdf
│   │   └── VS Game Over.pdf
│   ├── Hotel Mario
│   │   └── Main Menu-Map.pdf
│   ├── Luigi's Mansion
│   │   ├── Bogmire Battle.pdf
│   │   ├── Boss Room After Victory.pdf
│   │   ├── Credits.pdf
│   │   ├── Dancing Shy Guy Ghosts.pdf
│   │   ├── Game Boy Horror.pdf
│   │   ├── Main Theme.pdf
│   │   ├── Melody Pianissima Collection.pdf
│   │   ├── Outside.pdf
│   │   ├── Playing Mini-Games With Ghosts.pdf
│   │   ├── Professor E. Gadd's Laboratory.pdf
│   │   ├── Stage Clear.pdf
│   │   ├── Talking with Ghosts.pdf
│   │   └── Toad's Theme.pdf
│   ├── Luigi's Mansion 3
│   │   ├── B2: Boilerworks.pdf
│   │   └── Main Theme.pdf
│   ├── Luigi's Mansion: Dark Moon
│   │   ├── Catching Ghosts 3.pdf
│   │   ├── Ghostly Piano.pdf
│   │   ├── Gloomy Manor.pdf
│   │   ├── Scarescraper.pdf
│   │   ├── Secret Mine.pdf
│   │   ├── Sticky Situation.pdf
│   │   └── Title Theme.pdf
...
```

## Sorter
### Intro
This sorter isn't ready for now.
It will parse all your PDF files and sort them using their tempo.
The result will probably be written in a text file.