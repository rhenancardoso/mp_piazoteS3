# boot.py -- run on boot-up
import network
from lib.umqttsimple import MQTTClient
import ubinascii
import machine
import esp
import gc

# Replace the following with your WIFI Credentials
SSID = "wifi-ssid"
SSI_PASSWORD = "wifi-password"
MQTT_SERVER = '192.168.1.183'

def mqtt_config():
    #EXAMPLE IP ADDRESS
    #mqtt_server = '192.168.1.144'
    client_id = ubinascii.hexlify(machine.unique_id())
    topic_sub = b'notification'
    topic_pub = b'hello'

    last_message = 0
    message_interval = 5
    counter = 0

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSI_PASSWORD)
        while sta_if.isconnected() == False:
            pass
    print('Connection successful')
    print(sta_if.ifconfig())

if __name__ == "__main__":
    esp.osdebug(None)
    gc.collect()

    print("Connecting to your wifi...")
    do_connect()