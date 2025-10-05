import random

def password_generator():
    n = int(input("Number of chars (maximum 40) : "))
    if n > 40:
        return ("max. chars ---> 40 \n Password can't generate....😑😑😐")
    else:
        chars = "qwertyuiop147852369asdfghjkl!@#$%&?:ZXCVBNM"
        password = ""
        for i in range(n):
            ch = random.choice(chars)
            while ch in password:
                ch = random.choice(chars)
            password += ch
        return password
print(password_generator())