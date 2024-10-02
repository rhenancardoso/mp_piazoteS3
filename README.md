# Mycropython for ESP32-PICO

## Flashing Micropython to ESP32-PICO dev-board
### Using MAKE
1. First update `PORT` in the Makefile in the root directory, then run
```
make flash_upy
```

## Copying micropython files
In root directory
1. To copy files `main.py`, `boot.py` and `config.json` run
```
make copy_main
```
2. To copy remaining directories run
```
make copy_rest
```

## Accesing the REPL
1. With `mpremote` installed, run
```
make repl
```

## Erasing FLASH
1. First update `PORT` in the Makefile in the root directory, then run
```
make erase
```

# Contributing
## pre-commit
1. When copying this repository run
```
pre-commit install
```
