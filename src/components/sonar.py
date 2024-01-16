from machine import I2C
import time

class SRF_RANGE_UNITS:
    """ SRF-XX rangefinder constants. """
    IN = b'\x50'
    CM = b'\x51'
    US = b'\x52'

class Sonar:
    _i2c: I2C
    rxb: bytearray(2)
    ADDRESS:int = 100

    def __init__(self, i2c:I2C, max_range_mm:int) -> None:
        self._i2c = i2c
        self.rxb = bytearray(2)
        # set max range to 50 cm
        self._set_max_range(max_range_mm)

    def _set_max_range(self, max_range_mm:int) -> None:
        print(f'setting range to: {max_range_mm}')
        get_value = int(max_range_mm/43) -1
        print(f'calculated value: {get_value.to_bytes(2,"big")}')
        self._i2c.writeto(self.ADDRESS, b'\x0A')

    def read_distance_cm(self) -> int:
        self._i2c.writeto(self.ADDRESS, SRF_RANGE_UNITS.CM)
        time.sleep(0.5)
        self._i2c.readfrom_into(self.ADDRESS, self.rxb)
        value = int.from_bytes(self.rxb, "big")
        print(f'Reading value: {value}')
        return value