# 📧 Python Email Scraper

A Python-based terminal tool to help you find and extract email addresses from the web!  
You can use it to discover emails of content creators from Instagram, Facebook, TikTok, or any other public web page.  
Copy-paste web results, and let the script do the rest.  
Made with ❤️ by [batmanrizz](https://github.com/batmanrizz)

---

## ✨ Features

- 🔍 Google custom search queries for various social platforms
- 📋 Copy-paste Google results and extract emails with one run
- 📄 Automatically saves found emails to `emails.txt`
- 🧹 Filters duplicates and only appends new emails
- 🐍 Simple, clean Python code—easy to customize!

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x 🐍

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/batmanrizz/email-scraper.git
   cd email-scraper
   ```

2. *(Optional)* Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**  
   No external dependencies are strictly required, but for full web scraping you may want:
   ```bash
   pip install requests
   ```

---

## 📝 Usage

1. **Run the script:**
   ```bash
   python email_scraper.py
   ```
   - Choose the platform (Instagram, Facebook, Tiktok) when prompted.
   - A Google search tab will open with a custom query.

2. **Copy the whole page content** (Ctrl+C) from the Google results and **paste into a file** called `data.txt` in the script directory.

3. **The script will automatically extract all emails** from `data.txt` and append them to `emails.txt`.

---

## ⚡ Example

```
0 --> Instagram content creators
1 --> Facebook content creators
2 --> Tiktok content creators
PLEASE SELECT YOUR TYPE: 0
# (Google tab opens, copy content into data.txt)
Scrapping emails from url......
Found emails:
example1@gmail.com
creator@yahoo.com
...
```

---

## 🛠️ Customization

- Edit the `choices` and `rchoices` dictionaries in the script to add more platforms or refine your search queries.
- Adjust the regex in the script for custom email patterns or to scrape other data like phone numbers.

---

## 🤝 Contributing

Pull requests are welcome! Fork, tweak, and submit your ideas — let’s make scraping easier together. 👍

---

## 👤 Author

Made with ❤️ by [batmanrizz](https://github.com/batmanrizz)

---

## 📄 License

This project is licensed under the MIT License.

---

Happy Scraping! 🚀📧
