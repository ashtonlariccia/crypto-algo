import sys

def rfi(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except:
        print("Error opening file")
        sys.exit(1)

def iroot(n, k):
    lo, hi = 0, 1 << (n.bit_length() // k + 1)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid**k <= n: lo = mid
        else: hi = mid - 1
    return lo

def k_decrypt(encrypted, rate, salt=None):
    preprocessed = list(encrypted.strip())
    if salt:
        for ch in salt.strip():
            preprocessed.remove(ch)
    return iroot(int("".join(preprocessed)), rate)

def uk_decrypt(encrypted):
    return 0

def main():
    name = input("(d)file name: ")
    
    encrypted = rfi(name)
    if input("salt file? (y/n): ").lower().strip() == "y":
        salt = rfi("salt")
    else: salt = None
        
    rate = input("(d)rate [or 'na']: ")
    if rate == "na": password = uk_decrypt(encrypted)
    else: password = k_decrypt(encrypted, int(rate), salt)
        
    print(f"decrypted password: {password}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())