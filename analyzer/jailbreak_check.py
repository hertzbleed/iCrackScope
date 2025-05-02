import lief

def scan_jailbreak_checks(binary_path):
    suspicious_strings = [
        "/Applications/Cydia.app",
        "/Applications/Dopamine.app",
        "/bin/bash",
        "/usr/sbin/sshd",
        "/etc/apt",
        "MobileSubstrate",
        "libcycript",
        "/private/var/lib/apt/"
    ]

    try:
        binary = lief.parse(binary_path)
        print("\n== Jailbreak Check Heuristics ==")
        found = False

        for segment in binary.segments:
            if not segment.content:
                continue
            data = bytes(segment.content)
            for s in suspicious_strings:
                if s.encode() in data:
                    print(f"Potential jailbreak check: {s}")
                    found = True

        if not found:
            print("No obvious jailbreak checks found.")

    except Exception as e:
        print(f"[!] Jailbreak heuristic scan failed: {e}")
