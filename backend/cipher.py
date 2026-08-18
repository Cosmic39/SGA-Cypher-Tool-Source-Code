import random

def _normalize_seed(seed):
    """Ensure seed is at least 8 chars long."""
    seed = str(seed).strip()
    if len(seed) < 8:
        raise ValueError("Seed must be at least 8 characters long.")
    return seed

def generate_sga_map(seed):
    """Generate reproducible SGA map from a seed."""
    seed = _normalize_seed(seed)
    random.seed(seed)  # works with both numbers & strings
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    sga_symbols = [
        'ᔑ','ʖ','ᓵ','↸','ᒷ','⎓','⎔','𝙷',
        '⚍','∷','╎','⋮','⍊','∴','ᓭ','ℸ',
        '⚎','⍁','⍂',':','⨅','⨀','𝙒','⨁','⨂','⨀'
    ]
    random.shuffle(sga_symbols)
    return dict(zip(alphabet, sga_symbols))

def generate_reverse_map(seed):
    return {v: k for k, v in generate_sga_map(seed).items()}

def caesar_encrypt(text, key):
    result = ''
    for char in text.lower():
        if char.isalpha():
            shifted = (ord(char) - ord('a') + key) % 26
            result += chr(ord('a') + shifted)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

def encrypt_message(message, caesar_key, seed):
    caesar = caesar_encrypt(message, caesar_key)
    sga_map = generate_sga_map(seed)
    return ''.join(sga_map.get(c, c) for c in caesar)

def decrypt_message(sga_text, caesar_key, seed):
    reverse_map = generate_reverse_map(seed)
    caesar = ''.join(reverse_map.get(symbol, symbol) for symbol in sga_text)
    return caesar_decrypt(caesar, caesar_key)
