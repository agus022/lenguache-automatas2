def traducir_letra_a_simbolo(letra):
    letras_a_simbolos = {
        'A': 'Au',
        'B': 'Be',
        'C': 'C',
        'D': 'Dy',
        'E': 'Er',
        'F': 'F',
        'G': 'Ga',
        'H': 'H',
        'I': 'I',
        'J': 'Jn',
        'K': 'K',
        'L': 'Li',
        'M': 'Mg',
        'N': 'N',
        'O': 'O',
        'P': 'P',
        'Q': 'Qu',
        'R': 'Rb',
        'S': 'S',
        'T': 'Ti',
        'U': 'U',
        'V': 'V',
        'W': 'W',
        'X': 'Xe',
        'Y': 'Y',
        'Z': 'Zn'
    }
    
    if letra.upper() in letras_a_simbolos:
        return letras_a_simbolos[letra.upper()]
    else:
        return letra  # Devolver la letra original si no está en el diccionario

def traducir_frase_a_simbolos(frase):
    resultado = ""
    for letra in frase:
        resultado += traducir_letra_a_simbolo(letra)
    return resultado.strip()

while True:
    # Pedir al usuario una palabra o frase
    entrada = input("Ingresa el texto para traducirlo a LENGUACHE : ")
    
    if entrada.lower() == '0':
        break
    
    # Traducir y mostrar el resultado
    resultado = traducir_frase_a_simbolos(entrada)
    print(f"La traducción de '{entrada}' es: {resultado}")

print("Programa terminado.")
