import random
from math import gcd

# Lista de caracteres permitidos
Caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z", "á", "é", "í", "ó", "ú", "A", "B", "C", "D", "E", "F", "G", "H", "I",
              "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Á", "É", "Í",
              "Ó", "Ú", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "^", "%", "#", "$",
              "@", " ", ",", ";", ". ", ":", "¿", "?", "¡", "!", "(", ")", "[", "]", "{", "}", "~", "=", "¬", "ñ",
              "Ñ", "ü", "Ü"]

# Lista de numeros primos de 2 y 3 cifras
listaPrimos = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
               103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
               223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337,
               347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
               463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
               607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
               743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
               883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


# Función para elegir aleatoriamente p y q
def primos():
    p = random.choice(listaPrimos)
    q = random.choice(listaPrimos)
    while q == p:
        q = random.choice(listaPrimos)
    return p, q


# Función para calcular el valor de n (base de Zn)
def calcular_n(p, q):
    return p * q


# Función para calcular cociente de Euler (Phi(n))
def calcular_phi(p, q):
    return (p - 1) * (q - 1)


# Función para generar clave publica (e = numero aleatorio primo relativo entre 1 y phi(n))
def generar_clave_publica(phi_n):
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            return e


# Función para generar clave privada (d = módulo del producto de los números enteros
# entre 1 y phi por la clave publica “e”, con phi(n))
def generar_clave_privada(e, phi_n):
    for d in range(2, phi_n):
        if (e * d) % phi_n == 1:
            return d


# Función para encriptar el mensaje ( modulo n de la lista de los indices del mensaje elevados a la clave publica)
def encriptar(mensaje, e, n):
    cifrado = [(Caracteres.index(i) ** e) % n for i in mensaje]
    print("- Mensaje cifrado:")
    print(''.join([Caracteres[i % len(Caracteres)] for i in cifrado]))
    return cifrado


# Función para desencriptar un mensaje cifrado (módulos n de cada posición de la lista de los indices
# del mensaje encriptado, elevada a la clave privada)
def desencriptar(mensaje_encriptado, d, n):
    descifrado = [(c ** d) % n for c in mensaje_encriptado]
    return ''.join([Caracteres[i] for i in descifrado])


# Interfaz por consola
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
