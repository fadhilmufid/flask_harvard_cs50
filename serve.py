from http.server import BaseHTTPRequestHandler, HTTPServer
from xmlrpc.client import Server

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers();

        self.wfile.write(b"<!DOCTYPE html>")
        self.wfile.write(b"<html lang= en>")
        self.wfile.write(b"<head>")
        self.wfile.write(b"<title> hello, title</title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"hello, world")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")

port = 8080
server_adress = ("0.0.0.0", port)
httpd = HTTPServer(server_adress, HTTPServer_RequestHandler)

httpd.serve_forever
