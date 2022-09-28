n =int(input("veuillez entrer un nombre entier :"))

def puissance (x, n):
    if (n == 0) :
        return 1
    else :
        return x * puissance(x, n- 1)

print(puissance(4,n))