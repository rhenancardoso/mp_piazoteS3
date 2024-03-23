from machine import I2C
from micropython import const

STC3100_address = const(0x70)


class STC3100_cmd:
    CHARGE_L = const(0x02)
    CHARGE_H = const(0x03)
    CURRENT_L = const(0x06)
    CURRENT_H = const(0x07)
    VOLTAGE_L = const(0x08)
    VOLTAGE_H = const(0x09)


class STC3100:
    """Battery fuel gauge and monitoring device"""

    _address: int
    _i2c: I2C

    def __init__(self, i2c: I2C, address=STC3100_address) -> None:
        self._address = address
        self._i2c = i2c

    def _read_registers(self, registers, length=1):
        """Private function to read from given register"""
        # Values held in consecutive registers must be read
        # with a single I2C access to ensure data integrity
        self._i2c.writeto(self._address, bytes(registers))
        return self._i2c.readfrom(self._address, length)

    def read_charge(self) -> float:
        """Reads gas gauge charge register"""
        raw_data = self._read_registers([STC3100_cmd.CHARGE_L, STC3100_cmd.CHARGE_H], 2)
        raw_charge = raw_data[1] << 8 | raw_data[0]
        return raw_charge * 2.44  # LSB value is 6.70uVh

    def read_voltage(self) -> float:
        """Reads gas gauge voltage register"""
        raw_data = self._read_registers(
            [STC3100_cmd.VOLTAGE_L, STC3100_cmd.VOLTAGE_H], 2
        )
        raw_voltage = raw_data[1] << 8 | raw_data[0]
        return raw_voltage * 1.17e-3  # LSB value is 2.44mV

    def read_current(self) -> float:
        """Reads gas gauge current register"""
        raw_data = self._read_registers(
            [STC3100_cmd.CURRENT_L, STC3100_cmd.CURRENT_H], 2
        )
        raw_current = raw_data[1] << 8 | raw_data[0]
        return raw_current * 11.77e-3  # LSB value is 11.77uV => but I gues there
        # is a typo on the datasheet, and it should
        # be 11.77uAd
