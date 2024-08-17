from machine import I2C
from micropython import const

TMP117_address = const(0x48)


class TMP117_cmd:
    CONFIG = const(0x01)
    MSB_CONFIG = const(0x60)
    LSB_CONFIG = const(0x01)
    RESULT = const(0x00)


class TMP117:
    """Temperature sensor device TMP117"""

    _address: int
    _i2c: I2C

    def __init__(self, i2c: I2C, address=TMP117_address) -> None:
        self._address = address
        self._i2c = i2c
        self._sensor_configuration()

    def _read_register(self, register, length=1):
        """Private function to read from given register"""
        self._i2c.writeto(self._address, bytes([register]))
        return self._i2c.readfrom(self._address, length)

    def _sensor_configuration(self) -> None:
        """Condigures TMP117 sensor"""
        # Configure the TMP117 for temperature reading
        self._i2c.writeto(
            self._address,
            bytes([TMP117_cmd.CONFIG, TMP117_cmd.MSB_CONFIG, TMP117_cmd.LSB_CONFIG]),
        )

    def read_temperature(self) -> float:
        """Reads temperature from TMP117"""
        # Read temperature from TMP1117
        raw_data = self._read_register(TMP117_cmd.RESULT, 2)

        # Convert raw data to temperature (in Celsius)
        return (raw_data[0] << 8 | raw_data[1]) * 7.8125e-3
