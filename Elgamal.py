from Crypto.PublicKey import ElGamal
from Crypto import Random
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse, getRandomRange

key = ElGamal.generate(512, Random.new().read)
public_key = key.publickey()

def encrypt_message(message, public_key):

    prime_modulus = int(key.p)
    generator_value = int(key.g)
    public_key_component = int(public_key.y)

    max_chunk_size = (prime_modulus.bit_length() // 8) - 20

    message_bytes = message.encode()

    if len(message_bytes) <= max_chunk_size:
        message_as_integer = bytes_to_long(message_bytes)

        random_ephemeral_key = getRandomRange(1, prime_modulus)

        ciphertext_part1 = pow(generator_value, random_ephemeral_key, prime_modulus)
        ciphertext_part2 = (message_as_integer * pow(public_key_component, random_ephemeral_key, prime_modulus)) % prime_modulus

        return (ciphertext_part1, ciphertext_part2)
    else:
        encrypted_parts = []

        for i in range(0, len(message_bytes), max_chunk_size):
            chunk = message_bytes[i:i + max_chunk_size]
            chunk_as_integer = bytes_to_long(chunk)

            random_ephemeral_key = getRandomRange(1, prime_modulus)

            ciphertext_part1 = pow(generator_value, random_ephemeral_key, prime_modulus)
            ciphertext_part2 = (chunk_as_integer * pow(public_key_component, random_ephemeral_key, prime_modulus)) % prime_modulus

            encrypted_parts.append((ciphertext_part1, ciphertext_part2))

        return encrypted_parts

def decrypt_message(encrypted_data,key):

    prime_modulus = int(key.p)
    private_exponent = int(key.x)

    if isinstance(encrypted_data, tuple) and len(encrypted_data) == 2:
        ciphertext_part1, ciphertext_part2 = encrypted_data

        shared_secret = pow(ciphertext_part1, private_exponent, prime_modulus)
        shared_secret_inverse = inverse(shared_secret, prime_modulus)
        decrypted_message_integer = (ciphertext_part2 * shared_secret_inverse) % prime_modulus

        decrypted_plaintext = long_to_bytes(decrypted_message_integer).decode()
        return decrypted_plaintext

    else:
        decrypted_parts = []

        for encrypted_chunk in encrypted_data:
            ciphertext_part1, ciphertext_part2 = encrypted_chunk

            shared_secret = pow(ciphertext_part1, private_exponent, prime_modulus)
            shared_secret_inverse = inverse(shared_secret, prime_modulus)
            decrypted_chunk_integer = (ciphertext_part2 * shared_secret_inverse) % prime_modulus
            decrypted_chunk_bytes = long_to_bytes(decrypted_chunk_integer)

            decrypted_parts.append(decrypted_chunk_bytes)

        decrypted_message = b''.join(decrypted_parts).decode('utf-8')
        return decrypted_message


print("\n===ElGamal Cipher===")

message = "Encryption with ElGamal"

print("Original message:", message)

encrypted = encrypt_message(message, public_key)
print("Encrypted message:", encrypted)

decrypted = decrypt_message(encrypted, key)
print("Decrypted message:", decrypted)

if message == decrypted:
    print("\nSuccessful Encryption and Decryption!")
else:
    print("\nFailed Encryption and Decryption.")

print("\n" + "="*50)

long_message = "This is a very long message " * 30
print("Original long message:", long_message[:50] + "...")

encrypted_long = encrypt_message(long_message, public_key)
print("Type of encrypted data:", type(encrypted_long))

decrypted_long = decrypt_message(encrypted_long,key)
print("Message after decryption:", decrypted_long[:50] + "...")

if long_message == decrypted_long:
    print("\nSuccessful Encryption and Decryption of long message!")
else:
    print("\nFailed Encryption and Decryption of long message.")
