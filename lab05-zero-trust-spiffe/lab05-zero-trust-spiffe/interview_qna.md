### SPIFFE/SPIRE Interview Q&A

1. **What is SPIFFE?** A spec for secure service identity management via URIs and X.509/JWT SVIDs.  
2. **What is SPIRE?** Implementation of SPIFFE that issues and rotates SVIDs.  
3. **How does SPIRE implement Zero Trust?** By requiring every service to authenticate using dynamic identities.  
4. **What is an SVID?** SPIFFE Verifiable Identity Document (X.509 or JWT).  
5. **Why SAN URI instead of CN?** Modern PKI uses SAN URI for service identity binding.  
6. **How is mutual TLS achieved?** Both client and server present SPIFFE certificates.  
7. **What is the role of join token?** To bootstrap agent trust into the domain.  
8. **What benefits over static certs?** Automatic rotation and least‑privilege isolation.  
9. **How can this integrate with Kubernetes?** Via SPIRE Agent DaemonSet and Workload API for Pods.  
10. **What if a service is compromised?** Revoke its SVID or rotate CA; others remain unaffected.  
