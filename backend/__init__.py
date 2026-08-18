"""
Minecraft SGA Cipher Backend
----------------------------
Provides encryption and decryption functions that combine
a Caesar cipher with a seed-based Standard Galactic Alphabet (SGA) mapping.

Usage:
    from backend import encrypt_message, decrypt_message
"""

from .cipher import encrypt_message, decrypt_message

__all__ = ["encrypt_message", "decrypt_message"]
