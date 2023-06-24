"""
This is a module that contains all the cryptography tools.
"""

from .basics import *

import cryptography
from cryptography.fernet import Fernet
import hashlib


def encryptBasicString(to_encrypt: str, key: str) -> str:
    """
    Encrypts a string with a key using the Fernet algorithm

    :param to_encrypt: The string to encrypt
    :param key: The key to encrypt the string with
    :return: The encrypted string
    """
    f = Fernet(bytes(str(key).encode()))
    encrypted = f.encrypt(to_encrypt.encode()).decode()
    return encrypted


def decryptBasicString(to_decrypt: str, key: str) -> str:
    """
    Decrypts a string with a key using the Fernet algorithm

    :param to_decrypt: The encrypted string to decrypt
    :param key: The key to decrypt the string with
    :return: The decrypted string
    """
    f = Fernet(bytes(str(key).encode()))
    decrypted = f.decrypt(bytes(to_decrypt.encode())).decode()
    return decrypted


def generateKey() -> str:
    """
    Generates a key for the Fernet algorithm

    :return: The generated key
    """
    return Fernet.generate_key().decode()


def hashString(to_hash: str, mode="sha256") -> str:
    """
    Hashes a string with a given mode

    :param to_hash: The string to hash
    :param mode: The mode to hash the string with (sha256, sha512, sha224, sha384, sha1, md5)
    :raises ValueError: If the mode is invalid
    :return: The hashed string
    """
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