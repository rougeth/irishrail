# 🚂 irishrail 🇮🇪

<img width="776" alt="🚂🇮🇪" src="https://user-images.githubusercontent.com/431892/173165239-25db6a7c-a15c-4d25-ac69-150bd78a4968.png">

### Install
```
$ pip install irishrail
```

### Commands
```
❯ irishrail --help
Usage: irishrail [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  live
  stations
```

### Bonus
Use live command with `-f` option to receive updates every 30s:

```
❯ irishrail live -f -s "grand canal dock" 

                  Grand Canal Dock
              Northbound - Southbound
╔══════════════════╤════════╤═════════════╤════════╗
║ Destination      │ Due    │ Destination │ Due    ║
╟──────────────────┼────────┼─────────────┼────────╢
║ Howth            │ 16 min │ Greystones  │ 13 min ║
║ Grand Canal Dock │ 24 min │ Bray        │ 27 min ║
║ Malahide         │ 32 min │ Hazelhatch  │ 28 min ║
║ Howth            │ 49 min │ Greystones  │ 47 min ║
║ Dublin Connolly  │ 62 min │             │        ║
╚══════════════════╧════════╧═════════════╧════════╝
       Updated at: 2022-06-09 22:54:54.443851
                Press CTRL-C to exit
```
