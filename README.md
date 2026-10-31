# 🚀 B2B Website Email, Phone & Social Media Lead Scraper + Shopify & SEO Audit Suite

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Apify Store](https://img.shields.io/badge/Apify_Store-3_Live_Cloud_Actors-00C853.svg)](https://apify.com/tungnguyen84)
[![Hire on Fiverr](https://img.shields.io/badge/Fiverr-5.0%E2%98%85_Top_Rated_Developer-1DBF73.svg)](https://www.fiverr.com/tungnguyen84)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-speed, zero-dependency **Python B2B Lead Generation & Contact Extractor** paired with **1-Click Excel VBA Cleaning & Consolidation Macros** and **Hosted Cloud Scrapers**.

Designed for **Sales Teams, Cold Email Agencies, E-Commerce Brands, SEO Agencies, and Growth Hackers** who need verified business emails, phone numbers, social media profiles (`LinkedIn`, `Facebook`, `Instagram`, `X/Twitter`, `YouTube`, `TikTok`), Shopify product catalogs, and technical SEO audits.

---

## ☁️ Run Instantly in the Cloud (Apify Store — Export to CSV / Excel / JSON / API)

Don't want to manage proxies or servers? Run our official cloud scrapers directly in your browser or via REST API:

| Cloud Actor | Best For | Launch Link |
| :--- | :--- | :--- |
| **1. B2B Website Email, Phone & Social Media Contact Scraper** | Extracting verified emails, phone numbers, LinkedIn, Facebook, Instagram, X/Twitter, YouTube & TikTok from company domains (`/contact`, `/about` auto-discovery). | 👉 **[Run on Apify Store](https://apify.com/tungnguyen84/b2b-website-email-phone-social-scraper)** |
| **2. Shopify Store Products, Prices & B2B Contact Email Scraper** | Extracting full Shopify product catalogs (`title`, `price`, `compareAtPrice`, `SKU`, `inStock`, `variants`, `images`) + store contact emails. | 👉 **[Run on Apify Store](https://apify.com/tungnguyen84/shopify-store-product-contact-scraper)** |
| **3. Website SEO Audit, Meta Tags, Headings & Contact Email Scraper** | Auditing technical SEO across websites (`Title`, `Meta Description`, `Canonical`, `H1/H2`, `Word Count`, `Missing Alt Tags`, `Internal/External Links`, `Emails`). | 👉 **[Run on Apify Store](https://apify.com/tungnguyen84/website-sitemap-seo-audit-email-scraper)** |

---

## 🛠️ Need a Custom Web Scraper, Anti-Bot Bypass, or Excel VBA Dashboard?

We build custom **Python Scrapers (Playwright / Selenium / Cloudflare & DataDome Bypass)**, **B2B Lead Lists**, and **Automated Excel VBA Dashboards** with **24-Hour Turnaround** and a **Free Sample Before You Pay**:

- 🟢 **Order on Fiverr (5.0★ Rated, 100% Completion):**
  - [Python Web Scraping, Data Extraction & B2B Lead Generation](https://www.fiverr.com/s/kL4m6V0)
  - [Excel VBA Macros, Custom Formulas & Automated Dashboards](https://www.fiverr.com/s/bd4m6V0)
- 💼 **Hire on Freelancer.com:** [@ittungnguyen](https://www.freelancer.com/u/ittungnguyen)
- 💳 **Direct Fast-Track Order / Sponsorship via PayPal:** `it.tungnguyen@gmail.com`

---

## ✨ What's Included in This Open-Source Repository

1. **`b2b_lead_scraper_pro.py` (Multi-Threaded Python CLI)**
   - Concurrent multi-threaded crawling (`--workers 10` by default).
   - Automatic discovery & crawling of `/contact` and `/about` pages.
   - Filters out false-positive asset/image filenames and Sentry/Wix tracking hashes.
   - Extracts international & US phone numbers and company social links (`LinkedIn`, `Facebook`, `Instagram`, `Twitter/X`).
   - Outputs UTF-8-SIG CSV that opens cleanly in Microsoft Excel and Google Sheets.

2. **`excel_vba_automation_macros.bas` (1-Click Excel VBA Module)**
   - `CleanAndDeduplicateLeads`: Normalizes emails/domains and removes duplicate rows in 1 click.
   - `ConsolidateAllSheetsToMaster`: Merges all worksheets in a workbook into a single `Master_Consolidated` sheet automatically.

---

## 🚀 Quick Start (Python CLI)

```bash
# 1. Create a urls.txt file with one company website per line
echo https://apify.com > urls.txt
echo https://crawlee.dev >> urls.txt

# 2. Run the multi-threaded scraper
python b2b_lead_scraper_pro.py --input urls.txt --output b2b_leads.csv --workers 10
```

---

## 📊 Quick Start (Excel VBA Macros)

1. Open your scraped `.csv` or `.xlsx` file in **Microsoft Excel**.
2. Press `ALT + F11` to open the **VBA Editor**.
3. Click **File -> Import File...** and select `excel_vba_automation_macros.bas`.
4. Close the VBA Editor and press `ALT + F8` to run `CleanAndDeduplicateLeads` or `ConsolidateAllSheetsToMaster`.

---

## 📬 Contact & Custom Development

Need data extracted from **Google Maps, Yelp, YellowPages, LinkedIn, Car Dealerships, Real Estate Portals, or E-Commerce Stores**?
- **Email / PayPal:** `it.tungnguyen@gmail.com`
- **Apify Store Profile:** [https://apify.com/tungnguyen84](https://apify.com/tungnguyen84)
- **Fiverr Profile:** [https://www.fiverr.com/tungnguyen84](https://www.fiverr.com/tungnguyen84)
