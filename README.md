# Binance Futures Testnet Trading Bot

A simple and modular Python CLI trading bot for Binance Futures Testnet (USDT-M).

---

## Features

- MARKET Order Support
- LIMIT Order Support
- BUY / SELL Operations
- Binance Futures Testnet Integration
- Input Validation
- Logging System
- Error Handling
- Clean Modular Architecture

---

## Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── .env
└── README.md
```

---

## Setup (Mac)

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/trading_bot.git

cd trading_bot
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## requirements.txt

```txt
python-binance==1.0.19
python-dotenv==1.0.1
```

---

## Binance Futures Testnet Setup

1. Open:

```text
https://testnet.binancefuture.com
```

2. Login/Register

3. Go to API Management

4. Generate API Key & Secret Key

---

## Environment Variables

Create `.env` file in root directory:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

## Run the Bot

### MARKET BUY

```bash
python3 cli.py \
--symbol BTCUSDT \
--side BUY \
--order_type MARKET \
--quantity 0.01
```

---

### MARKET SELL

```bash
python3 cli.py \
--symbol BTCUSDT \
--side SELL \
--order_type MARKET \
--quantity 0.01
```

---

### LIMIT BUY

```bash
python3 cli.py \
--symbol BTCUSDT \
--side BUY \
--order_type LIMIT \
--quantity 0.01 \
--price 50000
```

---

### LIMIT SELL

```bash
python3 cli.py \
--symbol BTCUSDT \
--side SELL \
--order_type LIMIT \
--quantity 0.01 \
--price 80000
```

---

## Example Output

```text
========== ORDER SUMMARY ==========
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.01
===================================

2026-05-08 10:58:26 | INFO | Placing MARKET order

ORDER PLACED SUCCESSFULLY

=========== RESPONSE ===========
Order ID     : 13119853834
Status       : NEW
Executed Qty : 0.0000
Average Price: 0.00
================================
```

---

## Logging

Logs are stored in:

```bash
logs/trading_bot.log
```

Example:

```text
2026-05-08 10:58:26 | INFO | Placing MARKET order | Symbol=BTCUSDT | Side=BUY | Qty=0.01
```

---

## Validation

The bot validates:

- Trading Symbol
- BUY / SELL Side
- MARKET / LIMIT Order Type
- Quantity
- LIMIT Order Price

---

## Error Handling

Handles:

- Invalid Symbols
- Invalid Quantity
- Missing Price
- Binance API Errors
- Network Errors

---

## GitHub Push Commands

```bash
git init

git add .

git commit -m "Initial Commit"

git branch -M main

git remote add origin https://github.com/YOUR_USERNAME/trading_bot.git

git push -u origin main
```

---

## Author

Vikas Tiwari

GitHub:

```text
https://github.com/YOUR_USERNAME
```

---

## License

MIT License