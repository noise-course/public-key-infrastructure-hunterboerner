import http.server, ssl

server_address = ('localhost', 4443)  # Change port as needed
handler = http.server.SimpleHTTPRequestHandler

httpd = http.server.HTTPServer(server_address, handler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', keyfile='key.pem', server_side=True)
print("Serving on https://localhost:4443...")
httpd.serve_forever()
