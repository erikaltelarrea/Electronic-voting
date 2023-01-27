#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import random
from sympy import randprime, isprime

# --- IMPLEMENTATION GOES HERE ---------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed




# --------------------------------------------------------------------------



def uoc_bezout(a, b):
    """
    Implements the Euclides Algorithm for finding the Bezout Identity:
    \lambda * a + \mu * b = d
    (See Theorem 2 and 3)

    :param a: integer value.
    :param b: integer value.
    :return: lambda and mu values
    """

    lamb = 1
    mu = 1
    # --- IMPLEMENTATION GOES HERE ---
    r_0 = a
    r_1 = b
    lamb_0 = 1
    lamb = 0
    mu_0 = 0
    mu = 1
    while r_1 != 0:
        q = r_0//r_1
        (r_0, r_1) = (r_1, r_0 - q*r_1)
        if r_1 != 0: #unicamente modificamos lamb, mu si r_1 != 0 para 
            #obtener la igualdad deseada (de otro modo obtendriamos
            #lamb*a+mu*b=0).
            (lamb_0, lamb) = (lamb, lamb_0 - q*lamb)
            (mu_0, mu) = (mu, mu_0 - q*mu)

    #aplicamos la version extendida del algoritmo de Euclides
    # --------------------------------

    return (lamb, mu)
    


def uoc_crt(a1, n1, a2, n2):
    """
    Implements the Chinese remainder theorem using the uoc_bezout()
    function for solving the modular system:
    x = a1 mod n1
    x = a2 mod n2
    (See Theorem 7)

    :param a1: the 'a1' value of the modular system.
    :param n1: the 'n1' value of the modular system.
    :param a2: the 'a2' value of the modular system.
    :param n2: the 'n2' value of the modular system.
    :return: the 'x' value
    """

    x = 1

    # --- IMPLEMENTATION GOES HERE ---
    y = uoc_bezout(n1, n2)
    lamb = y[1]
    mu = y[0]
    #calculamos los coeficientes de bezout mediante la funcion anterior
    x = (lamb*n2*a1+mu*n1*a2)%(n1*n2)
    #calculamos el unico resultado modulo n1*n2
    # --------------------------------
    
    return x


def uoc_genkey(lamb):
    """
    Generate a random key for the proposed cryptosystem.

    :param lamb: lambda parameter
    :return: key values (N, d, p, q)
    """

    N, d, p, q = 1, 1, 1, 1

    # --- IMPLEMENTATION GOES HERE ---
    p = randprime(2, lamb)
    q = randprime(2, lamb)
    #generamos "aleatoriamente" dos primos aleatorios en el intervalo deseado
    N = p*q
    #calculamos su producto
    d = uoc_crt(1, N, 0, (p-1)*(q-1))
    #usamos el Teorema Chino del resto para imponer d = 1 mod N y d = 0 mod (p-1)*(q-1)
    # --------------------------------

    return (N, d, p, q)




def uoc_encrypt(m, N):
    """
    Encrypt the message using the proposed cryptosystem.

    :param m: integer containing the message to encrypt
    :return: the encrypted message
    """

    c = 1

    # --- IMPLEMENTATION GOES HERE ---
    #escogemos un valor "aleatorio" de Z_N^*, para ello nos basta coger un primo
    #menor que N
    r = randprime(1, N) 
    #calculamos los dos factores del mensaje cifrado mediante la funcion pow(), logaritmica
    #en el exponente, y pasando el modulo como tercer parametro para evitar overfloats
    mod = N**2 #evitamos calcular N**2 3 veces
    c = (pow(1+N, m, mod)*pow(r, N, mod))%mod
    #finalmente los multiplicamos modulo N^2

    # --------------------------------

    return c


def uoc_decrypt(c, d, N):
    """
    Decrypt the message using the proposed cryptosystem.

    :param c: integer containing the message to decrypt
    :return: the decrypted message
    """

    m = 1

    # --- IMPLEMENTATION GOES HERE ---
    m = (pow(c, d, N**2)-1)//N 
    #aplicamos definicion de la funcion de desencriptado efectuando la division entera
    # --------------------------------

    return m



def uoc_vote(votes, N):
    """
    Encrypt the votes using the proposed cryptosystem.

    :param votes: list of "YES", "NO" votes
    :return: encrypted votes
    """

    c = 1

    # --- IMPLEMENTATION GOES HERE ---
    for i in votes:
        if i == "YES":
            c *= uoc_encrypt(1, N)
        else:
            c *= uoc_encrypt(0, N)

    #vamos calculando el producto de los votos cifrados en c
    #si es SI ciframos 1, de lo contrario ciframos 0
    # --------------------------------

    return c


def uoc_vote_count(c, d, N):
    """
    Count the votes using the proposed cryptosystem.

    :param votes: list of "YES", "NO" votes
    :return: encrypted votes
    """

    count = 1

    # --- IMPLEMENTATION GOES HERE ---
    count = uoc_decrypt(c, d, N)
    #se aplica la idea comentada en el apartado 2, el descifrado del producto del
    #mensaje cifrado corresponde a la suma de los votos, al numero de votos SI (a favor)
    # --------------------------------

    return count





