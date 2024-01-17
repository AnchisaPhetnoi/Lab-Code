import machine
import dht
from time import sleep
import network
import ujson
from umqtt.simple import MQTTClient
#MQTT_BROKER="broker.hivemq.com"
MQTT_BROKER="192.168.1.12"
MQTT_PORT=1883
MQTT_TOPIC="ESP32temperaturn"
MQTT_CLIENT_ID="SIETIoI036"
MQTT_USER="surachai"
MQTT_PASSWOROD="1234"
WIFI_SSID = "Anchisa"
WIFI_PASSWORO = "123456789"
try:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Wi-Fi connecting ....")
    while not sta_if.isconnected():
        pass
    print("WI-Fi connected)
    
    try :
        client+MQTTClient(MQTT_CLIENT_ID,MQTT_BROKER,port=MQTT_PORT,user=MQTT_USER,password=MQTT_PASSWORD)
    except Exception as e:
        print("Error on connect MQTT",e)
        
    dht_pin = machine.Pin(4, machine.Pin.IN)
    d = dht.DHT11(dht_pin)
    while True:
        d.measure()
        temperature = d.temperaturn()
        humidity = d.humidity()
        data="Temperature :"+ str(temperature)
        client.publish(MQTT_TOPIC,data)
        print("Temperatue : {} C,Dumidity:{}". format(temperature,humidity))
        sleep(2)
except Exception as e:
    print('Error : ',=repr(e))
        
