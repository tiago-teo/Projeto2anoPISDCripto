import hashlib
import random
import getpass
from .models import Hashing
from django.shortcuts import get_object_or_404
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from django.conf import settings
import os, base64


#Gera um salt aleatório de 16 caracteres de letras e números.
def create_salt():
    salt = ""
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(16):
        salt = salt + random.choice(ALPHABET)
        "".join(salt)
    return salt

#Concatena a password com o salt e calcula o hash SHA-256 do resultado em hexadecimal
def hash_pass(passw, salt):                
        password_hash = hashlib.sha256((passw + salt).encode('utf-8')).hexdigest()
        return password_hash

#Vai há base de dados do Hashing, pequisar pelo salt associado ao ID do utilizador,
#Faz o hash da password que utilizou para dar login e retorna o resultado
def hash_login(passw, userid):
    
    hasher = get_object_or_404(Hashing, user=userid)
    salt = hasher.salt
    password_hash = hashlib.sha256((passw + salt).encode('utf-8')).hexdigest()
    return password_hash

# Utiliza como chave a SECRET_KEY definida no .env
#Gera um vetor de inicialização (iv)
#Cria uma cifra de criptografia AES em modo CBC
#Aplica padding caso o texto não seja multiplo do bloco AES
#Encripta os dados e devolve em base64
def encrypt(plaintext):        
        key = settings.SECRET_KEY.encode()[:32]
        iv = os.urandom(16)  # Gera um IV aleatório
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()

        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(iv + encrypted_data).decode('utf-8')  # Prepend IV para usá-lo na descriptografia


#Recebe o texto cifrado e gera uma chave de desencriptação
#Descodifica o texto de base64 para bytes
#Extrai o vetor de inicialização dos primeiro 16 bytes
#Extrai o texto cifrado dos ultimos 16 bytes
#Após desencriptar, retira o padding do texto e devolve o texto original
def decrypt(ciphertext):
        key = settings.SECRET_KEY.encode()[:32]
        ciphertext = base64.b64decode(ciphertext)
        iv = ciphertext[:16]  # Extrai o IV
        ciphertext = ciphertext[16:]

        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()

        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()

        return data.decode()