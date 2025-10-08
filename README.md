# 🏟️ Sports Social Media Analytics

![CI](https://github.com/ajay1018/sports-social-media-analytics/actions/workflows/ci.yml/badge.svg?branch=main)

Portfolio demo that ingests sample social posts (JSON), transforms them into engagement metrics (by team & league),
and renders a small Streamlit dashboard. Runnable extract/transform, **clean DE-style structure**, and diagrams.

---

## 🧱 Architecture (Mermaid)
```mermaid
flowchart TD
    SRC["Social APIs / JSON Dumps"] --> EXT["Extract (Python)"];
    EXT --> TR["Transform (pandas)"];
    TR --> OUT[("Processed CSVs")];
    OUT --> DASH["Streamlit Dashboard"];
```

## 🔁 Data Flow (Mermaid)
```mermaid
sequenceDiagram
    participant U as User/Runner
    participant E as Extract
    participant T as Transform
    participant F as Files (CSV)

    U->>E: run extract_local.py
    E-->>F: write posts.json
    U->>T: run transform_metrics.py
    T-->>F: write team_metrics.csv, league_metrics.csv
```

---

## ✅ What this shows
- 📥 Ingestion (stubbed extract) → 🧮 transformation → 📊 reporting
- 🧱 Organized repo for Data Engineering work
- ⚙️ Quick local run with minimal dependencies

---

## 🧰 Tech Stack
- 🐍 Python (pandas)
- 🗂️ JSON/CSV (local demo data)
- 🖥️ Streamlit (optional dashboard)

---

## 🚀 How to Run (Local)
```bash
# 1) install
pip install -r requirements.txt

# 2) generate raw + processed data
python src/extract/extract_local.py
python src/transform/transform_metrics.py

# 3) open the dashboard (optional)
streamlit run dashboards/app.py
```

---

## 📦 Outputs
- `data/processed/team_metrics.csv` — engagement by team
- `data/processed/league_metrics.csv` — engagement by league
- `data/processed/posts_enriched.csv` — posts with engagement column

---

## 📁 Project Structure
```
sports-social-media-analytics/
├─ src/
│  ├─ extract/extract_local.py
│  ├─ transform/transform_metrics.py
│  └─ load/ (optional)
├─ data/
│  ├─ raw/posts.json
│  └─ processed/
├─ dashboards/app.py
├─ notebooks/
├─ sql/
├─ docs/
├─ requirements.txt
└─ README.md
```

---

## 🔭 Status & Next
**Status:** Demo with sample data and runnable steps. 
**Next:** add lightweight CI, simple sentiment (e.g., VADER), and optional DB load.

