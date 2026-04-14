# Payment API (PIX) 💳

A lightweight Flask API that simulates the full PIX payment flow: creation, QR code generation, confirmation, and real-time status update.

## Highlights ✨

- Create PIX payments with expiration timestamp
- Generate QR Code images per transaction
- Confirm payments via API
- Real-time update with Socket.IO event (`payment-confirmed-<payment_id>`)
- HTML pages for pending, confirmed, and not-found states

## Stack 🛠️

- Python
- Flask + Flask-SQLAlchemy
- Flask-SocketIO
- SQLite
- qrcode + Pillow
- pytest

## API Overview 🚀

- `POST /payments/pix` -> create payment
- `GET /payments/pix/qr_code/<file_name>` -> get QR code image
- `POST /payments/pix/confirmation` -> confirm payment
- `GET /payments/pix/<payment_id>` -> payment status page

## Quick Start ⚡

```bash
python -m venv .venv
source .venv/Scripts/activate  # Git Bash (Windows)
pip install -r requirements.txt
python app.py
```

App URL:

- `http://127.0.0.1:5000`

## Test 🧪

```bash
python -m pytest tests/test_pix.py -v
```

## Notes 📌

- QR images are generated at runtime inside `static/img`.
- Generated images are ignored by Git via `.gitignore`.
