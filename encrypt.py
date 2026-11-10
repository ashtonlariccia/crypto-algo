import sys
import random
import string

char_pool = string.ascii_letters

def mkfi(name, data):
    with open(name, "w") as f:
        f.write(str(data))

def encrypt(password, rate, salt=None):
    if salt:
        preprocessed = str(password**rate)
        preprocessed_list = list(preprocessed)
        for ch in salt:
            pos = random.randint(0, len(preprocessed_list))
            preprocessed_list.insert(pos, ch)
        encrypted = "".join(preprocessed_list)
    else: 
        encrypted = password**rate
    return encrypted

def main():
    password = int(input("(e)password [int]: "))
    
    if input("(e)use salt? (y/n): ").strip().lower() == "y":
        salt = "".join(random.choices(char_pool, k=3))
        mkfi("salt", salt)
    else: salt = None
    
    rate = int(input("(e)rate: "))
    encrypted = encrypt(password, rate, salt)
    
    name = input("(e)file name: ")
    mkfi(name, encrypted)
    return 0

if __name__ == "__main__":
    sys.exit(main())
