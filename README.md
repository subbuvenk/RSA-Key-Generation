# RSA-Key-Generation
Approach:
Utilized Python Crypto.PublicKey package for generating the RSA key pairs using the RSA module
Random string of length N bytes for randomfunc parameter in RSA.generate is generated using API for random.org
Generated keys are persisted to the PEM files in the same directory for the given bits (2048 recommended)

References:
https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html
https://api.random.org/json-rpc/1/basic
