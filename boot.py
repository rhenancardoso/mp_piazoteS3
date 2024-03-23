import network
import time
import ntptime
from config import config

CONFIG = config()


def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.active(True)
        wlan.connect(CONFIG.wifi_ssid, CONFIG.wifi_password)

        while not wlan.isconnected():
            time.sleep(1)

    print("Connected to WiFi")
    print("IP Address:", wlan.ifconfig()[0])


def update_time_from_ntp():
    print("Updating time from NTP server...")
    try:

        def set_time():
            ntptime.settime()

        set_time()
    except OSError.errno == 116:  # ETIMEDOUT error
        time.sleep(1)
        set_time()

    print("Current time:", time.localtime())


if __name__ == "__main__":
    print("Initializig Wifi and update local time")
    connect_to_wifi()
    update_time_from_ntp()
