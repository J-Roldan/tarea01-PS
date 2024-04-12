import hashlib
from cryptography.fernet import Fernet

#Convierte la clave maestra en un Hash MD5
def encryptMasterPassword(masterPassword):
    md5 = hashlib.md5(masterPassword.encode())
    return md5

#Verifica que la clave ingresada correspnda al Hash almacenado 
def verifyMasterPassword(password, masterPasswordMD5):
    md5 = hashlib.md5(password.encode())
    return md5.hexdigest() == masterPasswordMD5.hexdigest()

#Genera una key para encriptar y desencriptar las contraseñas (GUARDAR KEY)
def generateKey():
    return Fernet.generate_key()

#Encripta la clave
def encryptPassword(key, password):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

#Desencripta la clave
def decryptPassword(key, password):
    fernet = Fernet(key)
    return fernet.decrypt(password.encode()).decode()