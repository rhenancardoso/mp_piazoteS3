PROJECT_NAME := Dev-Board-Battery-ESP32-Pico

PORT = /dev/cu.usbserial-32440
MP_FIRMWARE_FILE = firmware/ESP32_GENERIC-v1.22.0.bin
COPY_MAIN_FILES = main.py boot.py config.py config.json
COPY_HARDWARE_FOLDER = dev_board
COPY_WEBSERVER_FOLDER = web_server

all:
.PHONY: erase_all deploy_upy

deploy_upy:
	echo "Flashing Micropython to connected ESP32-PICO"
	esptool.py --chip esp32 --port $(PORT)  --baud 1000000 write_flash -z 0x1000 $(MP_FIRMWARE_FILE)

erase_all:
	echo "Erase all flash sector from ESP32-PICO"
	esptool.py --chip esp32 --port $(PORT) erase_flash

copy_files:
	echo "Copying files/folders to ESP32-PICO board"
	mpremote connect $(PORT) cp -r $(COPY_HARDWARE_FOLDER) :
	mpremote connect $(PORT) cp -r $(COPY_WEBSERVER_FOLDER) :
	mpremote connect $(PORT) cp $(COPY_MAIN_FILES) :

mount_sys:
	echo "Mount current directory to board"
	mpremote connect $(PORT) mount .

repl:
	echo "Connect REPL"
	mpremote connect $(PORT) repl
