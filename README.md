# Flashing Micropython to ESP32-PICO dev-board
1. in this repository, run
```
pip install esptool
```
2. then run
```
esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20231005-v1.21.0.bin
```

## Using MAKE
1. First update `PORT` in the Makefile in the root directory, then run
```
make deploy_upy
```

# Copying micropython files
In the `./src` directory
1. To copy files `main.py` and `boot.py` run
```
make copy_files
```
2. To copy files under `./components` directory run
```
make copy_comp
```
3. To copy files under `./lib` directory run
```
make copy_lib
```

# Running `main.py`
1. Run
```
make run_main
```

# Accesing the REPL
1. With `mpremote` installed, run
```
mpremote connect /dev/cu.SLAB_USBtoUART
```
OR
```
make monitor
```

# Erasing FLASH
1. First update `PORT` in the Makefile in the root directory, then run
```
make erase_all
```