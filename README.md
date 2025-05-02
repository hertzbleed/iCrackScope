# iCrackScope
iCrackScope is a Python-based iOS binary analysis toolkit built for sideloaders, tweak developers, and reverse engineers. It helps identify encryption status, interesting classes/symbols, ad frameworks, subscriptions, and jailbreak detection logic in decrypted iOS apps.

# iCrackScope

**iCrackScope** is a Python-based iOS binary analysis toolkit built for sideloaders, tweak developers, and reverse engineers. It helps identify encryption status, interesting classes/symbols, ad frameworks, subscriptions, and jailbreak detection logic in decrypted iOS apps.

---

## 🔧 Features

* 📦 Binary metadata extraction (architecture, entrypoint, linked libs)
* 🔍 Symbol scanning for jailbreak/ad/subscription keywords
* 🛡️ Jailbreak detection heuristic scanning
* 💰 Ad & StoreKit (subscription) usage detection

---

## 📥 Installation

```bash
# Make sure Python 3.8+ and pip are installed
pip install lief
```

---

## 🚀 Usage

```bash
python main.py <decrypted_binary> [flags]
```

### Example:

```bash
python main.py Payload/AppName --metadata --symbols --jailbreak --ads
```

---

## 🏁 Flags

| Flag          | Description                                          |
| ------------- | ---------------------------------------------------- |
| `--metadata`  | Show binary metadata (arch, linked libs, encryption) |
| `--symbols`   | Scan for interesting class and symbol names          |
| `--jailbreak` | Heuristic scan for jailbreak detection strings       |
| `--ads`       | Detect ad networks and StoreKit usage                |

---

## 📂 Structure

```
iCrackScope/
├── analyzer/
│   ├── metadata.py
│   ├── symbols.py
│   ├── jailbreak_check.py
│   └── ads_subscription.py
├── main.py
└── README.md
```

---

## 🧠 Notes

* This tool is intended for **educational** and **ethical research** purposes only.
* Requires **decrypted iOS binaries** (use Frida, dumpdecrypted, BFDecrypt, etc).

---

## 📜 License

MIT License — Use responsibly.
