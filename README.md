# Retail Data Warehouse Project

A complete, production-ready data warehouse implementation for retail analytics using dimensional modeling (Kimball methodology).

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Data Model](#data-model)
- [Getting Started](#getting-started)
- [ETL Pipeline](#etl-pipeline)
- [Data Quality](#data-quality)
- [Business Intelligence](#business-intelligence)

## 🎯 Project Overview

### Business Objectives

This data warehouse enables:
- Real-time sales analytics and reporting
- Customer segmentation and lifetime value analysis
- Inventory optimization and forecasting
- Store performance comparison
- Promotional campaign effectiveness tracking
- Executive KPI dashboards

### Key Features

- ✅ Star schema design for optimal query performance
- ✅ Slowly Changing Dimensions (SCD Type 1, 2)
- ✅ Incremental ETL with full audit trail
- ✅ Automated data quality validation
- ✅ Pre-built aggregate tables for fast reporting
- ✅ Apache Airflow orchestration
- ✅ Comprehensive business intelligence queries

## 🏗️ Architecture

### Data Flow

1. **Extract**: Pull data from source systems (POS, CRM, Inventory)
2. **Stage**: Load raw data into staging tables
3. **Transform**: Apply business rules, cleanse data, implement SCD
4. **Load**: Insert/update dimension and fact tables
5. **Aggregate**: Update pre-aggregated summary tables
6. **Validate**: Run data quality checks
7. **Refresh**: Update BI tool caches

## 💻 Technology Stack

- **Database**: PostgreSQL 14+ / Snowflake / Amazon Redshift
- **ETL**: Python 3.9+ with Pandas, SQLAlchemy
- **Orchestration**: Apache Airflow 2.5+
- **BI Tools**: Tableau / Power BI

## 📊 Data Model

### Star Schema Overview

**Fact Tables:**
- `fact_sales` - Sales transactions
- `fact_inventory` - Daily inventory snapshots

**Dimension Tables:**
- `dim_date` - Calendar and fiscal dates (Type 0)
- `dim_product` - Product master (Type 2 SCD)
- `dim_store` - Store information (Type 2 SCD)
- `dim_customer` - Customer profiles (Type 2 SCD)
- `dim_employee` - Employee data (Type 2 SCD)
- `dim_promotion` - Promotional campaigns (Type 1 SCD)

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.9+
python --version

# PostgreSQL 14+
psql --version

# Apache Airflow 2.5+
airflow version
```

### Installation

1. **Create database schemas**
```bash
psql -U your_user -d retail_dw -f create_dw_schema.sql
```

2. **Set up Python environment**
```bash
pip install -r requirements.txt
```

3. **Configure database connections**
Edit connection details in `etl_pipeline.py` and `airflow_dag.py`

## 🔄 ETL Pipeline

### Daily ETL Process

The ETL runs daily at 2 AM with these steps:

1. Pre-checks (5 min)
2. Dimension Loading (15 min)
3. Fact Loading (30 min)
4. Aggregation (10 min)
5. Quality Checks (5 min)
6. Post-processing (5 min)

**Total Runtime**: ~70 minutes

## ✅ Data Quality

Quality checks include:
- Completeness (null values)
- Accuracy (business rules)
- Consistency (referential integrity)
- Timeliness (data freshness)

## 📈 Business Intelligence

Sample queries available for:
- Sales performance analysis
- Store comparison
- Customer segmentation
- Inventory monitoring
- Promotional effectiveness
- Executive KPIs

## 📁 Project Files

- `retail_dw_project.md` - Complete project documentation
- `create_dw_schema.sql` - Database schema DDL
- `etl_pipeline.py` - Python ETL implementation
- `airflow_dag.py` - Airflow orchestration
- `sample_bi_queries.sql` - BI query collection

## 📝 Documentation

See `retail_dw_project.md` for complete documentation including:
- Detailed architecture
- Implementation timeline
- Monitoring procedures
- Maintenance guidelines

---

**Version**: 1.0.0  
**Last Updated**: 2024-01-15  
**Maintained By**: Data Engineering Team
