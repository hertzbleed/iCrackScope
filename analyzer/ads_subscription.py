import lief

def scan_ads_and_subscriptions(binary_path):
    ad_keywords = ["AdMob", "UnityAds", "FBAd", "GAD", "ads"]
    sub_keywords = ["StoreKit", "SKPayment", "subscription", "purchase"]

    try:
        binary = lief.parse(binary_path)
        print("\n== Ads & Subscription Indicators ==")
        found_ads, found_subs = False, False

        for symbol in binary.symbols:
            for ad in ad_keywords:
                if ad.lower() in symbol.name.lower():
                    if not found_ads:
                        print("\n[Ads Detected]:")
                    print(f"- {symbol.name}")
                    found_ads = True

            for sub in sub_keywords:
                if sub.lower() in symbol.name.lower():
                    if not found_subs:
                        print("\n[Subscription Related Detected]:")
                    print(f"- {symbol.name}")
                    found_subs = True

        if not found_ads:
            print("\nNo ad libraries found.")
        if not found_subs:
            print("\nNo subscription logic found.")

    except Exception as e:
        print(f"[!] Ads/Subscription scan failed: {e}")
