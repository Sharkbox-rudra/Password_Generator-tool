def password_generator():
    import random
    import time
    class NumberError(Exception):
        pass
    try:
        no_char = int(input("📌 Enter the number of charcter (must >4) : "))
        print("\n📌 Processing.....\n")
        time.sleep(1)
        upper_char = "QWERTYUYIOPASDFGHJKLZXCVBNM" 
        lower_char = "QWERTYUYIOPASDFGHJKLZXCVBNM".lower()
        symbl = "!@#$%&?/"
        number = "123456789"
        password = ""
        if no_char>=4:
            password +=  random.choice(upper_char)+random.choice(lower_char)+random.choice(symbl)+random.choice(number)
        else:
            raise NumberError("Value must be greater than 4 💀💀💀❌❌❌")
        all_char = upper_char+lower_char+symbl+number
        if len(all_char)<no_char:
            raise OverflowError("Character overflow 💀💀❌")
        while len(password)<no_char:
            new_char = random.choice(all_char)
            if new_char not in password:
                password += new_char
        # print(password)
        final_password = ' '.join(random.sample(password,len(password)))
    except ValueError:
        print("📌 Processing.......")
        time.sleep(1)
        print("Wrong Input enter ❌❌")
    except NumberError as e:
        # print("📌 Processing.......")
        # time.sleep(1)
        print(e)
    except OverflowError as e:
        print(e)
        
    else:
        print("✅ Password generating.......\n")
        time.sleep(1)
        uni_char = 1
        temp_char = ""
        print("📌 Checking Password (All Unique Charcters) : ")
        time.sleep(2)
        print(final_password)

        
    finally:
        print("Thank You ✨✨✨")
password_generator()
