from components.code_caesar import caesar_encrypt, caesar_decrypt

text = input("Entrez le texte à chiffrer : ")
key = int(input("Entrez la clé de décalage (1-25) : "))

encrypted_text = caesar_encrypt(text, key)
print(f"Texte chiffré : {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, key)
print(f"Texte déchiffré : {decrypted_text}")
