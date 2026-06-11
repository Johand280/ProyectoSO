import http.server
import socketserver

PORT = 5000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hola desde el Backend con Python (Puerto 5000)")

print(f"Servidor corriendo en el puerto {PORT}")
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    httpd.serve_forever()
