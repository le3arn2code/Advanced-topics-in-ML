import ssl, socket

host = 'localhost'
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.load_cert_chain(certfile='/tmp/spire-agent/api/x509svid-client/cert.pem',
                        keyfile='/tmp/spire-agent/api/x509svid-client/key.pem')
context.load_verify_locations(cafile='/tmp/spire-agent/api/x509svid-client/bundle.0.pem')

with socket.create_connection((host, 5000)) as sock:
    with context.wrap_socket(sock, server_hostname=host) as ssock:
        print("✅ Connected securely using SPIFFE mTLS")
        data = ssock.recv(1024)
        print("Received:", data.decode())
