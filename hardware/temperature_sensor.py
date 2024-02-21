from machine import I2C

READ_TEMP_BYTES = 8


class TMP117:

    address: str

    def __init__(self, address: str) -> None:
        self.address = address

    def read_temperature(self, i2c: I2C) -> float:
        return i2c.readfrom(self.address, READ_TEMP_BYTES)
