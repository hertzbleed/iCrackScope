import argparse
from analyzer import metadata


def main():
    parser = argparse.ArgumentParser(description="iCrackScope - iOS Binary Analysis Toolkit")
    parser.add_argument("binary", help="Path to decrypted iOS binary")
    parser.add_argument("--metadata", action="store_true", help="Print binary metadata")
    args = parser.parse_args()

    if args.metadata:
        print("[+] Extracting binary metadata...")
        metadata.analyze(args.binary)


if __name__ == "__main__":
    main()
