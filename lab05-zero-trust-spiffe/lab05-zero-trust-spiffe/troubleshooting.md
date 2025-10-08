### Common Issues and Fixes

| Issue | Cause | Resolution |
|--------|--------|-------------|
| 404 Not Found on SPIRE download | Old version URL removed | Use v1.13.1 musl build URL |
| 'directory must be configured' | KeyManager path missing | Add `keys_path=/opt/spire/data/agent/keys.json` |
| 'no identity issued' | Entry not registered | Create entry for service with selector |
| 'CERTIFICATE_VERIFY_FAILED' | Hostname check fails on localhost | Disable hostname verification in demo code |
