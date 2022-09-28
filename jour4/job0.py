n =int(input("veuillez entrer un nombre entier :"))

def factorial (n):
    if (n == 0) :
        return 1
    else :
        return n * factorial(n - 1)

print(factorial(n))