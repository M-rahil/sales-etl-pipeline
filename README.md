# Sales Data ETL Pipeline

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline for processing sales data.

## Architecture
- Extract → Fetch data from source (S3 or CSV)
- Transform → Clean and process data using Pandas
- Load → Store data into PostgreSQL database

## Project Structure
- etl.py → Main pipeline controller
- extract.py → Data extraction
- transform.py → Data cleaning and processing
- load.py → Load data into database

## Technologies Used
- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- AWS S3 (optional)

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the pipeline:
   python etl.py

## Features
- Modular ETL design
- Data validation and cleaning
- Scalable pipeline structure

## Future Improvements
- Add Airflow scheduling
- Cloud deployment (AWS)
- Data visualization dashboard
