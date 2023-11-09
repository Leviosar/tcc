import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512

KEY_SIZE = 16
SALT_SIZE = 16
PBKDF2_ITERATIONS = 2**15


def encrypt(message: bytes, password="big_bad_wolf") -> bytes:
    """Encrypt a message with AES Output Feedback Mode, using a key
    generated by PBDKF2, returning the ciphertext left-padded by a random
    salt of 16-bytes, in base64.

    Args:
        message (bytes): plaintext message to be encrypted
        password (str, optional): password used to generate the AES key, must be ASCII. Defaults to "big_bad_wolf".

    Returns:
        bytes: ciphertext produced, left-padded by the salt and enconded in base64.
    """
    salt = get_random_bytes(SALT_SIZE)

    key = PBKDF2(password, salt, KEY_SIZE, PBKDF2_ITERATIONS, hmac_hash_module=SHA512)

    iv = bytearray(16)

    cipher = AES.new(key, AES.MODE_OFB, iv=iv)

    result = cipher.encrypt(message)

    result = salt + result

    return base64.b64encode(result)


def decrypt(ciphertext: bytes, password: str):
    """Decrypts a message using AES Output Feedback mode with the given password and returns it as
    a bytes object.

    Args:
        ciphertext (bytes): text to be decrypted, must include the 16-byte salt.
        password (str): password used to decrypt the text.

    Returns:
        _type_: _description_
    """
    ciphertext = base64.b64decode(ciphertext)

    salt = ciphertext[:SALT_SIZE]

    ciphertext = ciphertext[SALT_SIZE:]

    key = PBKDF2(password, salt, KEY_SIZE, PBKDF2_ITERATIONS, hmac_hash_module=SHA512)

    iv = bytearray(16)

    cipher = AES.new(key, AES.MODE_OFB, iv=iv)

    plaintext = cipher.decrypt(ciphertext)

    return plaintext
