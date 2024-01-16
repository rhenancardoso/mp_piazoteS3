PROJECT_NAME := OLED-Esp32

BOARD = GENERIC_S3
PORT = /dev/cu.SLAB_USBtoUART
MP_FILE_NAME = ESP32_GENERIC-20231005-v1.21.0.bin

all: 
.PHONY: deploy_upy erase_all

deploy_upy:
	echo "Flashing Micropython to connected ESP32-PICO"
	esptool.py --chip esp32 --port $(PORT)  --baud 460800 write_flash -z 0x1000 $(MP_FILE_NAME)

install_ssd1306:
	echo "Installing ssd13-6 module"
	mpremote connect $(PORT) mip install ssd1306

erase_all:
	echo "Erase all flash sector from ESP32-PICO"
	esptool.py --chip esp32 --port $(PORT) erase_flash