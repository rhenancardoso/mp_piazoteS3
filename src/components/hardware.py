from machine import Pin, I2C
from .sonar import Sonar
import ssd1306


class Hardware:
    # Class to define hardware specs and peripherals

    i2c:I2C
    display:ssd1306.SSD1306_I2C
    sonar: Sonar

    # I2C configuration
    _DEV_BOARD_SDA = int(21)
    _DEV_BOARD_SCL = int(22)
    # OLED Display config
    _OLED_WIDTH = int(128)
    _OLED_HEIGTH = int(64)

    def __init__(self):
        self.i2c = I2C(sda=Pin(self._DEV_BOARD_SDA), scl=Pin(self._DEV_BOARD_SCL))
        self.display = ssd1306.SSD1306_I2C(self._OLED_WIDTH, self._OLED_HEIGTH, self.i2c)
        self.sonar = Sonar(self.i2c, 500)
    
    def get_sonar_distance(self) -> int:
        return self.sonar.read_distance_cm()