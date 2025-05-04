# 🚀 OMEGA-Surge 100X: Automated Prompt Commerce System

This repository contains a fully automated Python + Streamlit application with:
- 🔁 **CI/CD Pipelines**
- 🐳 **Dockerized Deployment**
- 🌐 **Streamlit Dashboard UI**
- 🤖 **Flowly AI Webhook Integration**
- 🧪 **Testing Framework via pytest**
- 📈 **CSV-based Data Visualization**

---

## 📂 Project Structure

| Path | Description |
|------|-------------|
| `streamlit_app.py` | Main app dashboard (CSV viewer + webhook tester) |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Builds Streamlit as a container |
| `.github/workflows/OMEGA_Surge_Full_Pipeline.yml` | Full CI/CD pipeline |
| `tests/` | pytest-compatible tests |
| `flowly_config.json` | Webhook config for Flowly integration |
| `monthly_drop_schedule.csv` | Drop calendar (for dashboard) |
| `white_label_licensing_kit.csv` | License kit contents |
| `multipliers_dashboard.csv` | Monetization and scale levers |

---

## ⚙️ Usage

### 🧪 Run Tests Locally
```bash
pip install -r requirements.txt
pytest tests/
```

### 🐳 Run with Docker
```bash
docker build -t omega-app .
docker run -p 8501:8501 omega-app
```

### 🌐 Launch Streamlit App
```bash
streamlit run streamlit_app.py
```

---

## 📡 Triggering Flowly
The Streamlit app includes a button to manually trigger the webhook defined in `flowly_config.json`.

---

## 🧠 Future Additions

| Component | Status |
|----------|--------|
| 🧬 GPT Prompt Generator | ⏳ Planned |
| 🧲 Real-Time User Feedback Capture | ⏳ Planned |
| 🔐 JWT-Gated Prompt Vault | ⏳ Planned |

---

### 📬 Questions? Ideas? Ping us via Flowly 🤖
