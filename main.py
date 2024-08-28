import time
import esp32

from utils import RgbIndicator
from device import (
    LightPattern,
    temp_sensor,
    bat_mon,
    rgb_led,
    user_led,
    usb_sense,
    ap_manager,
    websk_manager,
)

READINGS_INTERVAL_MS = 3000
UPDATE_INTERVAL_MS = 100
TOLERANCE_MS = 2


def is_ap_connected() -> bool:
    """Check if any device is connected to the Access Point."""
    return ap_manager.isconnected()


def is_usb_connected() -> bool:
    """Check if usb is connected."""
    user_led.usb.value(usb_sense.value())
    return usb_sense.value()


def main():
    rgb_color = RgbIndicator.OFF
    start_time = time.ticks_ms()
    while True:
        current_tick_ms = time.ticks_ms() - start_time
        if current_tick_ms % UPDATE_INTERVAL_MS <= TOLERANCE_MS:
            if ap_manager.isconnected():
                rgb_led.set_cycle_style(LightPattern.UPNDOWN)
                if websk_manager.check_request():
                    rgb_color = RgbIndicator.REQUEST_RECEIVED
                    rgb_led.set_cycle_style(LightPattern.FIXED)
                    rgb_led.set_rgb_led(rgb_color)
                    time.sleep(1)
                else:
                    rgb_color = RgbIndicator.HOST_CONNECTED
                    rgb_led.set_cycle_style(LightPattern.UPNDOWN)

            elif is_usb_connected():
                rgb_color = RgbIndicator.USB_CONNECTED
                rgb_led.set_cycle_style(LightPattern.UPONLY)
            else:
                rgb_color = RgbIndicator.HOST_READY
                rgb_led.set_cycle_style(LightPattern.BLINK)

            rgb_led.set_rgb_led(rgb_color)

        if current_tick_ms % READINGS_INTERVAL_MS <= TOLERANCE_MS:
            print(f"ESP32 temp: {(esp32.raw_temperature()-32)/1.8:4}")
            if temp_sensor:
                print(f"Temperature: {temp_sensor.read_temperature():4}")

            if bat_mon:
                print(f"Battery Voltage: {bat_mon.read_voltage():6}")
                print(f"Battery Current: {bat_mon.read_current():6}")


if __name__ == "__main__":
    print("Initiliazing application")
    try:
        main()
    except Exception as err:
        rgb_color = RgbIndicator.ERROR
        print(f"Error Main: {err}")
