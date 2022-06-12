# 🚂 irishrail 🇮🇪

<img width="772" alt="Print screen of the command `irishrail live 'dun laoghaire'`" src="https://user-images.githubusercontent.com/431892/173231379-df87b676-7093-4800-a3dd-352ef9417926.png">

🚉 Irish Rail live updates in your terminal

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
  live      Train station updates
  stations  List all stations available
```

### Bonus
Use live command with `-f` option to update timetable every couple of seconds:

```
❯ irishrail live -f "grand canal dock" 

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
