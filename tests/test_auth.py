import pytest
from dovepy import DOVE


def test_authentication_tag_mismatch():
    plaintext = b"HELLO THERE WE ARE TESTING OUT THIS AUTH MECH."
    key1 = "KeyOne"
    key2 = "KeyTwo"

    ciphertext, salt, tag = DOVE.encrypt(plaintext, key1, key2)

    bad_tag = (tag + 1) % 257

    with pytest.raises(ValueError):
        DOVE.decrypt(ciphertext, key1, key2, salt, bad_tag)
