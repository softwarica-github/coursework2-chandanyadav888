import unittest
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from secret_pixel import encrypt_data, decrypt_data

class TestSecretPixel(unittest.TestCase):
    def setUp(self):
        # Generate RSA key pair for testing
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def test_encrypt_data_decrypt_data(self):
        # Generate some random data to encrypt
        data = b"Secret message to encrypt"
        
        # Encrypt the data
        encrypted_session_key, salt, iv, encrypted_data = encrypt_data(data, self.public_key)
        
        # Decrypt the data using the private key
        decrypted_data = decrypt_data(encrypted_session_key, salt, iv, encrypted_data, self.private_key)
        
        # Check if the decrypted data matches the original data
        self.assertEqual(decrypted_data, data)

if __name__ == '__main__':
    unittest.main()
