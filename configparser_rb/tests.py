from configparser_rb import string_to_rotatedbits, rotatedbits_to_string
def test_configparser_rb():
    # --- Ejemplo de uso ---
    mensaje_original = "Hola"
    bits_modificados = string_to_rotatedbits(mensaje_original)
    mensaje_recuperado = rotatedbits_to_string(bits_modificados)

    print(f"Original:   {mensaje_original}")
    print(f"En bits (rotado): {bits_modificados}")
    print(f"Recuperado: {mensaje_recuperado}")