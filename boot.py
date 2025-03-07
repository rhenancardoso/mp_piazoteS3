import machine
import network

import secret
from config import config
from device import rgb_led, ap_manager
from utils import RgbIndicator

CPU_FREQUENCY = 80_000_000
CONFIG = config()


def access_point_config():
    print("Configuring access point")
    ap_manager.active(True)
    ap_manager.config(
        essid=secret.AP_SSID,
        password=secret.AP_PASS,
        channel=1,
        authmode=network.AUTH_WPA_WPA2_PSK,
    )

    while ap_manager.active() is False:
        pass

    print("Configuration successful")
    print(ap_manager.ifconfig())


if __name__ == "__main__":
    print(f"CPU Freq {machine.freq()/1_000_000} MHz")
    if not machine.freq() == CPU_FREQUENCY:
        machine.freq(CPU_FREQUENCY)
    rgb_led.set_rgb_led(RgbIndicator.INIT)
    access_point_config()
