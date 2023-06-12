import machine
import ssd1306
import time
import max6675
import amogos
import machine
import socket

class Reto():
    def __init__(self):
        i2c = machine.SoftI2C(scl=machine.Pin(18), sda=machine.Pin(19))
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)

        pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]
        html = """<!DOCTYPE html>
        <html>
            <head> <title>ESP8266 Pins</title> </head>
            <body> <h1>ESP8266 Pins</h1>
                <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
            </body>
        </html>
        """

        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.bind(addr)
        s.listen(1)
        print('listening on', addr)
        while True:

            max = max6675.MAX6675(17, 16 , 27)

            print("Temperature: {}".format(max.readCelsius()))

            # Clear the OLED display
            oled.fill(0)
            oled.text("Mediciones: ", 0, 0)

            # Display the signal value on the OLED display
            oled.text("Temp: {}".format(max.readCelsius()), 0, 20)

            # Read and print analog value from pin 2
            # set pin 2 to analog input mode
            adc = machine.ADC(machine.Pin(2))
            oled.text("ADC: {}".format(adc.read()), 0, 30)
            print("ADC: {}".format(adc.read()))

            oled.show()
            # amogos.Amogos(oled, -30, 0)
            # amogos.Amogos(oled, 30, 0)
            # cl, addr = s.accept()
            # print('client connected from', addr)
            # cl_file = cl.makefile('rwb', 0)
            # while True:
            #     line = cl_file.readline()
            #     if not line or line == b'\r\n':
            #         break
            # rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
            # response = html % '\n'.join(rows)
            # cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            # cl.send(response)
            # cl.close()
            time.sleep(1)
            
            

        
        
        

