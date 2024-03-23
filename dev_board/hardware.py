from machine import I2C, Pin
from dev_board.TMP117 import TMP117, TMP117_address
from dev_board.STC3100 import STC3100, STC3100_address

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
        print(f"I2C devices found: {i2c_devices}")
        for device in i2c_devices:
            if device == TMP117_address:
                self.temp_sensor = TMP117(i2c=self._i2c)
            elif device == STC3100_address:
                self.battery_monitor = STC3100(i2c=self._i2c)
            else:
                print(f"Device {device} not configured")
