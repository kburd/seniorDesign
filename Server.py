#Simple socket server using threads
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse,parse_qs

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        try:
            par = parse_qs(urlparse(self.requestline).query)
            print(par['speed'][0])
            print(par['direction'][0])

        except:
            print(end = "")

        # Send message back to client
        message = "Recieved"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('0.0.0.0', 5000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
