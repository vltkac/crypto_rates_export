# Crypto Rates to CSV/JSON

## Description
This script fetches the latest cryptocurrency market data from the [CoinGecko API](https://www.coingecko.com/en/api) and saves it into a CSV or JSON file.  
It provides key information for the top 10 cryptocurrencies by market capitalization, including:

- Currency name  
- Symbol  
- Current price in USD  
- Market capitalization in USD  
- Highest and lowest prices within the last 24 hours  

---

## Installation

1. Ensure you have Python 3 installed.
2. Install required packages:

```bash
pip install requests
```

3. Place `main.py` in your working directory.

---

## Usage

Run the script from the command line:

```bash
python main.py --export_format json --new_file_name rates
```

### Arguments

- `--export_format` : Output file format (`json` or `csv`). Default is `json`.  
- `--new_file_name` : Name of the file to save data to. Default is `rates`.

Example to save as CSV:

```bash
python main.py --export_format csv --new_file_name crypto_data
```

---

## Output

The script generates a file in the current directory:

- `rates.json` or `rates.csv` (or your chosen file name)  

### CSV Example Columns:

| currency | symbol | current_price_in_usd | market_capitalization_in_usd | highest_price_within_24_hours_in_usd | lowest_price_within_24_hours_in_usd |
|----------|--------|--------------------|-----------------------------|-------------------------------------|-----------------------------------|

---

## Notes

- Make sure you have an active internet connection to fetch the data.  
- If the network request fails, the script will display an error message.  
- The script handles only the top 10 cryptocurrencies by market capitalization.  

---

## License

This project is open-source and free to use.
