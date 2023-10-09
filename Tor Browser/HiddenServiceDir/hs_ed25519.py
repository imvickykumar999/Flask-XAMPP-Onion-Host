
# https://tor.stackexchange.com/a/23674/38956

import base64
import hashlib
import os
import pwd
import grp
from pathlib import Path


def expand_private_key(secret_key) -> bytes:
    hash = hashlib.sha512(secret_key[:32]).digest()
    hash = bytearray(hash)
    hash[0] &= 248
    hash[31] &= 127
    hash[31] |= 64
    return bytes(hash)


def onion_address_from_public_key(public_key: bytes) -> str:
    version = b"\x03"
    checksum = hashlib.sha3_256(b".onion checksum" + public_key + version).digest()[:2]
    onion_address = "{}.onion".format(
        base64.b32encode(public_key + checksum + version).decode().lower()
    )
    return onion_address


def verify_v3_onion_address(onion_address: str) -> list[bytes, bytes, bytes]:
    # v3 spec https://gitweb.torproject.org/torspec.git/plain/rend-spec-v3.txt
    try:
        decoded = base64.b32decode(onion_address.replace(".onion", "").upper())
        public_key = decoded[:32]
        checksum = decoded[32:34]
        version = decoded[34:]
        if (
            checksum
            != hashlib.sha3_256(b".onion checksum" + public_key + version).digest()[:2]
        ):
            raise ValueError
        return public_key, checksum, version
    except:
        raise ValueError("Invalid v3 onion address")


def create_hs_ed25519_secret_key_content(signing_key: bytes) -> bytes:
    return b"== ed25519v1-secret: type0 ==\x00\x00\x00" + expand_private_key(
        signing_key
    )


def create_hs_ed25519_public_key_content(public_key: bytes) -> bytes:
    assert len(public_key) == 32
    return b"== ed25519v1-public: type0 ==\x00\x00\x00" + public_key


def store_bytes_to_file(
    bytes: bytes, filename: str, uid: int = None, gid: int = None
) -> str:
    with open(filename, "wb") as binary_file:
        binary_file.write(bytes)
    if uid and gid:
        os.chown(filename, uid, gid)
    return filename


def store_string_to_file(
    string: str, filename: str, uid: int = None, gid: int = None
) -> str:
    with open(filename, "w") as file:
        file.write(string)
    if uid and gid:
        os.chown(filename, uid, gid)
    return filename


def create_hidden_service_files(
    private_key: bytes,
    public_key: bytes,
    tor_data_directory: str,
    hidden_service_dir: str,
) -> None:

    path = Path(tor_data_directory)
    parent = path.parent.absolute()
    # these are not strictly needed but takes care of the file permissions need by tor
    tor_user = parent.owner()
    tor_group = parent.group()
    uid = pwd.getpwnam(tor_user).pw_uid
    gid = grp.getgrnam(tor_group).gr_gid
    if not path.exists():
        os.mkdir(tor_data_directory)
        os.chmod(tor_data_directory, 0o700)
        os.chown(tor_data_directory, uid, gid)

    file_content_secret = create_hs_ed25519_secret_key_content(private_key)

    store_bytes_to_file(
        file_content_secret, f"{hidden_service_dir}/hs_ed25519_secret_key", uid, gid
    )

    file_content_public = create_hs_ed25519_public_key_content(public_key)
    store_bytes_to_file(
        file_content_public, f"{hidden_service_dir}/hs_ed25519_public_key", uid, gid
    )

    onion_address = onion_address_from_public_key(public_key)
    store_string_to_file(onion_address, f"{hidden_service_dir}/hostname", uid, gid)


if __name__ == "__main__":
    create_hidden_service_files(
        b"------32-bytes-private_key------",  # the ed25519 private key often includes the public key, this does not
        b"------32-bytes-public_key------",
        ".",
    )