import Adafruit_DHT as dht
import time
import config

DHT_SENSOR = dht.DHT11
DHT_PIN = config.DHT_PIN
MAX_RETRY = 10
def read_dht():
    humidity = None
    temperature = None
    num_retry = 0
    while (humidity is None or temperature is None) and num_retry < MAX_RETRY:
        time.sleep(3)
        num_retry += 1
        humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
        
    if humidity is not None and temperature is not None:
        print("Humidity: {0:0.1f}%\tTemperature: {1:0.1f}C\tRetries: {2}".format(humidity, temperature, num_retry))
        return humidity, temperature
    else:
        raise IOError("Failed to read humidity or temperature from DHT sensor module.")

read_dht()