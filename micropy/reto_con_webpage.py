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
        
        # Create a socket and bind it to a port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 80))
        s.listen(5)
        s.settimeout(0.5)

        while True:
            # Thermopar is a MAX6675 object

            # Read the temperature value
            temperature = max.readCelsius()

            # Convert the temperature to a string
            temperature_str = "{:.2f}".format(temperature)

            temp = float(temperature_str)
            activo = 0
            if temp > 30 or activo > 0:
                fan_pin.off()
                activo = 1
                if temp < 24:
                    activo = 0
            else:
                fan_pin.on()

            try:
                temperature = temp
                payload = ujson.dumps({"temperature": temperature}) 

                headers = {"Content-Type": "application/json"}
                print("Sending Payload to Server...")
                response = requests.post(server_url, headers=headers, data=payload)
                print(response.text)

            except:
                print("Error sending data to server")
            
            # Display the temperature on OLED
            oled.text("Temp: {}".format(temperature_str), 0, 20)

            # Show all data on OLED
            oled.show()

            
            # Accept connections and send temperature
            try:
                conn, addr = s.accept()
                print('Got a connection from %s' % str(addr))
                request = conn.recv(1024)
                request = str(request)

                response = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
                response += '<html><body>'
                response += '<h1>Temperature: ' + temperature_str + ' °C</h1>'
                response += '</body></html>'
                conn.send(response)
                conn.close()
            except:
                print("No connection")

            # Sleep for 5 seconds
            time.sleep(1)
