# Datum Metrics Ltd — Wagtail CMS Website

> Enterprise Web Development, SaaS Platforms, Cyber-Security & Data Analytics

A high-performance CMS website built with **Wagtail 8**, **Django 6.1**, and **Python 3.13**, featuring a Torchbox-inspired **Black, Red & White** design system.

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|-----------|
| CMS | Wagtail 8.0 |
| Backend | Django 6.1, Python 3.13 |
| Database | MySQL / MariaDB (XAMPP) |
| Frontend | Vanilla CSS3, ES6 JavaScript |
| Typography | Plus Jakarta Sans, Inter (Google Fonts) |

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/datum-metrics-ltd.git
cd datum-metrics-ltd

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install wagtail pymysql

# 4. Configure database in datum_metrics/settings/dev.py

# 5. Run migrations
python manage.py migrate

# 6. Seed sample content
python manage.py seed_data

# 7. Start the development server
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** — site is live!  
Visit **http://127.0.0.1:8000/admin/** — Wagtail CMS admin (admin / admin12345)

---

## 📄 Pages

- **Homepage** — StreamField modular layout
- **Services** — Web Development, SaaS, Cyber-Security, Data Analytics, AI/ML, Cloud
- **Case Studies** — Enterprise client success stories
- **Insights / Blog** — Engineering articles and whitepapers
- **Contact** — Consultation request form

---

## 🎨 Design System

- **Background**: Deep Obsidian `#0A0B0D`
- **Accent**: Neon Crimson `#E50914`
- **Text**: White `#FFFFFF` / Muted Slate `#94A3B8`
- **Components**: Glassmorphic navbar, animated service cards, live ROI calculator

---

## 🗂️ Project Structure

```
datum-metrics-ltd/
├── datum_metrics/          # Project settings & URL routing
│   ├── settings/           # base.py, dev.py, production.py
│   ├── static/             # CSS & JS assets
│   └── templates/          # base.html
├── home/                   # Main Wagtail app
│   ├── models.py           # All page models
│   ├── blocks.py           # StreamField blocks
│   ├── templates/          # Page & block templates
│   └── management/         # seed_data command
├── search/                 # Wagtail search
└── manage.py
```

---

## 🚢 Deployment

See the [cPanel Deployment Guide](docs/cpanel_deployment_guide.md) for step-by-step instructions to deploy to cPanel shared hosting.

---

## 📝 License

MIT © Datum Metrics Ltd 2026
