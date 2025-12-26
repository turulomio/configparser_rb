from configparser_rb.rotatedbits import string_to_rotated_base64, rotated_base64_to_string
def test_configparser_rb():
    # --- Ejemplo de uso ---
    mensaje_original = "Hola"
    obfuscado = string_to_rotated_base64(mensaje_original)
    print(obfuscado)
    mensaje_recuperado = rotated_base64_to_string(obfuscado)

    assert mensaje_original == mensaje_recuperado

    print(f"Original:   {mensaje_original}")
    print(f"Obfuscado (Base64): {obfuscado}")
    print(f"Recuperado: {mensaje_recuperado}")
    assert False