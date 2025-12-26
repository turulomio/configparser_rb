from configparser_rb.rotatedbase64 import string_to_rotatedbase64, rotatedbase64_to_string
def test_configparser_rb():
    mensaje_original = "Hola"
    obfuscado = string_to_rotatedbase64(mensaje_original)
    assert obfuscado =="kN7Ywg=="
    mensaje_recuperado = rotatedbase64_to_string(obfuscado)
    assert mensaje_recuperado == "Hola"
    mensaje_original = "Turulomíñçjhg$%&o"
    assert rotatedbase64_to_string(string_to_rotatedbase64(mensaje_original)) == mensaje_original
    mensaje_original = "đðßđð@ſ¶ħ€ŧđħħ¶ŧſħđßð12"
    assert rotatedbase64_to_string(string_to_rotatedbase64(mensaje_original)) == mensaje_original