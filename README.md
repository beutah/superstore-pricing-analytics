# superstore-pricing-analytics
## Strategic Pricing & Commercial Analytics Dashboard (Superstore)

End-to-end pricing performance analytics project using **PostgreSQL + SQL (KPI mart) + Python (ingestion) + Power BI (dashboard)**.  
Built to mirror real-world strategic pricing work: revenue/profit, **margin leakage**, **discount impact**, **returns**, and trend analysis.

---

## Business Goal

Help a commercial/pricing team answer:
- Where is profit coming from (and leaking)?
- Which product segments/sub-categories show negative margin despite strong sales?
- How does discounting affect margin and profitability?
- Where do returns and fulfillment (ship time) contribute to performance risk?

---

## What I Built

### 1) Data Pipeline (Excel → PostgreSQL)
- Source: Tableau “Superstore” dataset (`superstore.xls`)
- Ingestion: Python + pandas reads Excel sheets and loads them into PostgreSQL schema `superstore`
- Tables created:
  - `superstore.orders` (~9,994 rows)
  - `superstore.returns` (~296 rows)
  - `superstore.people` (regional managers)

### 2) Analytics Mart (SQL View)
Created a reporting-ready mart:
- `superstore.mart_pricing_performance`

Includes:
- Revenue (Sales), Profit, **Margin %**
- Discount and quantity
- Return flag
- Shipping lead time (ship_days)
- Region / Category / Sub-category / Product dimensions
- Regional manager (People table)

### 3) Power BI Dashboard
A 3-page executive-style dashboard:
- **Executive Overview:** Sales, Profit, Margin% trends and top/bottom segments
- **Discount & Margin Leakage:** discount bands, margin erosion analysis, worst sub-categories
- **Returns & Operations:** return rates and ship-time performance drivers

> Add screenshots here once ready:
- `docs/screenshots/exec_overview.png`
- `docs/screenshots/discount_margin.png`
- `docs/screenshots/returns_ops.png`

---

## Tech Stack

- **PostgreSQL** (data warehouse + analytics mart)
- **SQL** (modeling and performance queries)
- **Python** (pandas, SQLAlchemy, psycopg2)
- **DBeaver** (querying + validation)
- **Power BI** (reporting + measures)

---

## Project Structure

```text
superstore_pricing/
├── load_superstore_excel_to_postgres.py
├── sql/
│   └── mart_pricing_performance.sql
├── docs/
│   └── screenshots/
└── README.md
>>>>>>> c9243ee (Initial commit: Superstore pricing mart pipeline + SQL)
