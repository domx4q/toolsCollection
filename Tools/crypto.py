from .basics import *

import cryptography
from cryptography.fernet import Fernet
import hashlib


def encryptBasicString(to_encrypt: str, key: str) -> str:
    f = Fernet(bytes(str(key).encode()))
    encrypted = f.encrypt(to_encrypt.encode()).decode()
    return encrypted


def decryptBasicString(to_decrypt: str, key: str) -> str:
    f = Fernet(bytes(str(key).encode()))
    decrypted = f.decrypt(bytes(to_decrypt.encode())).decode()
    return decrypted


def generateKey() -> str:
    return Fernet.generate_key().decode()


def hashString(to_hash: str, mode="sha256") -> str:
    mode = mode.lower()
    methods = {
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
        "sha224": hashlib.sha224,
        "sha384": hashlib.sha384,
        "sha1": hashlib.sha1,
        "md5": hashlib.md5
    }
    if mode not in methods:
        raise ValueError(f"Invalid mode {mode}")
    return methods[mode](to_hash.encode()).hexdigest()