# 📊 HSBC Marketing Campaign Performance Dashboard

<h3 align="center">
Interactive Marketing Analytics Dashboard built with Google BigQuery, SQL & Looker Studio
</h3>

<p align="center">

<a href="https://datastudio.google.com/reporting/05a8d095-04f0-4cb2-a347-3b1446d65e65">
<img src="https://img.shields.io/badge/🚀_Live_Dashboard-View_Now-red?style=for-the-badge">
</a>


</p>

---

## 📌 Project Overview

The **HSBC Marketing Campaign Performance Dashboard** is an interactive business intelligence solution designed to analyze digital marketing campaign performance across multiple channels.

The project uses **Google BigQuery** as the cloud data warehouse and **Looker Studio** for visualization. Raw marketing data is transformed using SQL views to provide clean, analytics-ready datasets for dashboard creation.

The dashboard enables stakeholders to monitor KPIs, compare marketing channels, evaluate campaign effectiveness, and make data-driven decisions through interactive filtering and visual reporting.

---

# 🚀 Live Dashboard

👉 **Click below to explore the dashboard**

**🔗 https://datastudio.google.com/reporting/05a8d095-04f0-4cb2-a347-3b1446d65e65**

---

# 🖼 Dashboard Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/a0b37ce5-d2f7-494d-ba5b-738cd3f5bebb" 
       alt="Executive Overview Screenshot" width="100%">
</p>

---

## 🔄 Project Tech Flow

![Tech Flow Diagram](https://github.com/user-attachments/assets/677ad743-2fe1-4693-b6fc-368be4002ae5)


The diagram above illustrates the end-to-end pipeline:

- **Data Sources** → Raw inputs such as CSV files, APIs, or transactional databases  
- **ETL Layer (Python)** → Cleans, validates, and transforms data before loading  
- **Cloud Data Warehouse (BigQuery)** → Centralized storage for structured analytics  
- **SQL Transformations** → Business rules, aggregations, and dimensional modeling  
- **BI Layer (Power BI / Looker Studio)** → Interactive dashboards and visual insights  


# ✨ Features

### Executive Overview

- Interactive Date Range Filter
- Channel Filter
- Campaign Filter
- Campaign Objective Filter
- Target Audience Filter

### KPI Scorecards

- Total Impressions
- Total Clicks
- Total Conversions
- Total Spend ($)
- Total Revenue ($)
- Click Through Rate (CTR)
- Return on Ad Spend (ROAS)

### Visualizations

- Revenue by Channel
- Spend by Channel
- CTR by Channel

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Google BigQuery | Cloud Data Warehouse |
| SQL | Data Cleaning & Transformations |
| Looker Studio | Dashboard & Visualization |
| Git | Version Control |
| GitHub | Project Hosting |

---

# 📂 Project Structure

```
HSBC-Marketing-Dashboard
│
├── README.md
│
├── sql/
│   ├── dashboard_view.sql
│   ├── campaign_performance.sql
│   ├── country_performance.sql
│   ├── device_performance.sql
│   └── monthly_performance.sql
│
├── screenshots/
│   └── executive-overview.png
│
├── assets/
│   └── hsbc_logo.png
│
└── docs/
```

---

# 📊 Data Pipeline

```
Raw Marketing Dataset
          │
          ▼
Google BigQuery
          │
          ▼
SQL Views
(dashboard_view,
campaign_performance,
country_performance,
device_performance,
monthly_performance)
          │
          ▼
Looker Studio
          │
          ▼
Interactive Dashboard
```

---

# 📁 Data Sources

| Dashboard Page | Data Source |
|---------------|------------|
| Executive Overview | dashboard_view |
| Campaign Performance | campaign_performance |
| Country Analysis | country_performance |
| Device Analysis | device_performance |
| Monthly Performance | monthly_performance |

---

# 📈 KPIs

The dashboard tracks the following business metrics:

- Impressions
- Clicks
- Conversions
- Spend
- Revenue
- CTR
- ROAS

---

# 📋 Current Dashboard Status

| Dashboard | Status |
|-----------|--------|
| Executive Overview | ✅ Completed |
| Campaign Performance | 🚧 In Progress |
| Country Analysis | 🚧 Planned |
| Device Analysis | 🚧 Planned |
| Monthly Performance | 🚧 Planned |

---

# 🎯 Future Enhancements

- Campaign Performance Dashboard
- Country-wise Analytics
- Device-wise Analytics
- Monthly Trends
- Budget Analysis
- CPC Analysis
- CPM Analysis
- CPA Analysis
- Conversion Rate Dashboard
- Profit Analysis
- Advanced Executive Dashboard
- Interactive Campaign Report

---

# 💡 Learning Outcomes

Through this project I gained hands-on experience in:

- Data Warehousing with Google BigQuery
- SQL View Creation
- Data Transformation
- Business Intelligence Dashboard Design
- Marketing KPI Analysis
- Interactive Report Development
- Data Visualization Best Practices

---

# 📸 Screenshots

| Executive Overview |
|--------------------|
| ![](screenshots/executive-overview.png) |

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Feel free to fork the repository and submit a Pull Request.

---

# 👨‍💻 Author

## Saurav Das

📧 Email: sauravdasdas07@gmail.com

💼 LinkedIn:
https://linkedin.com/in/YOUR_LINKEDIN

💻 GitHub:
https://github.com/YOUR_GITHUB_USERNAME

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

<p align="center">

Made with ❤️ using Google BigQuery, SQL & Looker Studio

</p>
