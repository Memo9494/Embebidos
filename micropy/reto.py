import machine
import ssd1306
import time
import max6675
import amogos
import machine
import socket
import ujson
import urequests as requests



"""
MAIN CODE FOR FINAL PROJECT

by Roy Medina


"""

class Reto():
    def __init__(self):


        # Setup OLED display
        i2c = machine.SoftI2C(scl=machine.Pin(12), sda=machine.Pin(14))
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)

        max = max6675.MAX6675(4, 5 , 16)

        fan_pin = machine.Pin(2, machine.Pin.OUT)

        server_url = "http://201.159.108.218:25565"


        while True:
            # Thermopar is a MAX6675 object

            # Read the temperature value
            temperature = max.readCelsius()

            # Format OLED Display
            oled.fill(0)
            oled.text("Mediciones: ", 0, 0)

            # Convert the temperature to a string
            temperature_str = "{:.2f}".format(temperature)

            temp = float(temperature_str)
            
            if temp > 30:
                fan_pin.off()
            else:
                fan_pin.on()
            
            temperature = temp
            payload = ujson.dumps({"temperature": temperature}) 

            headers = {"Content-Type": "application/json"}
            print("Sending Payload to Server...")
            response = requests.post(server_url, headers=headers, data=payload)

            print(response.text)


            # Display the temperature on OLED
            oled.text("Temp: {}".format(temperature_str), 0, 20)

            # Show all data on OLED
            oled.show()

            # Sleep for 5 seconds
            time.sleep(1)

            