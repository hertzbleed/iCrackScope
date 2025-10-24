import lief

def scan_ads_and_subscriptions(binary_path):
    ad_keywords = ["AdMob", "UnityAds", "FBAd", "GAD", "ads"]
    sub_keywords = ["StoreKit", "SKPayment", "subscription", "purchase"]

    try:
        binary = lief.parse(binary_path)
        if not binary:
            print(f"[!] Could not parse {binary_path}")
            return

        print("\n== Ads & Subscription Indicators ==")
        found_ads, found_subs = False, False

        for symbol in getattr(binary, "symbols", []):
            if not symbol.name:
                continue

            for ad in ad_keywords:
                if ad.lower() in symbol.name.lower():
                    if not found_ads:
                        print("\n[Ads Detected]:")
                        found_ads = True
                    print(f"- {symbol.name}")

            for sub in sub_keywords:
                if sub.lower() in symbol.name.lower():
                    if not found_subs:
                        print("\n[Subscription Related Detected]:")
                        found_subs = True
                    print(f"- {symbol.name}")

        if not found_ads:
            print("\nNo ad libraries found.")
        if not found_subs:
            print("\nNo subscription logic found.")

    except Exception as e:
        print(f"[!] Ads/Subscription scan failed: {e}")
