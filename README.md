# RSA-Key-Generation
## Approach:
1. Utilized Python Crypto.PublicKey package for generating the RSA key pairs using the RSA module
2. Random string of length N bytes for randomfunc parameter in RSA.generate() method is generated using API for random.org
3. Generated keys are persisted to the PEM files in the same directory for the given bits (2048 recommended)

## References:
1. [PyCrypto API](https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html)
2. [Random.org API](https://api.random.org/json-rpc/1/basic)
