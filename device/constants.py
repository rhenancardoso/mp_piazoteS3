from machine import Pin
from board import I2C_SDA, I2C_SCL, NEO_PIN

_I2C_SDA_PIN = Pin(I2C_SDA, Pin.OUT, Pin.PULL_DOWN)
_I2C_SCL_PIN = Pin(I2C_SCL, Pin.OUT, Pin.PULL_DOWN)
_I2C_SPEED_HZ = 400000
_NEO_PIXEL_PIN = Pin(NEO_PIN, Pin.OUT)
_NEO_PIXELS_N = 1
_V_BUS_PIN = Pin(27, Pin.IN)
_LED_BUS_PIN = Pin(7, Pin.OUT)
