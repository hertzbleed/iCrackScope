import lief

def analyze(binary_path):
    try:
        binary = lief.parse(binary_path)
        if not binary:
            print(f"[!] Could not parse {binary_path}")
            return

        print("\n== Binary Metadata ==")
        print(f"Name: {binary.name}")
        print(f"Format: {binary.format.name}")

        # Handle different LIEF versions gracefully
        header = getattr(binary, "header", None)
        if header:
            cpu_type = getattr(header, "cpu_type", "Unknown")
            cpu_subtype = getattr(header, "cpu_subtype", "Unknown")
            print(f"Architecture: {cpu_type}")
            print(f"Subtype: {cpu_subtype}")

        entry = getattr(binary, "entrypoint", None)
        if entry:
            print(f"Entry Point: {hex(entry)}")

        print("\n== Linked Libraries ==")
        for lib in getattr(binary, "libraries", []):
            print(f"- {lib}")

        print("\n== Encryption Info ==")
        if hasattr(binary, "has_encryption_info"):
            print(f"Encrypted: {'Yes' if binary.has_encryption_info else 'No'}")
        else:
            print("Encrypted: Unknown (not supported by this LIEF version)")

    except Exception as e:
        print(f"[!] Failed to analyze binary: {e}")
