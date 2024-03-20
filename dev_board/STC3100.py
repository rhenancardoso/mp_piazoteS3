from machine import I2C


class STC3100_cmd:
    CHARGE_L = 0x02
    CHARGE_H = 0x03
    CURRENT_L = 0x06
    CURRENT_M = 0x07
    VOLTAGE_L = 0x08
    VOLTAGE_M = 0x09


class STC3100:
    """Battery fuel gauge and monitoring device"""

    _address: int
    _i2c: I2C

    def __init__(self, i2c: I2C, address=0x70) -> None:
        self._address = address
        self._i2c = i2c

    def read_charge(self) -> float:
        """Reads gas gauge charge register"""
        # Send TMP117 cmd for temperature reading
        self._i2c.writeto(
            self._address, bytes([STC3100_cmd.CHARGE_L, STC3100_cmd.CHARGE_H])
        )

        # Read response data (2 bytes)
        raw_data = self._i2c.readfrom(self._address, 2)
        gas_gauge_raw = raw_data[0] << 8 | raw_data[1]

        return gas_gauge_raw
