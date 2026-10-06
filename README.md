# Flight Analytics Project

## Overview
This project demonstrates an end-to-end data engineering and analytics workflow using Databricks and SQL.

The project follows a Medallion Architecture:
- Bronze Layer (Raw Data)
- Silver Layer (Cleaned Data)
- Gold Layer (Business KPIs)

## Tools Used
- Databricks
- SQL
- Apache Spark
- Tableau
- GitHub

## Business Objectives
Analyze flight performance and identify:
- Total Flights
- Delayed Flights
- On-Time Performance
- Average Delay Minutes
- Top Delayed Routes
- Best Performing Airlines
- Worst Performing Airlines
- 
# Dataset Description

Source:
Commercial flight operations dataset

Fields:

- Flight_Number
- Airline
- Departure_Airport
- Arrival_Airport
- Scheduled_Departure_Time
- Actual_Departure_Time
- Flight_Status
- Aircraft
- Gate

Records:
1000+ flight records

## Architecture
Documentation/Architecture.png

## Key Insights

- Identified the routes with the highest delay volume.
- Measured airline performance using delay rates.
- Calculated on-time performance percentages.
- Built KPI-ready Gold tables for reporting.
- Developed dashboard-ready data models.

## Dashboard


## Author
Kamran Zhwandoon
