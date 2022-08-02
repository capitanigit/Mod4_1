#Mod 4 Zad 1
def palindrome(tekst):
    return tekst == tekst[::-1]
tekst = "kajak"
print(palindrome(tekst))