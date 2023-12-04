import unittest
from aes128 import encrypt, decrypt

class TestEncryptionModule(unittest.TestCase):

    def test_encrypt_decrypt(self):
        # Тестовый случай 1: Базовое шифрование с ключом
        input_bytes = [0x32, 0x88, 0x31, 0xe0, 0x43, 0x5a, 0x31, 0x37, 0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34]
        key = "TwoOneNineTwoOneNine"
        encrypted_result = encrypt(input_bytes, key)
        self.assertNotEqual(input_bytes, encrypted_result)  # Убедитесь, что шифрование изменяет входные данные

        # Тестовый случай 2: Шифрование с тем же ключом должно давать одинаковые результаты
        reencrypted_result = encrypt(input_bytes, key)
        self.assertEqual(encrypted_result, reencrypted_result)  # Убедитесь, что повторное шифрование идентично

        # Тестовый случай 3: Убедитесь, что расшифровка обратно
        decrypted_result = decrypt(encrypted_result, key)
        self.assertEqual(input_bytes, decrypted_result)  # Убедитесь, что расшифровка обратно

if __name__ == '__main__':
    unittest.main()