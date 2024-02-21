PROJECT_NAME := Dev-Board-Battery-ESP32-Pico

PORT = /dev/cu.usbserial-10
MP_FILE_NAME = ESP32_GENERIC-20231227-v1.22.0.bin

all:
.PHONY: erase_all deploy_upy

deploy_upy:
	echo "Flashing Micropython to connected ESP32-PICO"
	esptool.py --chip esp32 --port $(PORT)  --baud 1000000 write_flash -z 0x1000 $(MP_FILE_NAME)

erase_all:
	echo "Erase all flash sector from ESP32-PICO"
	esptool.py --chip esp32 --port $(PORT) erase_flash
