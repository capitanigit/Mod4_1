def Palindrome(tekst):
    return tekst == tekst[::-1]
tekst = "kajak"
print(Palindrome(tekst))



"""def dodawanie():
    sum = 2+2
    print(f"wynik dodawania 2+2= {sum}")

dodawanie()

a = 1

def scope_demo():
    a = 2
    print(a)

scope_demo()
print(a)

def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

print(shopping())
"""

"""
#Mod 3 Zad 1
print("Mod 3 zad 1") 
print()
d = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"],
    }
suma = 0
for k in d:
    temp = [v.capitalize() for v in d[k]]
    print(f"Idę do {k.capitalize()} kupię tu naspępujące rzeczy {temp}")
    suma = suma + len(d[k])   
print(f"W sumie kupuję {suma} produktów")
print()
print("commit1")
print("commit2")
print("pozdrowienia dla Mentora ;]")"""