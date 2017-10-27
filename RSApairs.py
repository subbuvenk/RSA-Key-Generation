#!/usr/bin/python

'''
Author: Subramanian Venkateswaran
References:
    https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html
    https://api.random.org/json-rpc/1/basic
'''


import requests, json, sys
from os import chmod
from Crypto.PublicKey import RSA

# Request parameters
url = "https://api.random.org/json-rpc/1/invoke"
beta_key = "6572df18-a43b-46b5-b5c4-d313fa7cc43e"
headers = {'content-type': 'application/json'}


# Generate random strings of length given bytes
def random_string(bytes):
    data = {
        "jsonrpc": "2.0",
        "method": "generateBlobs",
        "params": {
            "apiKey": beta_key,
            "n": 1,
            "size": bytes*8,
            "format": "hex"
        },
        "id": 42
    }
    response = requests.post(url, data=json.dumps(data), headers=headers).json()
    try:
        result = response.get('result').get('random').get('data')
    except:
        print(response)
        sys.exit(1)
    return result[0].decode('hex')


# Generate public and private keys of given bits
def rsa_keys(bits):
    if bits % 256 != 0 or bits < 1024:
        print 'Error: Please enter multiples of 256 and greater than or equal 1024' \
              '\nRecommended: 2048'
        sys.exit(1)
    keys = RSA.generate(bits,randfunc=random_string)
    public_key = keys.publickey().exportKey("PEM")
    private_key = keys.exportKey("PEM")
    return private_key, public_key


# Write private and public keys to file with set permissions
def persist_rsa_key(private_key,public_key):
    with open("./private_key.pem", 'w') as file:
        chmod("./private_key.pem", 0600)
        file.write(private_key)
    with open("./public_key.pem", 'w') as file:
        file.write(public_key)


# Main function
if __name__ == '__main__':
    bits = 2048
    private_key, public_key = rsa_keys(bits)
    persist_rsa_key(private_key,public_key)
    print private_key, public_key
