import string

def caesar_encrypt(text: str, key: int) -> str:

    alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
    def shift(alphabet):
        return alphabet[key:] + alphabet[:key]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    result = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    encrypted_text = ''.join(text.translate(result))
    return encrypted_text

def caesar_decrypt(text: str, key: int) -> str:
    return caesar_encrypt(text, -key)