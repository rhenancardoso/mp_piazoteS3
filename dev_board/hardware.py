from machine import I2C, Pin
from dev_board.TMP117 import TMP117, TMP117_address
from dev_board.STC3100 import STC3100

I2C_SDA_PIN = Pin(21)
I2C_SCL_PIN = Pin(22)
I2C_SPEED_HZ = 400000


class Hardware:
    """Implements the Hardware of the ESP32 board"""

    _i2c: I2C
    temp_sensor: TMP117
    battery_monitor: STC3100

    def __init__(self) -> None:
        self._i2c = I2C(scl=I2C_SCL_PIN, sda=I2C_SDA_PIN, freq=I2C_SPEED_HZ)
        i2c_devices = self._i2c.scan()
        if TMP117_address in i2c_devices:
            self.temp_sensor = TMP117(i2c=self._i2c, address=TMP117_address)
        else:
            print(f"TMP117 not found in I2C bus at address: {TMP117_address}")
