cadena = "abccba"
fruta = "anana"
hija = "hannah"
me = "ever"

def isCasiPalindromo(palabra):
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

print("1.   ", isCasiPalindromo(cadena))
print("2.   ", isCasiPalindromo(fruta))
print("3.   ", isCasiPalindromo(hija))
print("4.   ", isCasiPalindromo(me))