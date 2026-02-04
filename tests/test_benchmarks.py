from dovepy import DOVE


def test_encrypt_benchmark_1kb(benchmark):
    plaintext = b"A" * 1024
    key1 = "BenchmarkKeyOne"
    key2 = "BenchmarkKeyTwo"

    benchmark(lambda: DOVE.encrypt(plaintext, key1, key2))


def test_encrypt_benchmark_1mb(benchmark):
    plaintext = b"A" * (1024 * 1024)
    key1 = "BenchmarkKeyOne"
    key2 = "BenchmarkKeyTwo"

    benchmark(lambda: DOVE.encrypt(plaintext, key1, key2))


def test_encrypt_benchmark_10mb(benchmark):
    plaintext = b"A" * (1024 * 1024 * 10)
    key1 = "BenchmarkKeyOne"
    key2 = "BenchmarkKeyTwo"

    benchmark(lambda: DOVE.encrypt(plaintext, key1, key2))


def test_decrypt_benchmark(benchmark):
    plaintext = b"A" * 4096
    key1 = "BenchmarkKeyOne"
    key2 = "BenchmarkKeyTwo"

    c, s, t = DOVE.encrypt(plaintext, key1, key2)

    benchmark(lambda: DOVE.decrypt(c, key1, key2, s, t))
