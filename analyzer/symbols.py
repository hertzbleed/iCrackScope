import lief
import re

def scan_symbols(binary_path):
    try:
        binary = lief.parse(binary_path)
        print("\n== Interesting Symbols ==")
        suspicious_keywords = ["jailbreak", "cydia", "substrate", "StoreKit", "AdMob", "ads", "subscription"]

        found = False
        for symbol in binary.symbols:
            for keyword in suspicious_keywords:
                if re.search(keyword, symbol.name, re.IGNORECASE):
                    print(f"- {symbol.name}")
                    found = True
        
        if not found:
            print("No suspicious symbols found.")

    except Exception as e:
        print(f"[!] Symbol scan failed: {e}")
