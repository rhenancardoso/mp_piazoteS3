PROJECT_NAME := OLED-Esp32

BOARD = GENERIC_S3
PORT = /dev/cu.SLAB_USBtoUART
MP_MAIN_DIRECTORY = main.py
MP_BOOT_DIRECTORY = boot.py
MP_COMP_DIRECTORY = components/*
MP_LIB_DIRECTORY = lib/*

all: 
.PHONY: deploy_upy copy_files monitor copy_lib copy_comp

run_main:
	echo "Run ./main.py"
	mpremote connect $(PORT) run $(MP_MAIN_DIRECTORY)

monitor:
	echo "Access device REPL"
	mpremote connect $(PORT) repl

ls_root:
	echo "List files in device's root"
	mpremote connect $(PORT) fs ls :

copy_lib: 
	echo "Copying ./src/lib to the device"
	mpremote connect $(PORT) cp -r $(MP_LIB_DIRECTORY) :

copy_comp: 
	echo "Copying ./src/components to the device"
	mpremote connect $(PORT) cp -r $(MP_COMP_DIRECTORY) :

copy_files: copy_lib copy_comp
	echo "Copying ./src/main.py and ./src/boot.py to the device"
	mpremote connect $(PORT) cp $(MP_MAIN_DIRECTORY) :
	mpremote connect $(PORT) cp $(MP_BOOT_DIRECTORY) :