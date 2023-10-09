
import rsa
fKey = open('hs_ed25519_public_key','rb')
# fKey = fKey.replace(b'\\n', b'\n').decode('ascii')

fkr = fKey.read()
print(fkr)

# publicKey = rsa.PublicKey.load_pkcs1(fkr)
# print(publicKey)

# --------------------------------

# import rsa

# def encrypt(message, public_key):
#     return rsa.encrypt(message.encode(), public_key)

# def decrypt(ciphertext, private_key):
#     return rsa.decrypt(ciphertext, private_key).decode()

# with open('hostname', encoding='unicode_escape') as hn:
#     message = hn.read()

# with open('hs_ed25519_public_key', encoding='unicode_escape') as pk:
#     public_key = pk.read()

# with open('hs_ed25519_secret_key', encoding='unicode_escape') as sk:
#     private_key = sk.read()

# enc = encrypt(message, public_key)
# print(enc)

# ciphertext = enc
# dec = decrypt(ciphertext, private_key)
# print(dec)

# ------------------------------------

# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
# from base64 import b64decode,b64encode

# pubkey = open('hs_ed25519_public_key', 'r', encoding='unicode_escape').read()
# msg = "Test"
# keyDER = b64decode(pubkey).encode('ascii')
# keyPub = RSA.importKey(keyDER)
# cipher = Cipher_PKCS1_v1_5.new(keyPub)
# cipher_text = cipher.encrypt(msg.encode())
# emsg = b64encode(cipher_text)
# print(emsg)
