# Flashing Micropython to ESP32-PICO dev-board
1. in this repository, run
```
pip install esptool
```
2. then run
```
esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20231005-v1.21.0.bin
```

# Accesing the REPL
1. With `mpremote` installed, run
```
mpremote connect /dev/cu.SLAB_USBtoUART
```