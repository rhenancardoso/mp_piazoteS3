from umqtt.simple import MQTTClient
import machine
import utime
import ubinascii
import time
import esp32
from boot import CONFIG, event_led_indication, water_event

mqtt_client: MQTTClient

CLIENT_ID = ubinascii.hexlify(machine.unique_id())
BASE_TOPIC = "/palm-plant"
NEW_EVENT_GAP_DAYS = 15
NEW_EVENT_EPOCH_SEC = 60 * 60 * 24 * NEW_EVENT_GAP_DAYS


# Connect to MQTT broker
def connect_to_mqtt():
    client = MQTTClient(
        CLIENT_ID,
        CONFIG.mqtt_broker_addr,
        user=CONFIG.mqtt_user,
        password=CONFIG.mqtt_user_password,
    )

    print("Connecting to MQTT broker...")
    client.connect()
    print("Connected to MQTT broker")
    return client


def publish_to_mqtt(topic, msg):
    print(f"Publishing :: {msg}\nto ::{BASE_TOPIC + topic}")
    mqtt_client.publish(BASE_TOPIC + topic, msg)


def calculate_watering_date() -> str:
    print("Calculating new watering event")
    new_event_date = time.localtime(utime.time() + NEW_EVENT_EPOCH_SEC)
    print(f"New date's event: {new_event_date}")
    return new_event_date


def trigger_event():
    print("Water event button pressed")
    publish_to_mqtt("/water-event", calculate_watering_date())
    # LED should be ON at the boot start
    event_led_indication.value(1)
    time.sleep(3)
    event_led_indication.value(0)


if __name__ == "__main__":
    print("Initiliazing main.py")
    mqtt_client = connect_to_mqtt()
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print("woke up from a light sleep")
        trigger_event()

    print("configuring light sleep")
    esp32.wake_on_ext0(pin=water_event, level=esp32.WAKEUP_ANY_HIGH)
    while True:
        # print("Going to light sleep mode ...")
        # machine.deepsleep()
        if water_event.value() == 0:
            trigger_event()
        time.sleep_ms(50)
