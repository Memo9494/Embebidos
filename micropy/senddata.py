import urequests as requests
import machine
import time
import network
import ujson

def read_temperature():
    # Code to read temperature from the sensor
    # Replace this with your actual temperature reading code
    return 25.5  # Dummy temperature value

server_url = "http://201.159.108.218:25565"

while True:
    temperature = read_temperature()
    payload = ujson.dumps({"temperature": temperature}) 

    headers = {"Content-Type": "application/json"}
    response = requests.post(server_url, headers=headers, data=payload)

    print(response.text)

    time.sleep(5)

