import lief

def analyze(binary_path):
    try:
        binary = lief.parse(binary_path)

        print("\n== Binary Metadata ==")
        print(f"Name: {binary.name}")
        print(f"Format: {binary.format.name}")
        print(f"Architecture: {binary.header.cpu_type.name}")
        print(f"Mode: {binary.header.cpu_subtype.name}")
        print(f"Entry Point: {hex(binary.entrypoint)}")

        print("\n== Linked Libraries ==")
        for lib in binary.libraries:
            print(f"- {lib}")

        print("\n== Encryption Info ==")
        if hasattr(binary, 'has_encryption_info') and binary.has_encryption_info:
            print("Encrypted: Yes")
        else:
            print("Encrypted: No or info not available")

    except Exception as e:
        print(f"[!] Failed to analyze binary: {e}")
