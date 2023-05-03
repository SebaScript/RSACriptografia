import random
from math import gcd


Caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z", "á", "é", "í", "ó", "ú", "A", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Á", "É", "Í",
        "Ó", "Ú", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "^", "%", "#", "$",
        "@"," ", ",", ";", ". ", ":", "¿", "?", "¡", "!", "(", ")", "[", "]", "{", "}", "~", "=", "¬", "ñ",
        "Ñ", "ü", "Ü"]


listaPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
               103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def primos():
    while True:
        p = random.choice(listaPrimos)
        q = random.choice(listaPrimos)
        while q == p:
            q = random.choice(listaPrimos)
            return p, q

def calcular_n(p, q):
    return p * q

def calcular_phi(p, q):
    return (p - 1) * (q - 1)

def generar_clave_publica(phi_n):
        for e in range(2, phi_n):
            if gcd(e, phi_n) == 1:
                return e

def generar_clave_privada(e, phi_n):
    for d in range(1, phi_n):
        if (d * e) % phi_n == 1:
            return d

def encriptar(mensaje, e, n):
    indices_mensaje = [Caracteres.index(c) for c in mensaje]
    mensaje_encriptado = [(i ** e) % n for i in indices_mensaje]
    return ''.join([Caracteres[i % len(Caracteres)] for i in mensaje_encriptado])

def desencriptar(mensaje_encriptado, d, n):
    indices_encriptados = [Caracteres.index(C) for C in mensaje_encriptado]
    mensaje_desencriptado = [(j ** d) % n for j in indices_encriptados]
    return ''.join([Caracteres[i % len(Caracteres)] for i in mensaje_desencriptado])

def main():
    p, q = primos()
    n = calcular_n(p, q)
    phi_n = calcular_phi(p, q)
    e = generar_clave_publica(phi_n)
    d = generar_clave_privada(e, phi_n)
    print(f"Clave pública (n, e): ({n}, {e})")
    print(f"Clave privada (n, d): ({n}, {d})")

    mensaje = input("Ingrese un mensaje para encriptar: ")
    mensaje_cifrado = encriptar(mensaje, e, n)
    print(f"Mensaje encriptado: {mensaje_cifrado}")

    mensaje_descifrado = desencriptar(mensaje_cifrado, d, n)
    print(f"Mensaje desencriptado: {mensaje_descifrado}")


if __name__ == "__main__":
    main()