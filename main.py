import random

def password_generator():
    n = int(input("Number of chars (maximum 30) : "))
    if n > 40:
        return ("max. chars ---> 30 \n Password can't generate....😑😑😐")
    else:
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        symbols = "!@#$%&?|"
        password = ''
        password += random.choice(lower)
        password += random.choice(upper)
        password += random.choice(digits)
        password += random.choice(symbols)
        all_chars = lower + upper + digits + symbols
        while len(password) < n :
            char = random.choice(all_chars)
            if char not in password:
                password += char
        password = ''.join(random.sample(password , len(password)))
        return password

print(password_generator())

