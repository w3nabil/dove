from dovepy import DOVE

def test_encrypt_decrypt_roundtrip():
    plaintext = b"HELLO DOVE ENCRYPTION"
    key1 = "AlphaKey"
    key2 = "BetaKey"

    ciphertext, salt, tag = DOVE.encrypt(plaintext, key1, key2)
    recovered = DOVE.decrypt(ciphertext, key1, key2, salt, tag)

    assert recovered == plaintext
