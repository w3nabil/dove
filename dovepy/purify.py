import re

"""
This module provides text purification utilities to sanitize and validate input strings.
Primary goal is to ensure small projects can avoid xss and injection attacks without needing large dependencies.
"""
class Purify:
    @staticmethod
    def text(text: str) -> str:
        return re.sub(r"[^a-zA-Z0-9 \-.]", "", text).strip()

    @staticmethod
    def passphrase(text: str) -> str:
        return re.sub(r"[^a-z]", "", text.lower()).strip()

    @staticmethod
    def text_size(text: str, max_size: int = 1000, min_size: int = 1) -> str:
        if not text:
            raise ValueError("Cannot encrypt an empty message.")

        purified = Purify.text(text)

        if len(purified) < min_size:
            raise ValueError(f"Message too short (min {min_size}).")

        if len(purified) > max_size:
            raise ValueError(f"Message too long (max {max_size}).")

        return purified
