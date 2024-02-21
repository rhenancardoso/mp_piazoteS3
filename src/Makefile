PROJECT_NAME := Dev-Board-Battery-ESP32-Pico

PORT = /dev/cu.usbserial-10
MP_MAIN_DIRECTORY = main.py
MP_BOOT_DIRECTORY = boot.py

all:
.PHONY: deploy_upy copy_files monitor

run_main:
	echo "Run ./main.py"
	mpremote connect $(PORT) run $(MP_MAIN_DIRECTORY)

monitor:
	echo "Access device REPL"
	mpremote connect $(PORT) repl

ls_root:
	echo "List files in device's root"
	mpremote connect $(PORT) fs ls :

copy_files:
	echo "Copying ./src/main.py and ./src/boot.py to the device"
	mpremote connect $(PORT) + cp main.py boot.py config.py config.json : + repl
