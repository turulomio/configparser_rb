def string_to_rotatedbits(texto):
    # 1. Convertir cada carácter a su representación binaria de 8 bits
    # 'join' los une todos en una sola cadena de ceros y unos
    bits = ''.join(format(ord(c), '08b') for c in texto)
    
    if not bits:
        return ""

    # 2. El bit 0 (el primero) pasa a ser el último
    # Tomamos desde el índice 1 hasta el final + el primer bit
    bits_rotados = bits[1:] + bits[0]
    
    return bits_rotados

def rotatedbits_to_string(bits_rotados):
    if not bits_rotados:
        return ""
    
    # 1. Invertir la rotación: el último bit vuelve a ser el primero
    # Tomamos el último bit + desde el inicio hasta el penúltimo
    bits = bits_rotados[-1] + bits_rotados[:-1]
    
    # 2. Separar la cadena de bits en bloques de 8
    caracteres = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        # Convertir de binario (base 2) a entero y luego a carácter
        caracteres.append(chr(int(byte, 2)))
        
    return ''.join(caracteres)

