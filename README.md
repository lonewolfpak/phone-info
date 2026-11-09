# Phone Info OSINT 🐺

A fast, offline CLI utility for basic phone number intelligence. Extracts country, carrier, line type, and timezone directly from any international phone number.

Built by **Lone Wolf**.

## ⚡ Features

- **Offline & Fast:** Powered by Google's `libphonenumber` metadata. No API keys, no rate limits, no external requests.
- **Deep Parsing:** Retrieves country code, region, carrier, line type (mobile, VoIP, fixed-line), and timezones.
- **Format Standardization:** Automatically formats numbers into E.164, International, and National standards.
- **Validation:** Checks if the number is syntactically possible and assigned to a valid range.

## 🛠️ Installation

Because modern Linux distributions (like Kali) use externally managed environments, it is best to run this in a virtual environment.

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/phone-info.git
cd phone-info

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
