import time
from boot import dev_board


if __name__ == "__main__":
    print("Initiliazing main.py")
    ind = 0
    while True:
        print(dev_board.temp_sensor.read_temperature())
        time.sleep_ms(50)
