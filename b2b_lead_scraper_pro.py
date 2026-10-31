#!/usr/bin/env python3
"""
B2B Website Email, Phone & Social Media Lead Extractor Pro
Author: Tung Nguyen (@tungnguyen84)
Cloud Version: https://apify.com/tungnguyen84/b2b-website-email-phone-social-scraper
Custom Scrapers & Automation: https://www.fiverr.com/tungnguyen84
"""
import argparse
import csv
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_RE = re.compile(r"(?:\+?\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
SOCIAL_PATTERNS = {
    "linkedin": re.compile(r"https?://(?:www\.)?linkedin\.com/(?:company|in)/[^\s\"'<>]+", re.I),
    "facebook": re.compile(r"https?://(?:www\.)?facebook\.com/(?!sharer)[^\s\"'<>]+", re.I),
    "instagram": re.compile(r"https?://(?:www\.)?instagram\.com/[^\s\"'<>]+", re.I),
    "twitter": re.compile(r"https?://(?:www\.)?(?:twitter|x)\.com/(?!intent)[^\s\"'<>]+", re.I),
}

def fetch_html(url, timeout=12):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="ignore")

def extract_from_domain(url):
    url = url.strip()
    if not url.startswith("http"):
        url = "https://" + url
    domain = urlparse(url).netloc.replace("www.", "")
    pages = [url, urljoin(url, "/contact"), urljoin(url, "/about")]
    emails, phones = set(), set()
    socials = {k: "" for k in SOCIAL_PATTERNS}
    scanned = 0
    for page_url in pages:
        try:
            html = fetch_html(page_url)
            scanned += 1
            for e in EMAIL_RE.findall(html):
                el = e.lower()
                if not el.endswith((".png", ".jpg", ".gif", ".svg", ".webp", ".js", ".css")) and "sentry.io" not in el and "example.com" not in el:
                    emails.add(el)
            for p in PHONE_RE.findall(html):
                digits = re.sub(r"\D", "", p)
                if 10 <= len(digits) <= 15:
                    phones.add(p.strip())
            for k, pat in SOCIAL_PATTERNS.items():
                if not socials[k]:
                    m = pat.search(html)
                    if m:
                        socials[k] = m.group(0)
        except Exception:
            continue
    sorted_emails = sorted(emails)
    return {
        "website": url,
        "domain": domain,
        "primary_email": sorted_emails[0] if sorted_emails else "",
        "all_emails": "; ".join(sorted_emails),
        "phones": "; ".join(sorted(phones)[:5]),
        "linkedin": socials["linkedin"],
        "facebook": socials["facebook"],
        "instagram": socials["instagram"],
        "twitter": socials["twitter"],
        "pages_scanned": scanned,
        "status": "SUCCESS" if scanned > 0 else "UNREACHABLE",
    }

def main():
    parser = argparse.ArgumentParser(description="B2B Website Email, Phone & Social Media Lead Scraper")
    parser.add_argument("--input", "-i", help="Path to text file with URLs (one per line)")
    parser.add_argument("--output", "-o", default="b2b_leads_output.csv", help="Output CSV path")
    parser.add_argument("--workers", "-w", type=int, default=10, help="Concurrent worker threads")
    parser.add_argument("urls", nargs="*", help="Website URLs to scrape")
    args = parser.parse_args()

    targets = list(args.urls)
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            targets.extend([line.strip() for line in f if line.strip()])
    if not targets:
        targets = ["https://apify.com", "https://crawlee.dev"]

    fields = ["website", "domain", "primary_email", "all_emails", "phones", "linkedin", "facebook", "instagram", "twitter", "pages_scanned", "status"]
    with open(args.output, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(extract_from_domain, t): t for t in targets}
            for fut in as_completed(futures):
                row = fut.result()
                w.writerow(row)
                print(f"[{row['status']}] {row['domain']} -> Email: {row['primary_email']} | LinkedIn: {row['linkedin']}")
    print(f"\nSaved {len(targets)} records to {args.output}")

if __name__ == "__main__":
    main()
