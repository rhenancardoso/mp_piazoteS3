import network
from machine import SoftI2C
from neopixel import NeoPixel
from .TMP117 import TMP117, TMP117_address
from .STC3100 import STC3100, STC3100_address
from .rgb_manager import RgbManager, LightPattern
from .constants import (
    _LED_BUS_PIN,
    _I2C_SCL_PIN,
    _I2C_SDA_PIN,
    _I2C_SPEED_HZ,
    _NEO_PIXEL_PIN,
    _NEO_PIXELS_N,
    _V_BUS_PIN,
)
from server import WebServer


class UserLed:
    def __init__(self) -> None:
        self.usb = _LED_BUS_PIN


_i2c_manager = SoftI2C(sda=_I2C_SDA_PIN, scl=_I2C_SCL_PIN, freq=_I2C_SPEED_HZ)

# System managers
ap_manager = network.WLAN(network.AP_IF)
websk_manager = WebServer()
temp_sensor = (
    TMP117(i2c=_i2c_manager) if TMP117_address in _i2c_manager.scan() else None
)
bat_mon = STC3100(i2c=_i2c_manager) if STC3100_address in _i2c_manager.scan() else None
rgb_led = RgbManager(NeoPixel(_NEO_PIXEL_PIN, _NEO_PIXELS_N), LightPattern.UPNDOWN)
user_led = UserLed()
usb_sense = _V_BUS_PIN
