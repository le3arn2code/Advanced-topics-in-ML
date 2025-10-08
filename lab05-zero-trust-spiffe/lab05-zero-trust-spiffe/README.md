# Lab 05 – Zero‑Trust Model Security in Cloud with SPIFFE

## Objective
Implement and validate a Zero‑Trust security model using SPIFFE & SPIRE for identity‑based authentication between services.

## Environment
Ubuntu 22.04 VM or EC2  
Docker + Kubernetes (Minikube optional)  
Python 3.12 for mTLS demo

## Steps
1. Install prerequisites (Docker, kubectl, Minikube).  
2. Download & configure SPIRE Server and Agent.  
3. Start SPIRE Server and Agent for trust domain `example.org`.  
4. Create SPIFFE IDs for `ml‑service` and `ml‑client`.  
5. Fetch SVID certificates and keys.  
6. Run Python mTLS demo.  
7. Verify SPIFFE URI inside certs.

Expected Output:
```
SPIFFE mTLS Server running securely on port 5000 …
✅ Connected securely using SPIFFE mTLS
```
