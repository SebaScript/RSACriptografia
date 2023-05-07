import random
from math import gcd

Caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z", "á", "é", "í", "ó", "ú", "A", "B", "C", "D", "E", "F", "G", "H", "I",
              "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Á", "É", "Í",
              "Ó", "Ú", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "^", "%", "#", "$",
              "@", " ", ",", ";", ". ", ":", "¿", "?", "¡", "!", "(", ")", "[", "]", "{", "}", "~", "=", "¬", "ñ",
              "Ñ", "ü", "Ü"]

listaPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
               103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]


def primos():
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
    for d in range(2, phi_n):
        if (e * d) % phi_n == 1:
            return d


def encriptar(mensaje, e, n):
    cifrado = [(Caracteres.index(i) ** e) % n for i in mensaje]
    print("- Mensaje cifrado:")
    print(''.join([Caracteres[i % len(Caracteres)] for i in cifrado]))
    return cifrado


def desencriptar(mensaje_encriptado, d, n):
    descifrado = [(c ** d) % n for c in mensaje_encriptado]
    return ''.join([Caracteres[i] for i in descifrado])


def main():
    while True:
        print("Algoritmo RSA para cifrar y descifrar mensajes")
        decision = input("1) Cifrar y descifrar un mensaje \n"
                         "2) Cerrar ")
        if decision == "1":
            p, q = primos()
            n = calcular_n(p, q)
            phi_n = calcular_phi(p, q)
            e = generar_clave_publica(phi_n)
            d = generar_clave_privada(e, phi_n)
            print(f"Clave pública (n, e): ({n}, {e})")
            print(f"Clave privada (n, d): ({n}, {d})")

            mensaje = input("Ingrese un mensaje para encriptar: ")

            mensaje_cifrado = encriptar(mensaje, e, n)
            mensaje_descifrado = desencriptar(mensaje_cifrado, d, n)

            decision2 = int(input("¿Ver el mensaje descifrado\n"
                                  "1) Si. \n"
                                  "2) No. "))
            if decision2 == 1:
                print("- Mensaje descifrado:")
                print(mensaje_descifrado)
        elif decision == "2":
            return False

        else:
            print("Por favor ingrese 1 o 2")


if __name__ == "__main__":
    main()
