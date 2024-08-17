from machine import Pin

_I2C_SDA_PIN = Pin(21, Pin.OUT, Pin.PULL_DOWN)
_I2C_SCL_PIN = Pin(22, Pin.OUT, Pin.PULL_DOWN)
_I2C_SPEED_HZ = 400000
_NEO_PIXEL_PIN = Pin(19, Pin.OUT)
_NEO_PIXELS_N = 1
_V_BUS_PIN = Pin(27, Pin.IN)
_LED_BUS_PIN = Pin(7, Pin.OUT)
