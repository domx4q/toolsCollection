import cryptography.fernet
from fastapi import APIRouter, HTTPException
from fastapi.utils import *
import sys

sys.path.append("..")  # not ../.., because this file is imported from server.py, which is one level up
from Tools import crypto

router = APIRouter()


@router.get("/encrypt")
def encrypt(text: str, key: Optional[str] = None) -> Dict[str, str]:
    """
    Encrypts a string with a key.\n
    :param text: The string to encrypt\n
    :param key: [Optional] The key to encrypt with. If not provided, a new key will be generated.\n
    :return: A dictionary with the encrypted string and the key\n
    """
    if key is None:
        key = crypto.generateKey()
    try:
        encrypted = crypto.encryptBasicString(text, key)
    except ValueError:
        raise HTTPException(status_code=400, detail="The key is invalid")
    return {"encrypted": encrypted, "key": key}


@router.get("/decrypt")
def decrypt(text: str, key: str) -> Union[dict, str]:
    """
    Decrypts a string with a key.\n
    :param text: The string to decrypt\n
    :param key: The key to decrypt with\n
    :return: A dictionary with the decrypted string\n
    """
    try:
        decrypted = crypto.decryptBasicString(text, key)
    except (ValueError, cryptography.fernet.InvalidToken):
        return {"error": "The key is invalid"}
    return decrypted


@router.get("/generateKey")
def generate_key() -> str:
    """
    Generates a key.\n
    :return: A dictionary with the generated key\n
    """
    return crypto.generateKey()


@router.get("/hash")
def hash_string(text: str, mode: Optional[str] = "sha256") -> str:
    """
    Hashes a string.\n
    :param text: The string to hash\n
    :param mode: [Optional] The mode to hash with. Default is sha256\n
    :return: A dictionary with the hashed string\n
    """
    return crypto.hashString(text, mode)