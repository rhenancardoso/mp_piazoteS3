import network
import machine
import time
import ntptime

from config import config
from device import rgb_led, user_led
from utils import RgbIndicator

CPU_FREQUENCY = 80_000_000
CONFIG = config()
wlan = network.WLAN(network.STA_IF)


def connect_to_wifi():
    global esp32_board, wlan

    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.active(True)
        wlan.connect(CONFIG.wifi_ssid, CONFIG.wifi_password)
        attempt = 0
        while not wlan.isconnected():
            time.sleep(1)
            attempt += 1
            if attempt > 3:
                print(f"Max attempt: {attempt}")
                break

    if wlan.isconnected():
        print("Connected to WiFi")
        print("IP Address:", wlan.ifconfig()[0])
        rgb_led.set_rgb_led(RgbIndicator.WIFI_CONNECTED)
    else:
        print("WiFi not connected")
        rgb_led.set_rgb_led(RgbIndicator.ERROR)


def update_time_from_ntp():
    print("Updating time from NTP server...")
    try:

        def set_time():
            ntptime.settime()

        set_time()
    except OSError as err:
        if hasattr(err, "errno"):
            if err.errno == 116:  # ETIMEDOUT error
                time.sleep(1)
                set_time()
        else:
            print(f"Error NTP: {err}")

    print("Current time:", time.localtime())


if __name__ == "__main__":
    print(f"CPU Freq {machine.freq()/1_000_000} MHz")
    machine.freq(CPU_FREQUENCY)
    rgb_led.set_rgb_led(RgbIndicator.INIT)
    user_led.usb.value(0)
    print("Initializing Wifi and update local time")
    try:
        connect_to_wifi()
        if wlan.isconnected():
            update_time_from_ntp()
    except OSError as err:
        print(f"Error: {err}")
