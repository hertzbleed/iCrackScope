import lief
import re

def scan_symbols(binary_path):
    try:
        binary = lief.parse(binary_path)
        if not binary:
            print(f"[!] Could not parse {binary_path}")
            return

        print("\n== Interesting Symbols ==")
        suspicious_keywords = [
            "jailbreak", "cydia", "substrate", "StoreKit",
            "AdMob", "ads", "subscription"
        ]

        found = False
        for symbol in getattr(binary, "symbols", []):
            if not symbol.name:
                continue
            for keyword in suspicious_keywords:
                if re.search(keyword, symbol.name, re.IGNORECASE):
                    print(f"- {symbol.name}")
                    found = True

        if not found:
            print("No suspicious symbols found.")

    except Exception as e:
        print(f"[!] Symbol scan failed: {e}")
