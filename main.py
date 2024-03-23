import time
from dev_board.hardware import Hardware

esp32_board: Hardware

if __name__ == "__main__":
    print("Initiliazing hardware")
    esp32_board = Hardware()
    while True:
        print(f"Temperature {esp32_board.temp_sensor.read_temperature()} C")
        time.sleep_ms(50)
        print(f"Bat Voltage {esp32_board.battery_monitor.read_voltage()} V")
        time.sleep_ms(50)
        print(f"Bat Charge {esp32_board.battery_monitor.read_charge()} Vh")
        time.sleep_ms(50)
        print(f"Bat Current {esp32_board.battery_monitor.read_current()/1000} mA")
        time.sleep_ms(1000)
