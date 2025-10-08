# Install SPIRE v1.13.1
wget https://github.com/spiffe/spire/releases/download/v1.13.1/spire-1.13.1-linux-amd64-musl.tar.gz
tar -xvzf spire-1.13.1-linux-amd64-musl.tar.gz
sudo mv spire-1.13.1/bin/* /usr/local/bin/

# Configure server and agent
sudo mkdir -p /opt/spire/conf/{server,agent} /opt/spire/data/{server,agent}
# (server.conf and agent.conf content as per lab)

# Start server and agent
spire-server run --config /opt/spire/conf/server/server.conf &
spire-agent run --config /opt/spire/conf/agent/agent.conf -joinToken <token> &

# Register identities
spire-server entry create -spiffeID spiffe://example.org/ml-service -parentID spiffe://example.org/spire/agent/join_token/<token> -selector unix:user:toor -x509SVIDTTL 3600
spire-server entry create -spiffeID spiffe://example.org/ml-client -parentID spiffe://example.org/spire/agent/join_token/<token> -selector unix:user:toor -x509SVIDTTL 3600

# Fetch certs
spire-agent api fetch x509 -socketPath /tmp/spire-agent.sock -write /tmp/spire-agent/api/x509svid/

# Run mTLS demo
python3 ml_server.py  # terminal 1
python3 ml_client.py  # terminal 2
