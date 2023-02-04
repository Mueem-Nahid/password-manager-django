from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings


def encrypt(pas):
    try:
        pas = str(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
        return encrypt_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(pas):
    print("here at decrypt", pas)
    try:
        pas = base64.urlsafe_b64decode(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        decod_pass = cipher_pass.decrypt(pas).decode("ascii")
        return decod_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None
