# ๐ irishrail ๐ฎ๐ช

<img width="772" alt="Print screen of the command `irishrail live 'dun laoghaire'`" src="https://user-images.githubusercontent.com/431892/173231379-df87b676-7093-4800-a3dd-352ef9417926.png">

๐ Irish Rail live updates in your terminal

### Install
```
$ pip install irishrail
```

### Commands
```
โฏ irishrail --help
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
โฏ irishrail live -f "grand canal dock" 

                  Grand Canal Dock
              Northbound - Southbound
โโโโโโโโโโโโโโโโโโโโคโโโโโโโโโคโโโโโโโโโโโโโโคโโโโโโโโโ
โ Destination      โ Due    โ Destination โ Due    โ
โโโโโโโโโโโโโโโโโโโโผโโโโโโโโโผโโโโโโโโโโโโโโผโโโโโโโโโข
โ Howth            โ 16 min โ Greystones  โ 13 min โ
โ Grand Canal Dock โ 24 min โ Bray        โ 27 min โ
โ Malahide         โ 32 min โ Hazelhatch  โ 28 min โ
โ Howth            โ 49 min โ Greystones  โ 47 min โ
โ Dublin Connolly  โ 62 min โ             โ        โ
โโโโโโโโโโโโโโโโโโโโงโโโโโโโโโงโโโโโโโโโโโโโโงโโโโโโโโโ
       Updated at: 2022-06-09 22:54:54.443851
                Press CTRL-C to exit
```
