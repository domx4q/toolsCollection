from .basics import *
from . import crypto


class Manager:
    """
    This manages, handles and groups all the tools together.
    """

    __key = None

    def __init__(self):
        self.__key = crypto.generateKey()
        print("Manager is initialized")

    def __str__(self):
        return "I am the manager"

    @property
    def key(self):
        return self.__key

    def encrypt(self, to_encrypt: str) -> str:
        return crypto.encryptBasicString(to_encrypt, self.__key)

    def decrypt(self, to_decrypt: str) -> str:
        return crypto.decryptBasicString(to_decrypt, self.__key)

    def hash(self, to_hash: str) -> str:
        return crypto.hashString(to_hash)
