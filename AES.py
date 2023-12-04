from cryptography.fernet import Fernet

# Генерируем случайный ключ
key = Fernet.generate_key()

# Создаем объект Fernet, используя сгенерированный ключ
cipher = Fernet(key)

# Шифруем сообщение
message = "Hello, world!"
encrypted_message = cipher.encrypt(message.encode())

# Расшифровываем сообщение
decrypted_message = cipher.decrypt(encrypted_message)

# Выводим результат
print("Message:", message)
print("Encrypted message:", encrypted_message.decode())
print("Decrypted message:", decrypted_message.decode())