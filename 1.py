import machine
import dht
from time import sleep

try:
    dht_pin = machine.Pin(4, machine.Pin.IN)
    dht0bject = dth.DHT11(dht_pin)
    
    while True:
        dhtObject.measure()
        temperature = dhtObject.temperature()
        humidity = dhtObject.humidity()
        print("Temperature:{} C,Humiditry:{}".format(temperature,humidity))
        sleep(2)
except Exception as e:
    print('Erro' +repr(e))
