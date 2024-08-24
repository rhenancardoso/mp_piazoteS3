import machine
import network

from config import config
from device import rgb_led, user_led, ap_manager
from utils import RgbIndicator

CPU_FREQUENCY = 80_000_000
CONFIG = config()


def access_point_config():
    print("Configuring access point")
    ap_manager.active(True)
    ap_manager.config(
        essid=CONFIG.ap_ssid,
        password=CONFIG.ap_password,
        channel=1,
        authmode=network.AUTH_WPA_WPA2_PSK,
    )

    while ap_manager.active() is False:
        pass

    print("Configuration successful")
    print(ap_manager.ifconfig())


if __name__ == "__main__":
    print(f"CPU Freq {machine.freq()/1_000_000} MHz")
    machine.freq(CPU_FREQUENCY)
    rgb_led.set_rgb_led(RgbIndicator.INIT)
    user_led.usb.value(0)
    access_point_config()
