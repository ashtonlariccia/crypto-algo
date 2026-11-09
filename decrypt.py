import sys

def rfi(name):
    with open(name, "r") as f:
        return f.read()

def k_decrypt(encrypted, rate):
    password = encrypted**(1/rate)
    return int(password)

def uk_decrypt(encrypted):
    return 0

def main():
    name = input("(d)file name: ")
    encrypted = int(rfi(name))
    rate = input("(d)rate [or 'na']: ")
    if rate == "na": password = uk_decrypt(encrypted)
    else: password = k_decrypt(encrypted, int(rate))
    print(f"decrypted password: {password}")
    return 0

if __name__ == "__main__":
    sys.exit(main())