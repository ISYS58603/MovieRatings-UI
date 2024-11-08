# This file gives a little bit more control over starting the web server locally 
# you can also run this with a bit less control by typing `python -m http.server 8090`
# This will start a web server on port 8090 and serve files from the current directory.

import http.server
import socketserver

PORT = 8090  # You can change this port if needed

# SimpleHTTPRequestHandler is the same handler used by `python -m http.server`
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
