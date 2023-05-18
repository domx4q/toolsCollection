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


def hashString(to_hash: str) -> str:
    return hashlib.sha256(to_hash.encode()).hexdigest()