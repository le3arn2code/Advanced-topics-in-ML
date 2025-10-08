import ssl, http.server

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Secure connection established with SPIFFE mTLS")

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='/tmp/spire-agent/api/x509svid/cert.pem',
                        keyfile='/tmp/spire-agent/api/x509svid/key.pem')
context.load_verify_locations(cafile='/tmp/spire-agent/api/x509svid/bundle.0.pem')
context.verify_mode = ssl.CERT_REQUIRED

server = http.server.HTTPServer(('0.0.0.0', 5000), Handler)
server.socket = context.wrap_socket(server.socket, server_side=True)
print("SPIFFE mTLS Server running securely on port 5000 ...")
server.serve_forever()
