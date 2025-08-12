def generate_pattern(length):
    charset1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charset2 = "abcdefghijklmnopqrstuvwxyz"
    charset3 = "0123456789"

    pattern = ""
    for ch1 in charset1:
        for ch2 in charset2:
            for ch3 in charset3:
                if len(pattern) >= length:
                    return pattern[:length]
                pattern += ch1 + ch2 + ch3
    return pattern[:length]

def find_offset(value, pattern, endian='little'):
    try:
        if value.startswith("0x"):
            value = value[2:]
        if len(value) % 2 != 0:
            value = "0" + value
        raw_bytes = bytes.fromhex(value)
        decoded = raw_bytes[::-1] if endian == 'little' else raw_bytes
        ascii_val = decoded.decode('latin-1', errors='replace')
        index = pattern.find(ascii_val)
        return ascii_val, index
    except Exception as e:
        return None, -1

def menu():
    while True:
        print("\n=== Cyclic Pattern Tool ===")
        print("1. Generate a pattern")
        print("2. Find offset of a value")
        print("3. Exit")
        choice = input("> ")

        if choice == '1':
            try:
                length = int(input("Enter pattern length: "))
                result = generate_pattern(length)
                print(f"\nGenerated pattern:\n{result}\n")
            except:
                print("Invalid input.")
        elif choice == '2':
            try:
                pat_len = int(input("Length of original pattern: "))
                value = input("Enter hex value (e.g. 0x63413463): ")
                endian = input("Endianness (little/big) [little]: ") or 'little'
                pat = generate_pattern(pat_len)
                ascii_val, offset = find_offset(value, pat, endian)
                if offset != -1:
                    print(f"Value '{ascii_val}' found at offset {offset}")
                else:
                    print("Not found. Check input.")
            except:
                print("Invalid input.")
        elif choice == '3':
            print("Bye!")
            break
        else:
            print("Pick 1, 2, or 3.")

if __name__ == "__main__":
    menu()
