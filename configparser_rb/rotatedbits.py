import base64

def string_to_rotated_base64(texto):
    if not texto:
        return ""
    
    # Convertir string a bytes (latin-1 es eficiente y mapea 1:1 los primeros 256 caracteres)
    # Esto reemplaza la lógica de ord(c) y format(..., '08b')
    try:
        b_data = texto.encode('latin-1')
    except UnicodeEncodeError:
        raise ValueError("El texto debe contener solo caracteres en el rango 0-255")

    num_bits = len(b_data) * 8
    val = int.from_bytes(b_data, 'big')
    
    # Rotar bits a la izquierda 1 posición usando operaciones bitwise
    # ((val << 1) | (val >> (num_bits - 1))) & mask
    mask = (1 << num_bits) - 1
    rotated_val = ((val << 1) & mask) | (val >> (num_bits - 1))
    
    rotated_bytes = rotated_val.to_bytes(len(b_data), 'big')
    return base64.b64encode(rotated_bytes).decode('utf-8')

def rotated_base64_to_string(b64_texto):
    if not b64_texto:
        return ""
    
    try:
        rotated_bytes = base64.b64decode(b64_texto)
    except Exception:
        return ""

    if not rotated_bytes:
        return ""

    num_bits = len(rotated_bytes) * 8
    val = int.from_bytes(rotated_bytes, 'big')
    
    # Rotar bits a la derecha 1 posición (inverso de la rotación izquierda)
    original_val = (val >> 1) | ((val & 1) << (num_bits - 1))
    
    original_bytes = original_val.to_bytes(len(rotated_bytes), 'big')
    return original_bytes.decode('latin-1')
