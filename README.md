<!-- Project Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,100:0072ff&height=200&section=header&text=NIFTron%20(NIFTY%2050%20Trading%20Bot%20)📈&fontSize=40&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&center=true&vCenter=true&width=700&height=50&lines=Real-time+Strategy+Backtesting+%7C+Feature+Engineering" alt="Typing SVG" />
</p>

---

## 📊 Project Overview

**NIFTY 50 Trading Bot** is a professional-grade algorithmic trading system that:
- Fetches **real-time OHLCV data**
- Engineers technical and momentum-based features
- Implements **multiple portfolio strategies** (Momentum, Mean Reversion, Equal Weight)
- Generates **ensemble recommendations**
- Provides **backtesting performance reports**
- Includes a **Streamlit dashboard** for live insights

> 🔍 Built using Python · Pandas · NumPy · Streamlit  
> 🧠 Strategy-first design with modular architecture  
> 📦 Data refresh every 30 seconds (simulated near real-time)

---

## 🧠 Core Features

### 🔧 Feature Engineering
- **Momentum & Volatility Indicators**: MACD, RSI, Bollinger Bands
- **Returns Analysis**: Daily returns, price momentum, price-to-volume ratio
- **Normalization & Cleaning**: Data imputation, scaling, OHLCV smoothing

### 📈 Strategy Modules
- **Quantitative Momentum Strategy**
- **Mean Reversion Strategy**
- **Equal Weight Portfolio**
- **Ensemble Recommender**

### 🧪 Backtesting Engine
- Plug & play backtesting of strategies with:
  - Portfolio rebalancing
  - Daily returns tracking
  - Cumulative PnL calculation

### 📊 Streamlit Dashboard
- Visual performance metrics
- Portfolio allocation snapshots
- Strategy comparison charts

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,git,linux" />
</p>

- **Language**: Python  
- **Dashboard**: Streamlit  
- **Data Source**: Yahoo Finance (via `yfinance`)  
- **Deployment**: Localhost

---

## 🗂️ Project Structure

```bash
.
├── data/
│   └── nifty50/                   # OHLCV CSVs for each stock
├── src/
│   ├── feature_engineering/       # All feature extraction modules
│   ├── strategy_modules/          # Individual and ensemble strategies
│   ├── backtesting/               # Custom backtesting logic
│   └── utils/                     # Data cleaning, normalization, etc.
├── dashboard/
│   └── streamlit_app.py           # Live portfolio UI
├── scheduler/
│   └── fetch_ohlcv.py             # Auto-fetching of stock data
├── main.py                        # Central runner
├── requirements.txt
└── README.md
```

---
### 🚀 How to Run
- Install Requirements
  ```bash
    pip install -r requirements.txt
  ```
- Fetch NIFTY 50 Data
  ```bash
    python scheduler/fetch_ohlcv.py
  ```
- Run Strategies
  ```bash
  python main.py
  ```
- Launch Dashboard
  ```bash
  cd dashboard
  streamlit run streamlit_app.py
  ```
  ---
  ### 🧑‍💻 Author
  <p align="center">
  <a href="https://sachinchandra2022.github.io/Portfolio-Website/" target="_blank">
    <img src="https://img.icons8.com/color/96/internet--v1.png" width="40" title="Portfolio"/>
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/sachin-chandra-442349246/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" width="40" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="mailto:sachinchandra.work@gmail.com">
    <img src="https://skillicons.dev/icons?i=gmail" width="40" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://leetcode.com/Sachin_Chandra/" target="_blank">
    <img src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-level-up-your-coding-skills-and-quickly-land-a-job-logo-color-tal-revivo.png" width="40" title="LeetCode"/>
  </a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0072ff,100:00c6ff&height=120&section=footer"/>
</p>
```


