import argparse
from metadata import analyze
from symbols import scan_symbols
from ads_subscription import scan_ads_and_subscriptions
from jailbreak_check import scan_jailbreak_checks


def main():
    parser = argparse.ArgumentParser(
        description="iCrackScope - iOS Binary Analysis Toolkit"
    )
    parser.add_argument("binary", help="Path to decrypted iOS binary")

    parser.add_argument("--metadata", action="store_true", help="Print binary metadata")
    parser.add_argument("--symbols", action="store_true", help="Scan for interesting symbols")
    parser.add_argument("--ads", action="store_true", help="Scan for ad/subscription frameworks")
    parser.add_argument("--jailbreak", action="store_true", help="Scan for jailbreak detection logic")
    parser.add_argument("--all", action="store_true", help="Run all scans")

    args = parser.parse_args()

    if args.all or args.metadata:
        print("[+] Extracting binary metadata...")
        analyze(args.binary)

    if args.all or args.symbols:
        scan_symbols(args.binary)

    if args.all or args.ads:
        scan_ads_and_subscriptions(args.binary)

    if args.all or args.jailbreak:
        scan_jailbreak_checks(args.binary)


if __name__ == "__main__":
    main()
