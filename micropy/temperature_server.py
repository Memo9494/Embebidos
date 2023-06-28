from http.server import BaseHTTPRequestHandler, HTTPServer
import json

"""
TEMPERATURE SERVER RECEIVES JSON DATA FROM THE ESP32,
AND THEN PRINTS THE TEMPERATURE READING AND SAVES IT AS A CSV FILE


by Roy Medina
"""


class TemperatureRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body.decode('utf-8'))
        temperature = data.get('temperature')
        print(f"Received temperature reading: {temperature}")

        # Process the temperature reading as needed

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Temperature reading received")

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, TemperatureRequestHandler)
    print(f"Server started on port {port}")
    httpd.serve_forever()

# Replace PORT with the desired port number, e.g., 8080
PORT = 25565

# Start the server
run_server(PORT)

