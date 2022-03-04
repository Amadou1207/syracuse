def mul_egyptienne(a,b):

    s = 0
    while a != 0:
        if a % 2 == 1:
            s += b
        a = a // 2
        b += b

    print(s)

print ("Veuillez insérer 2 chiffres : ")
a = int(input("chiffre1 : "))
b = int(input("chiffre2 : "))
mul_egyptienne(a, b)

