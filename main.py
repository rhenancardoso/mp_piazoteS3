import time
import esp32

from utils import RgbIndicator
from web_server.microdot import Microdot
from device import temp_sensor, bat_mon, rgb_led, user_led, usb_sense

app = Microdot()
INTERVAL_MS = 3000


@app.route("/temperature")
async def read_temperature():
    if not temp_sensor:
        return "Temperature sensor not connected", 200, {"Content-Type": "text/html"}
    return (
        f"Temperature: {temp_sensor.read_temperature()}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/battery/voltage")
async def read_battery_voltage():
    if not bat_mon:
        return "Battery monitor not connected", 200, {"Content-Type": "text/html"}
    return (
        f"Battery Voltage: {bat_mon.read_voltage()}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/battery/charge")
async def read_battery_charge():
    if not bat_mon:
        return "Battery monitor not connected", 200, {"Content-Type": "text/html"}
    return (
        f"Battery Charge: {bat_mon.read_charge()}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/battery/current")
async def read_battery_current():
    if not bat_mon:
        return "Battery monitor not connected", 200, {"Content-Type": "text/html"}
    return (
        f"Battery Current: {bat_mon.read_current()}",
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
    rgb_led.set_rgb_led(
        int(request.args["r"]), int(request.args["g"]), int(request.args["b"])
    )
    return (
        f"RGB ON => R:{int(request.args['r'])}, "
        f"G:{int(request.args['g'])}, "
        f"B:{int(request.args['b'])}",
        200,
        {"Content-Type": "text/html"},
    )


@app.route("/LedRGB/OFF")
def neopixel_OFF(request):
    rgb_led.set_rgb_led(0, 0, 0)
    return "RGB OFF", 200, {"Content-Type": "text/html"}


def is_usb_connected() -> bool:
    """Check if usb is connected."""
    user_led.usb.value(usb_sense.value())
    return usb_sense.value()


def main():
    rgb_color = RgbIndicator.OFF
    start_time = time.ticks_ms()
    while True:
        now = time.ticks_ms()
        if (now - start_time) % INTERVAL_MS <= 60:
            print(f"Time diff: {now - start_time}")
            rgb_color = RgbIndicator.RUNNING
            try:
                print(f"ESP32 temp: {(esp32.raw_temperature()-32)/1.8:4}")
                if temp_sensor:
                    print(f"Temperature: {temp_sensor.read_temperature():4}")

                if bat_mon:
                    print(f"Battery Voltage: {bat_mon.read_voltage():6}")
                    print(f"Battery Current: {bat_mon.read_current():6}")

                if is_usb_connected():
                    print("USB Connected")
                    rgb_color = RgbIndicator.USB_CONNECTED

            except Exception as err:
                rgb_color = RgbIndicator.ERROR
                print(f"Error Main: {err}")
        rgb_led.set_rgb_led(rgb_color)
        time.sleep_ms(50)


if __name__ == "__main__":
    print("Initiliazing hardware")
    # `main()` for testing only
    main()
    # app.run(debug=True, port=80)
