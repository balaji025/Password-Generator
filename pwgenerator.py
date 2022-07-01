import random

def pwgenerate(n):
    a = 'abcdefghijklmnopqrstuvwxyz'
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    no = '1234567890'
    s = ['@', '_']
    c, m = '', ''
    for i in range(1, n):
        x = random.randint(1,3)
        if x == 1:
            c+=random.choice(a)
        elif x == 2:
            c+=random.choice(A)
        else:
            c+=random.choice(no)
    g = list(c)
    f = random.randint(1,n-1)
    g.insert(f, random.choice(s))
    for i in g:
        m+=i
    return m

def start():
    print("Welcome to password generator.")
    h = int(input("Enter the desired length of paasword: "))
    print("The generated password for the given length:",pwgenerate(h))
    print("Thank you for using our password generator.")

start()
