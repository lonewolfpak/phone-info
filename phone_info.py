
#!/usr/bin/env python3
"""
Phone Info OSINT Tool
=====================
A fast, offline CLI utility for basic phone number intelligence.

Author:  Lone Wolf
GitHub:  https://github.com/lonewolfpak
License: MIT
Version: 1.0.0
"""

import sys
import phonenumbers
from phonenumbers import carrier, geocoder, timezone, number_type, PhoneNumberType

def describe_type(num_obj):
    """Map phonenumbers type enum to readable label."""
    t = number_type(num_obj)
    mapping = {
        PhoneNumberType.MOBILE: "mobile",
        PhoneNumberType.FIXED_LINE: "fixed line",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "fixed line or mobile",
        PhoneNumberType.TOLL_FREE: "toll free",
        PhoneNumberType.PREMIUM_RATE: "premium rate",
        PhoneNumberType.VOIP: "VoIP",
        PhoneNumberType.PERSONAL_NUMBER: "personal number",
        PhoneNumberType.PAGER: "pager",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.VOICEMAIL: "voicemail",
        PhoneNumberType.UNKNOWN: "unknown",
    }
    return mapping.get(t, f"type {t}")
def main():
    if len(sys.argv) < 2:
        print("usage: python phone_info.py <number_with_country_code> [--truecaller <installation_id>]")
        sys.exit(1)

    print("\033[94m" + r"""
    ██╗      ██████╗ ███╗   ██╗███████╗    ██╗    ██╗ ██████╗ ██╗     ███████╗
    ██║     ██╔═══██╗████╗  ██║██╔════╝    ██║    ██║██╔═══██╗██║     ██╔════╝
    ██║     ██║   ██║██╔██╗ ██║█████╗      ██║ █╗ ██║██║   ██║██║     █████╗  
    ██║     ██║   ██║██║╚██╗██║██╔══╝      ██║███╗██║██║   ██║██║     ██╔══╝  
    ███████╗╚██████╔╝██║ ╚████║███████╗    ╚███╔███╔╝╚██████╔╝███████╗██║     
    ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝     
    """ + "\033[0m")
    print("  [+] Tool: Phone OSINT")
    print("  [+] Author: Lone Wolf (Pakistani Ethical hacker")
    print("  [+] WhatsApp:https://chat.whatsapp.com/CaeXTwxd1081ZuHAZSUAvW?s=cl&p=a&iam=2")
    print("  [+] GitHub: https://github.com/lonewolfpak")
    print("-" * 44)

    # ... the rest of your main() code goes here ...
    if len(sys.argv) < 2:
        print("usage: python3 phone_info.py <number_with_country_code>")
        print("example: python3 phone_info.py +14155551234")
        sys.exit(1)

    raw = sys.argv[1].strip()

    # Parse — requires + prefix for global uniqueness
    try:
        num = phonenumbers.parse(raw, None)
    except phonenumbers.NumberParseException as e:
        print(f"error: could not parse '{raw}' — {e}")
        print("hint: include the country code, e.g. +1 for US")
        sys.exit(1)

    # Validate
    valid = phonenumbers.is_valid_number(num)
    possible = phonenumbers.is_possible_number(num)

    # Format variants
    e164 = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164)
    international = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    national = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.NATIONAL)

    # Country info
    region_code = phonenumbers.region_code_for_number(num)  # e.g. "US"
    country_name = geocoder.description_for_number(num, "en") or "(unknown)"

    # Carrier
    carrier_name = carrier.name_for_number(num, "en") or "(unknown or ported)"

    # Timezones
    tz_list = timezone.time_zones_for_number(num)
    tz_str = ", ".join(tz_list) if tz_list else "(unknown)"

    # Line type
    line_type = describe_type(num)

    # Output
    print("=" * 44)
    print(f"  Input:        {raw}")
    print("=" * 44)
    print(f"  E.164:        {e164}")
    print(f"  International:{international}")
    print(f"  National:     {national}")
    print("-" * 44)
    print(f"  Country:      {country_name} ({region_code})")
    print(f"  Carrier:      {carrier_name}")
    print(f"  Line type:    {line_type}")
    print(f"  Timezone:     {tz_str}")
    print("-" * 44)
    print(f"  Valid:        {valid}")
    print(f"  Possible:     {possible}")
    print("=" * 44)

    if not valid:
        print("  note: number passes syntax but is not in an assigned range")

if __name__ == "__main__":
    main()
