import re
"""
This module ensures that when we meant two words, it means two words not some spam.
"""
class PassChecker:
    @staticmethod
    def pass_chars(text: str):
        if not re.fullmatch(r"[a-zA-Z]+", text):
            raise ValueError("Keyphrase must contain only A–Z or a–z.")

    @staticmethod
    def pass_req(text: str):
        if not 5 <= len(text) <= 32:
            raise ValueError("Keyphrase length must be 5–32 characters.")
