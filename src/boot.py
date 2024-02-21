from machine import Pin
from hardware.hardware import Hardware
from time import sleep_ms

board_led = Pin(20, Pin.OUT)


def blick_led():
    print("Blinking LED")
    for ind in range(5):
        board_led.value(0)
        sleep_ms(250)
        board_led.value(1)
        sleep_ms(250)


if __name__ == "__main__":
    print("Initializig boot.py file")
    dev_board = Hardware()
    print(dev_board.read_temperature)
    blick_led()
