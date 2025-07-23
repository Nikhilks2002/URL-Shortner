# 🔗 URL Shortener Service

A simple URL shortening service like [bit.ly](https://bit.ly) or [tinyurl.com](https://tinyurl.com), built using Python and Flask.

---

## 🚀 Features

- Shorten long URLs to a short 6-character alphanumeric code.
- Redirect using the short code.
- Track and view analytics (click count, original URL, creation timestamp).
- In-memory storage (no database).
- REST API with JSON responses.

---

## 🛠 Prerequisites

- Python 3.8+
- `pip` (Python package manager)
- 3 hours of focused development time (for challenge)

---

## 📁 Project Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nikhilks2002/URL-Shortner.git
   cd url-shortener
``

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Run the Flask Server

In a new terminal window:

### On **Windows PowerShell**:

```powershell
$env:FLASK_APP = "app.main"
python -m flask run
```

### On **macOS/Linux** (or Git Bash):

```bash
export FLASK_APP=app.main
python -m flask run
```

You should see:

```
 Running on http://127.0.0.1:5000
```

---

## ✅ Running the Tests

In a **separate terminal** while the Flask server is running:

```bash
pytest
```

Alternatively, if you have a custom test file (e.g., `test_api.py`):

```bash
python test_api.py
```

> ✅ Make sure the Flask server is running **before** you run tests — otherwise requests will fail with connection errors.

---

## 🔄 Example API Usage

### 1. Shorten a URL

```bash
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/very/long/url"}'
```

**Response:**

```json
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
```

---

### 2. Redirect to Original URL

```bash
curl -L http://localhost:5000/abc123
```

---

### 3. Get Analytics

```bash
curl http://localhost:5000/api/stats/abc123
```

**Response:**

```json
{
  "url": "https://www.example.com/very/long/url",
  "clicks": 5,
  "created_at": "2024-01-01T10:00:00"
}
```

---

## 🧪 Testing Notes

* At least 5 tests cover:

  * Shorten logic
  * Redirection
  * Analytics
  * Error cases (e.g., invalid URL, missing short code)
  * Concurrent behavior
---

