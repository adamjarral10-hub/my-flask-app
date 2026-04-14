# ⚡ Flask Web App

A clean, production-ready Flask web application with a styled frontend and live REST API endpoints. Deploy in minutes.

---

## 📁 Project Structure

```
flask-app/
├── app.py              # Flask application & routes
├── templates/
│   └── index.html      # Frontend (HTML + CSS + JS)
├── requirements.txt    # Python dependencies
├── Procfile            # For Heroku / Railway / Render
├── runtime.txt         # Python version
├── .gitignore
└── README.md
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# 2. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Open **http://localhost:5000** in your browser.

---

## 🌐 API Endpoints

| Method | URL          | Description                    |
|--------|--------------|--------------------------------|
| GET    | `/`          | Serves the frontend page       |
| POST   | `/api/greet` | Returns a personalised greeting|
| GET    | `/api/ping`  | Health-check / uptime test     |

### Example — `/api/greet`

```bash
curl -X POST http://localhost:5000/api/greet \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice"}'
```

Response:
```json
{
  "message": "Hello, Alice! 👋  You reached the server at 14:30 on 14 April 2026.",
  "status": "ok"
}
```

---

## ☁️ Deploy to GitHub + Cloud

### Step 1 — Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2 — Deploy (choose one)

#### 🚂 Railway (recommended — free tier)
1. Go to [railway.app](https://railway.app) → **New Project → Deploy from GitHub**
2. Select your repo → Railway auto-detects the `Procfile` and deploys ✅

#### 🎨 Render (free tier)
1. Go to [render.com](https://render.com) → **New Web Service**
2. Connect your GitHub repo
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`

#### 🟣 Heroku
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

---

## 🛠 Adding New Routes

Open `app.py` and add a new route like this:

```python
@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello, World!"})
```

---

## 📄 License

MIT — free to use, modify, and distribute.
