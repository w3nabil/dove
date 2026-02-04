import pytest
from dovepy import DOVE


def test_empty_plaintext():
    plaintext = b""
    key1 = "KeyOne"
    key2 = "KeyTwo"

    ciphertext, salt, tag = DOVE.encrypt(plaintext, key1, key2)

    assert ciphertext == b""
    assert isinstance(salt, bytes)
    assert isinstance(tag, int)


def test_single_byte():
    plaintext = b"A"
    key1 = "KeyOne"
    key2 = "KeyTwo"

    c, s, t = DOVE.encrypt(plaintext, key1, key2)
    r = DOVE.decrypt(c, key1, key2, s, t)

    assert r == plaintext
