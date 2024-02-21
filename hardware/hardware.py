# setup hardware on the board
# TMP117: temperature sensor
# STC3100: battery fuel gauge
from machine import I2C, Pin
from hardware.temperature_sensor import TMP117

SDA_PIN = Pin(21)
SCL_PIN = Pin(22)
I2C_SPEED_HZ = 400000


class Hardware:
    """
    Hardware class for Dev Board.

    Parameters:
        TMP117: Temperature sensor [I2C]
        STC3100: Battery fuel gauge [I2C]
    """

    _i2c: I2C
    _temp_sensor: TMP117

    def __init__(self) -> None:
        self._i2c = I2C.init(SDA_PIN, SCL_PIN, I2C_SPEED_HZ)
        self._temp_sensor = TMP117(0x70)
