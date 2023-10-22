
import hashlib
import base64
import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def get_rsa_key():
    return rsa.generate_private_key(
        public_exponent = 0x10001, 
        key_size = 0x400, 
        backend = default_backend()
    )

def find_onion(public_bytes):
    public_key_bytes = bytearray(base64.b64decode(public_bytes))
    sha_1 = hashlib.sha1()
    sha_1.update(public_key_bytes)
    digest = sha_1.digest()
    b32 = base64.b32encode(digest).decode('utf-8')
    return str(b32[:16].lower()) + '.onion'

def get_public_part(private_key):
    public_key = private_key.public_key()
    public_bytes = public_key.public_bytes(
        encoding = serialization.Encoding.PEM, 
        format = serialization.PublicFormat.PKCS1
    ).decode('utf-8')
    return ''.join(public_bytes.splitlines()[1:-1])

def match(desired, onion):
    return onion.startswith(desired)

def get_private_key_str(private_key):
    pem = private_key.private_bytes(
        encoding = serialization.Encoding.PEM, 
        format = serialization.PrivateFormat.TraditionalOpenSSL, 
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem.decode('utf-8')

def print_info(*argv):
    for a in argv:
        print(a)

def write_text_to_file(path, text):
    with open(path, 'w+') as text_file:
        text_file.write(text)

def run(desired):
    while True:
        private_key = get_rsa_key()
        public_part = get_public_part(private_key)
        onion = find_onion(public_part)

        print(onion) # f62bhf7t7hpscwcm.onion
        if match(desired, onion):
            key_str = get_private_key_str(private_key)
            write_text_to_file('hidden_service/private_key', key_str)
            print_info(onion)
            break

if __name__ == '__main__':
    desired = sys.argv[1]
    run(desired)

# >>> python termux.py f62bhf7t7hpscwcm.onion
