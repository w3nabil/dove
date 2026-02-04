# 🕊️ DOVE — Experimental Encryption Algorithm (Python Version)

⚠️ WARNING: EXPERIMENTAL & NOT PRODUCTION-READY
DOVE is a research / experimental encryption algorithm.
Do NOT use this library to protect real, sensitive, or valuable data.

## Overview

DOVE is an experimental encryption algorithm implemented in Python for learning, research, and cryptographic exploration.

This project is not a replacement for established cryptographic standards such as `AES`, `ChaCha20`, or `RSA`.
It exists to explore ideas such as:

- Custom S-Box–based transformations

- Tag / authentication value evolution

- Byte-level operations

- Algorithm design trade-offs

## ⚠️ Security Disclaimer (Read This First)

- ❌ NOT audited

- ❌ NOT peer-reviewed

- ❌ NOT proven secure

- ❌ Vulnerable to cryptanalysis

If you need real security, use well-established libraries like cryptography, PyNaCl, hashlib (for hashing)

By using DOVE, you accept full responsibility for any consequences.

### Installation

```{py}
pip install dovepy
```

Installation does not imply stability or security.

### Basic Usage

```{py}
from dovepy import DOVE 

message = "Only I allow who will know my secrets."
key1 = "Matsubishi"
key2 = "Nissan"

cipher, salt, tag = DOVE.encrypt(message.encode("utf-8"), key1, key2)
print("Cipher:", cipher.hex()) #bytes , key1 and key2 are strings
print("Salt:", salt.hex()) #bytes
print("Tag:", tag) #int 

recovered = DOVE.decrypt(cipher, key1, key2, salt, tag)
print("Decrypted:", recovered.decode("utf-8"))
```

## Design Notes

- DOVE operates at the byte level

- Uses a custom S-Box

- Maintains an evolving authentication tag

- Focuses on simplicity and experimentation rather than performance or security guarantees

- This design intentionally avoids hiding complexity — the goal is learning, not obscurity.

## What This Project Is For

- ✅ Cryptography learning
- ✅ Algorithm experimentation
- ✅ Educational use
- ✅ Research and exploration
- ✅ Personal hidden projects
- ✅ Secondary data obfuscation

## What This Project Is NOT For

- ❌ Production encryption
- ❌ Protecting passwords
- ❌ Financial data
- ❌ Personal or private data directly

## Versioning & Stability

Current status:

- Development Stage:         Pre-Alpha

- API Stability:             Unstable

- Backward Compatibility:    Not guaranteed

Breaking changes may happen at any time.

## Testing

This project uses pytest for testing.

```{py}
pytest
```

Benchmarks:

```{py}
pytest --benchmark-only
```

## License

Licensed under the Apache-2.0 License.

## A few words

If you are studying cryptography: `Designing crypto is easy. Designing secure crypto is extremely hard.` DOVE is a step toward understanding why.

If you are curious about why an experimental encryption algorithm like DOVE was published, We plan to extend our research and build the most secure encryption algorithm oneday if we have enough fundings.......
