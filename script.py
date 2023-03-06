from cryptography.fernet import Fernet

message = "Hello everyone, I am Abdou"

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print(f"normal: {message}")

print(f"encrypted: {encMessage}")

decrypt = fernet.decrypt(encMessage).decode()

print(f"decrypted {decrypt}")