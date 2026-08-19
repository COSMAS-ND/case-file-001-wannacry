import re
import sys
from pathlib import Path

IP_PATTERN = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
HASH_PATTERN = r'\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{40}\b|\b[a-fA-F0-9]{64}\b'
URL_PATTERN = r'https?://[^\s<>"\']+'

def extract_iocs(text):
    ips = sorted(set(re.findall(IP_PATTERN, text)))
    hashes = sorted(set(re.findall(HASH_PATTERN, text)))
    urls = sorted(set(re.findall(URL_PATTERN, text)))

    return ips, hashes, urls


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ioc_extractor.py <input_file>")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)

    text = input_file.read_text(errors="ignore")

    ips, hashes, urls = extract_iocs(text)

    print("\n=== IOC EXTRACTION RESULTS ===\n")

    print("IP ADDRESSES:")
    for ip in ips:
        print(f"  {ip}")

    print("\nHASHES:")
    for h in hashes:
        print(f"  {h}")

    print("\nURLS:")
    for url in urls:
        print(f"  {url}")

    print("\n=== SUMMARY ===")
    print(f"IP addresses: {len(ips)}")
    print(f"Hashes:       {len(hashes)}")
    print(f"URLs:         {len(urls)}")


if __name__ == "__main__":
    main()
