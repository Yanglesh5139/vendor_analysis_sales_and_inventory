# 📊 Sales and Vendor Analysis Dashboard (End-to-End Data Analytics Project)

## 🧩 Situation
The organization required a **comprehensive and reliable analytics solution** to evaluate both **sales performance** and **vendor efficiency** across multiple liquor brands.  
The raw data was scattered in various CSV files — lacking a unified system for cleaning, validation, and analysis.

---

## 🎯 Task
To design and develop an **end-to-end analytics pipeline** that:
- Automates data ingestion, cleaning, and transformation using **Python** and **SQL**.  
- Maintains **industry-grade logging and data traceability** for audit and debugging.  
- Delivers a **dynamic Power BI dashboard** for sales and vendor performance insights.  
- Provides **KPI-driven intelligence** for management decisions.

---

## 🚀 Action

### **1. Data Procurement & Integration**
- Collected data from multiple sources — sales, purchases, inventory, and vendor invoices.
- Stored standardized datasets in a **SQL relational database** for integrity and scalability.
- Established connections between Power BI and the SQL database for live analytics.

### **2. Data Cleaning & Transformation**
- Utilized **Python (Pandas, NumPy, and logging modules)** for:
  - Handling missing, inconsistent, and duplicate data.
  - Validating data types and schema consistency.
  - Implementing **log capturing** for every data cleaning operation to ensure traceability.
- Used **Excel** for preliminary validation and cross-verification of aggregated results.

### **3. Data Modeling (Power BI)**
- Developed a **star-schema model** with key dimension and fact tables:
  - **Dimensions:** Product, Vendor, Store, Calendar  
  - **Facts:** Sales_Data, Purchases, Vendor_Invoice, Inventory
- Established critical relationships:
  - `Purchases[Brand] → Purchase_Prices[Brand]`  
  - `Sales[VendorNumber] → Purchases[VendorNumber]`  
  - `VendorInvoice[vendorNumber] → Purchases[VendorNumber]`  
  

### **4. DAX Measures and KPIs**
- Created optimized **DAX measures** for business insights:
  - `Total Sales = SUM(SalesDollars)`
  - `Gross Profit = [Total Sales] - [Gross Cost]`
  - `Gross Margin % = DIVIDE([Gross Profit], [Total Sales])`
  
- Implemented error-handling logic and reusable measures aligned with enterprise reporting standards.

### **5. Dashboard Development**
- Designed **two interactive dashboards**:
  - 🟩 **Sales Dashboard:** Tracks Total Sales, quantity, profit, and brand performance.  
  - 🟦 **Vendor Dashboard:** Evaluates vendors efficiency.
- Used **gradient color themes**, **KPI cards**, and **trend visuals** for executive readability.

### **6. Logging & Governance**
- Implemented detailed **logging mechanisms in Python** for each transformation step (data extraction, cleaning, load status).
- Ensured **data lineage** from raw sources to final Power BI visuals, adhering to industry best practices.

---

## 💡 Result
- Built a **fully automated end-to-end analytics solution** from data procurement to dashboarding.  
- Delivered a Power BI system that offers:
  - **Sales KPIs:** Total Sales $441M | Total Quantity 32.9M | Gross Profit $129.7M.  
  - **Vendor KPIs:** Total Spend $139.4M | Quantity 10.4M | Profit $40.7M.  
- Reduced manual effort through automation and ensured complete transparency with logging and version control.
- Empowered management to make faster, data-driven decisions on performance, sourcing, and profitability.

---

## 🧮 Key Performance Indicators (KPIs)

### **Sales KPIs**
| KPI | Formula | Description |
|------|----------|-------------|
| Total Sales | `SUM(SalesDollars)` | Overall sales revenue |
| Gross Profit | `Total Sales - (SalesQuantity × PurchasePrice)` | Profit before expenses |
| Gross Margin % | `Gross Profit / Total Sales` | Profitability ratio |
| Average Selling Price | `SalesDollars / SalesQuantity` | Per-unit selling value |
| Inventory Turnover | `SalesQuantity / Avg(OnHand)` | Stock utilization rate |

### **Vendor KPIs**
| KPI | Formula | Description |
|------|----------|-------------|
| Total Purchase Spend | `SUM(Dollars)` | Total procurement cost |
| Average Lead Time | `DATEDIFF(PODate, ReceivingDate, DAY)` | Supplier delivery time |
| Invoice Approval Rate | `Approved / Total Invoices` | Approval efficiency |
| On-Time Delivery % | `OnTimePOs / TotalPOs` | Delivery punctuality |
| Payment Delay | `DATEDIFF(InvoiceDate, PayDate, DAY)` | Payment efficiency |

---

## 🗂️ Attachments / Links
> 🔗 [Dashboard (.pbit)](https://github.com/Yanglesh5139/vendor_analysis_sales_and_inventory/blob/main/dashboard/vendor_dashboard.pbit)  
> 🔗 [Dashboard PDF Report](https://github.com/Yanglesh5139/vendor_analysis_sales_and_inventory/blob/main/dashboard/vendor_dashboard.pdf)  
> 🔗 [Python Cleaning Script (.py)](https://github.com/Yanglesh5139/vendor_analysis_sales_and_inventory/blob/main/scripts/get_vendor_summary.py)  
> 🔗 [SQL Schema / Queries](https://github.com/Yanglesh5139/vendor_analysis_sales_and_inventory/blob/main/utils/json_files/queries.json)  
> 🖼️ [Sales Dashboard Preview](https://github.com/Yanglesh5139/vendor_analysis_sales_and_inventory/blob/main/images/vendor_sales_analysis_sales_dark_mood.png)  
> 🖼️ [Vendor Dashboard Preview](https://github.com/Yanglesh5139/vendor_analysis_sales_and_inventory/blob/main/images/vendor_sales_analysis_vendor.png)

---

## 🧠 Tools & Technologies
| Category | Tools |
|-----------|--------|
| **Data Cleaning & Logging** | Python (Pandas, NumPy, Logging) |
| **Database Management** | SQL (MySQL / PostgreSQL) |
| **Data Validation & Analysis** | Microsoft Excel |
| **Visualization & Modeling** | Power BI Desktop, Power Query, DAX |
| **Version Control** | Git, VS Code |
| **Documentation** | Markdown, README.md |

---

## 📈 Outcome Summary
This project showcases a **complete data analytics lifecycle** — from **data extraction, validation, and cleaning**, through **data modeling and visualization**, to **final business insight generation**.  
It adheres to **industry standards** for automation, logging, and governance — making it a reliable and scalable analytics solution.

---

*Prepared by — **Yanglesh Jaiswal***   
