import sys

def mkfi(name, encrypted):
    with open(name, "w") as f:
        f.write(str(encrypted))

def encrypt(password, rate):
    encrypted = password**rate
    return encrypted

def main():
    password = int(input("(e)password: "))
    rate = int(input("(e)rate: "))
    encrypted = encrypt(password, rate)
    name = input("(e)file name: ")
    mkfi(name, encrypted)
    return 0

if __name__ == "__main__":
    sys.exit(main())