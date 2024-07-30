from dev_board.hardware import Hardware
from web_server.microdot import Microdot
import time
import esp32

esp32_board: Hardware
app = Microdot()


@app.route("/temperature")
async def read_temperature():
    if not esp32_board.temp_sensor:
        return "Temperature sensor not connected", 200, {"Content-Type": "text/html"}
    return (
        f"Temperature: {esp32_board.temp_sensor.read_temperature()}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/battery/voltage")
async def read_battery_voltage():
    if not esp32_board.battery_monitor:
        return "Battery monitor not connected", 200, {"Content-Type": "text/html"}
    return (
        f"Battery Voltage: {esp32_board.battery_monitor.read_voltage()}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/battery/charge")
async def read_battery_charge():
    if not esp32_board.battery_monitor:
        return "Battery monitor not connected", 200, {"Content-Type": "text/html"}
    return (
        f"Battery Charge: {esp32_board.battery_monitor.read_charge()}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/battery/current")
async def read_battery_current():
    if not esp32_board.battery_monitor:
        return "Battery monitor not connected", 200, {"Content-Type": "text/html"}
    return (
        f"Battery Current: {esp32_board.battery_monitor.read_current()}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/shutdown")
async def shutdown(request):
    request.app.shutdown()
    return "The server is shutting down..."


@app.route("/LedRGB/rgb")
def neopixel_ON(request):
    # http://localhost/rgb?r=<int>&g=<int>&b=<int>
    esp32_board.set_rgb_led(
        int(request.args["r"]), int(request.args["g"]), int(request.args["b"])
    )
    return (
        f"RGB ON => R:{int(request.args['r'])}, "
        f"G:{int(request.args['g'])}, "
        f"B{int(request.args['b'])}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/LedRGB/OFF")
def neopixel_OFF(request):
    esp32_board.set_rgb_led(0, 0, 0)
    return "RGB OFF", 200, {"Content-Type": "text/html"}


def main():
    while True:
        R, G, B = 0
        try:
            print(f"ESP32 temp: {(esp32.raw_temperature()-32)/1.8:4}")
            print(f"Temperature: {esp32_board.temp_sensor.read_temperature():4}")
            print(f"Battery Voltage: {esp32_board.battery_monitor.read_voltage():6}")
            print(f"Battery Current: {esp32_board.battery_monitor.read_current():6}")
            print("Setting RGB led\n")
            esp32_board.set_rgb_led(R, G, B)
        except Exception as err:
            print(f"Error: {err}")

        R = 0 if R > 255 else R + 2
        B = 0 if B > 255 else B + 5
        G = 0 if G > 255 else G + 10
        time.sleep(1)


if __name__ == "__main__":
    print("Initiliazing hardware")
    esp32_board = Hardware()
    # `main()` for testing only
    # main()
    app.run(debug=True, port=80)
