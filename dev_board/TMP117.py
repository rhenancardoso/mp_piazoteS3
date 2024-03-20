from machine import I2C

TMP117_address = 0x48


class TMP117_cmd:
    CONFIG = 0x01
    MSB_CONFIG = 0x60
    LSB_CONFIG = 0x01
    RESULT = 0x00


class TMP117:
    """Temperature sensor device TMP117"""

    _address: int
    _i2c: I2C

    def __init__(self, i2c: I2C, address=TMP117_address) -> None:
        self._address = address
        self._i2c = i2c
        self._sensor_configuration()

    def _sensor_configuration(self) -> None:
        """Condigures TMP117 sensor"""
        # Configure the TMP117 for temperature reading
        self._i2c.writeto(
            self._address,
            bytes([TMP117_cmd.CONFIG, TMP117_cmd.MSB_CONFIG, TMP117_cmd.LSB_CONFIG]),
        )

    def read_temperature(self) -> float:
        """Reads temperature from TMP117"""
        # Send TMP117 cmd for temperature reading
        self._i2c.writeto(self._address, bytes([TMP117_cmd.RESULT]))

        # Read temperature data (2 bytes)
        raw_data = self._i2c.readfrom(self._address, 2)

        # Convert raw data to temperature (in Celsius)
        temperature_raw = raw_data[0] << 8 | raw_data[1]
        return temperature_raw / 256.0
