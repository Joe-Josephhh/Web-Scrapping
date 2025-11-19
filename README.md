
[README.md](https://github.com/user-attachments/files/23635283/README.md)
# Quotes Scraper

**A small, beginner-friendly Python web scraper** that fetches quotes from [quotes.toscrape.com](https://quotes.toscrape.com) and filters them by keywords.

## What you get
- `scrapping.py` — main script (CLI-friendly)
- `requirements.txt` — libraries to install
- `.gitignore` — common ignores
- `LICENSE` — MIT license
## Quick start

1. Create a virtual environment (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate    # Windows (PowerShell)
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script
   ```bash
   python scrapping.py
   ```

4. Example: filter only for `life` and `love`
   ```bash
   python scrapping.py --keywords life love
   ```

## Project structure
```
quotes-scraper/
├── scrapping.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
```

## Contributing
Feel free to open issues or pull requests. 
