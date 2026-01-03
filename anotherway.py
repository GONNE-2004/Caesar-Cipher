def caesar(text, shift, encrypt=True):
    """
Uses str.maketrans() to create a letter-to-letter shift table and
str.translate() to apply that table to the text. This maps each letter
(lower and upper) to its shifted version for encryption or decryption.
 """
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    """
    Encrypts the given text using a Caesar cipher with the specified shift.
   """
    return caesar(text, shift)


def decrypt(text, shift):
    """
    Decrypts the given text using a Caesar cipher with the specified shift.
    """
    return caesar(text, shift, encrypt=False)


encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
