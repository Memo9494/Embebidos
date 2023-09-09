from SensorDHT import SensorDHT  # Asegúrate de que el archivo se llama mi_modulo.py
import time
from time import sleep
import ssd1306
sensor = SensorDHT("Xiaomi 12", "memo121255")

while True:
    real_temperature = sensor.get_temperature()
    estimated_temperature = sensor.update_estimated_temperature()
    if real_temperature is not None:
        print("Temperatura Real:", real_temperature)
    if estimated_temperature is not None:
        print("Temperatura Estimada:", estimated_temperature)

    sensor.lcd_str("Temperatura Real",0,0)
    sensor.lcd_str(str(real_temperature),0,1)
    sensor.lcd_str("Temperatura Estimada:",0,2)
    sensor.lcd_str("29",0,3)

    sleep(2)