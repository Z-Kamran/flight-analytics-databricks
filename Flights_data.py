# Databricks notebook source
# MAGIC %md
# MAGIC Bronze  

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT id AS ID, TRIM(airport) AS Airport_Name, TRIM(departure_airport) AS Dept_Airport, TRIM(arrival_airport) AS Arr_Airport FROM groupbwt_airport_flight_delay_schedule_change_dataset.flights.flights

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT to_date(scheduled_time,'m/d/yyyy') AS Sch_Dept_Date, to_date(actual_time,'m/d/yyyy') AS Actual_Dept_Date, from_utc_timestamp(scheduled_time, 'America/Chicago') AS Sch_Dept_Time_CT, from_utc_timestamp(actual_time, 'America/Chicago') AS Actual_Dept_Time_CT, date_format(from_utc_timestamp(scheduled_time, 'America/Chicago'),'HH:mm') AS Sch_Dept_Time_CT, date_format(from_utc_timestamp(actual_time, 'America/Chicago'),'HH:mm') AS Actual_Dept_Time_CT  from groupbwt_airport_flight_delay_schedule_change_dataset.flights.flights
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT CONCAT(airlines_iata_code,flight_number) AS Flight_Number, TRIM(flight_status) AS Flight_Status, TRIM(gate) AS Gate, TRIM(aircraft_type) AS Aircraft FROM groupbwt_airport_flight_delay_schedule_change_dataset.flights.flights
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO data_from_kaggle.bronze.airlinecodes
# MAGIC VALUES
# MAGIC ('AA','AAL','American Airlines'),
# MAGIC ('DL','DAL','Delta Air Lines'),
# MAGIC ('UA','UAL','United Airlines'),
# MAGIC ('WN','SWA','Southwest Airlines'),
# MAGIC ('AS','ASA','Alaska Airlines'),
# MAGIC ('B6','JBU','JetBlue Airways'),
# MAGIC ('NK','NKS','Spirit Airlines'),
# MAGIC ('F9','FFT','Frontier Airlines'),
# MAGIC ('G4','AAY','Allegiant Air'),
# MAGIC ('HA','HAL','Hawaiian Airlines'),
# MAGIC ('AC','ACA','Air Canada'),
# MAGIC ('WS','WJA','WestJet'),
# MAGIC ('AM','AMX','Aeromexico'),
# MAGIC ('AV','AVA','Avianca'),
# MAGIC ('CM','CMP','Copa Airlines'),
# MAGIC ('LA','LAN','LATAM Airlines'),
# MAGIC ('IB','IBE','Iberia'),
# MAGIC ('BA','BAW','British Airways'),
# MAGIC ('VS','VIR','Virgin Atlantic'),
# MAGIC ('EI','EIN','Aer Lingus'),
# MAGIC ('AF','AFR','Air France'),
# MAGIC ('KL','KLM','KLM Royal Dutch Airlines'),
# MAGIC ('LH','DLH','Lufthansa'),
# MAGIC ('LX','SWR','Swiss International Air Lines'),
# MAGIC ('OS','AUA','Austrian Airlines'),
# MAGIC ('SN','BEL','Brussels Airlines'),
# MAGIC ('SK','SAS','Scandinavian Airlines'),
# MAGIC ('AY','FIN','Finnair'),
# MAGIC ('LO','LOT','LOT Polish Airlines'),
# MAGIC ('TP','TAP','TAP Air Portugal'),
# MAGIC ('TK','THY','Turkish Airlines'),
# MAGIC ('AZ','ITA','ITA Airways'),
# MAGIC ('FR','RYR','Ryanair'),
# MAGIC ('U2','EZY','easyJet'),
# MAGIC ('EW','EWG','Eurowings'),
# MAGIC ('DY','NAX','Norwegian Air Shuttle'),
# MAGIC ('EK','UAE','Emirates'),
# MAGIC ('QR','QTR','Qatar Airways'),
# MAGIC ('EY','ETD','Etihad Airways'),
# MAGIC ('SV','SVA','Saudia'),
# MAGIC ('MS','MSR','EgyptAir'),
# MAGIC ('RJ','RJA','Royal Jordanian'),
# MAGIC ('GF','GFA','Gulf Air'),
# MAGIC ('KU','KAC','Kuwait Airways'),
# MAGIC ('WY','OMA','Oman Air'),
# MAGIC ('AI','AIC','Air India'),
# MAGIC ('UK','VTI','Vistara'),
# MAGIC ('6E','IGO','IndiGo'),
# MAGIC ('SG','SEJ','SpiceJet'),
# MAGIC ('AK','AXM','AirAsia'),
# MAGIC ('MH','MAS','Malaysia Airlines'),
# MAGIC ('SQ','SIA','Singapore Airlines'),
# MAGIC ('TR','TGW','Scoot'),
# MAGIC ('TG','THA','Thai Airways'),
# MAGIC ('VN','HVN','Vietnam Airlines'),
# MAGIC ('PR','PAL','Philippine Airlines'),
# MAGIC ('GA','GIA','Garuda Indonesia'),
# MAGIC ('BI','RBA','Royal Brunei Airlines'),
# MAGIC ('CX','CPA','Cathay Pacific'),
# MAGIC ('CI','CAL','China Airlines'),
# MAGIC ('BR','EVA','EVA Air'),
# MAGIC ('CA','CCA','Air China'),
# MAGIC ('MU','CES','China Eastern'),
# MAGIC ('CZ','CSN','China Southern'),
# MAGIC ('HU','CHH','Hainan Airlines'),
# MAGIC ('MF','CXA','Xiamen Airlines'),
# MAGIC ('ZH','CSZ','Shenzhen Airlines'),
# MAGIC ('NH','ANA','All Nippon Airways'),
# MAGIC ('JL','JAL','Japan Airlines'),
# MAGIC ('KE','KAL','Korean Air'),
# MAGIC ('OZ','AAR','Asiana Airlines'),
# MAGIC ('QF','QFA','Qantas'),
# MAGIC ('JQ','JST','Jetstar Airways'),
# MAGIC ('NZ','ANZ','Air New Zealand'),
# MAGIC ('FJ','FJI','Fiji Airways'),
# MAGIC ('SA','SAA','South African Airways'),
# MAGIC ('KQ','KQA','Kenya Airways'),
# MAGIC ('ET','ETH','Ethiopian Airlines'),
# MAGIC ('AT','RAM','Royal Air Maroc'),
# MAGIC ('TU','TAR','Tunisair'),
# MAGIC ('AH','DAH','Air Algerie'),
# MAGIC ('RO','ROT','TAROM'),
# MAGIC ('FB','LZB','Bulgaria Air'),
# MAGIC ('OK','CSA','Czech Airlines'),
# MAGIC ('JU','ASL','Air Serbia'),
# MAGIC ('A3','AEE','Aegean Airlines'),
# MAGIC ('BT','BTI','Air Baltic'),
# MAGIC ('SU','AFL','Aeroflot'),
# MAGIC ('S7','SBI','S7 Airlines'),
# MAGIC ('UT','UTA','UTair'),
# MAGIC ('UA','UAI','Ukraine International Airlines'),
# MAGIC ('W6','W6U','Wind Jet')

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT f.id, f.airlines_iata_code, a.Airline
# MAGIC FROM groupbwt_airport_flight_delay_schedule_change_dataset.flights.flights f
# MAGIC LEFT JOIN data_from_kaggle.bronze.airlinecodes a
# MAGIC     on f.airlines_iata_code = a.IATA
# MAGIC LIMIT 1000

# COMMAND ----------

# MAGIC %md
# MAGIC SILVER

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     f.id AS ID,
# MAGIC
# MAGIC     -- Airports
# MAGIC     TRIM(f.departure_airport) AS Dept_Airport,
# MAGIC     TRIM(f.arrival_airport) AS Arr_Airport,
# MAGIC
# MAGIC     -- Dates
# MAGIC     TO_DATE(from_utc_timestamp(f.scheduled_time, 'America/Chicago')) AS Sch_Dept_Date,
# MAGIC     TO_DATE(from_utc_timestamp(f.actual_time, 'America/Chicago')) AS Actual_Dept_Date,
# MAGIC
# MAGIC       -- Time Only
# MAGIC     date_format(
# MAGIC         from_utc_timestamp(f.scheduled_time, 'America/Chicago'),
# MAGIC         'HH:mm'
# MAGIC     ) AS Sch_Dept_Time,
# MAGIC     date_format(
# MAGIC         from_utc_timestamp(f.actual_time, 'America/Chicago'),
# MAGIC         'HH:mm'
# MAGIC     ) AS Actual_Dept_Time,
# MAGIC
# MAGIC     -- Timestamps (Central Time)
# MAGIC     from_utc_timestamp(f.scheduled_time, 'America/Chicago') AS Sch_Dept_Time_CT,
# MAGIC     from_utc_timestamp(f.actual_time, 'America/Chicago') AS Actual_Dept_Time_CT,
# MAGIC
# MAGIC     -- Flight Details
# MAGIC     CONCAT(f.airlines_iata_code, f.flight_number) AS Flight_Number,
# MAGIC     TRIM(f.flight_status) AS Flight_Status,
# MAGIC     TRIM(f.gate) AS Gate,
# MAGIC     TRIM(f.aircraft_type) AS Aircraft,
# MAGIC     
# MAGIC     -- Airline Lookup
# MAGIC    a.Airline
# MAGIC
# MAGIC FROM groupbwt_airport_flight_delay_schedule_change_dataset.flights.flights f
# MAGIC
# MAGIC LEFT JOIN data_from_kaggle.bronze.airlinecodes a
# MAGIC     ON f.airlines_iata_code = a.IATA;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS flights_schema.silver.flights_list_table_silver
# MAGIC AS
# MAGIC SELECT
# MAGIC     f.id AS ID,
# MAGIC
# MAGIC     -- Airports
# MAGIC     TRIM(f.departure_airport) AS Dept_Airport,
# MAGIC     TRIM(f.arrival_airport) AS Arr_Airport,
# MAGIC
# MAGIC     -- Dates
# MAGIC     TO_DATE(from_utc_timestamp(f.scheduled_time, 'America/Chicago')) AS Sch_Dept_Date,
# MAGIC     TO_DATE(from_utc_timestamp(f.actual_time, 'America/Chicago')) AS Actual_Dept_Date,
# MAGIC
# MAGIC       -- Time Only
# MAGIC     date_format(
# MAGIC         from_utc_timestamp(f.scheduled_time, 'America/Chicago'),
# MAGIC         'HH:mm'
# MAGIC     ) AS Sch_Dept_Time,
# MAGIC     date_format(
# MAGIC         from_utc_timestamp(f.actual_time, 'America/Chicago'),
# MAGIC         'HH:mm'
# MAGIC     ) AS Actual_Dept_Time,
# MAGIC
# MAGIC     -- Timestamps (Central Time)
# MAGIC     from_utc_timestamp(f.scheduled_time, 'America/Chicago') AS Sch_Dept_Time_CT,
# MAGIC     from_utc_timestamp(f.actual_time, 'America/Chicago') AS Actual_Dept_Time_CT,
# MAGIC
# MAGIC     -- Flight Details
# MAGIC     CONCAT(f.airlines_iata_code, f.flight_number) AS Flight_Number,
# MAGIC     TRIM(f.flight_status) AS Flight_Status,
# MAGIC     TRIM(f.gate) AS Gate,
# MAGIC     TRIM(f.aircraft_type) AS Aircraft,
# MAGIC     
# MAGIC     -- Airline Lookup
# MAGIC    a.Airline
# MAGIC
# MAGIC FROM groupbwt_airport_flight_delay_schedule_change_dataset.flights.flights f
# MAGIC
# MAGIC LEFT JOIN data_from_kaggle.bronze.airlinecodes a
# MAGIC     ON f.airlines_iata_code = a.IATA;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Gold Tables

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE flights_schema.gold.total_flights AS
# MAGIC SELECT COUNT(ID) AS total_flights FROM flights_schema.silver.flights_list_table_silver

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Total flights KPI
# MAGIC SELECT Airline AS airline, count(ID) AS total_flights  from flights_schema.silver.flights_list_table_silver
# MAGIC GROUP BY airline
# MAGIC ORDER BY total_flights DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Average delay - minutes KPI
# MAGIC SELECT Airline AS airline, ROUND(AVG(timestampdiff(MINUTE, Sch_Dept_Time_CT, Actual_Dept_Time_CT)),1) AS delay_minutes FROM flights_schema.silver.flights_list_table_silver
# MAGIC GROUP BY airline
# MAGIC ORDER BY delay_minutes DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Average delay - minutes KPI/ Create Table
# MAGIC CREATE OR REPLACE TABLE flights_schema.gold.delay_minutes
# MAGIC AS SELECT Airline AS airline, ROUND(AVG(timestampdiff(MINUTE, Sch_Dept_Time_CT, Actual_Dept_Time_CT)),1) AS delay_minutes FROM flights_schema.silver.flights_list_table_silver
# MAGIC GROUP BY airline
# MAGIC ORDER BY delay_minutes DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- On-Time flights percentage KPI
# MAGIC WITH 
# MAGIC     flight_status_temp AS (
# MAGIC         SELECT Airline, CASE 
# MAGIC             WHEN Sch_dept_Time_CT IS NULL OR Actual_Dept_Time_CT IS NULL THEN 0
# MAGIC             ELSE
# MAGIC             ((unix_timestamp(Sch_dept_Time_CT)-unix_timestamp(Actual_Dept_Time_CT))/60) END AS delay_time FROM flights_schema.silver.flights_list_table_silver
# MAGIC     )
# MAGIC
# MAGIC SELECT Airline, ROUND((COUNT(CASE WHEN delay_time >=0 THEN 1 END)*100)/count(*),1) AS on_time_percentage FROM flight_status_temp
# MAGIC GROUP BY Airline
# MAGIC ORDER BY on_time_percentage DESC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- On-Time flights percentage KPI, CREATE TABLE
# MAGIC CREATE OR REPLACE TABLE flights_schema.gold.on_time_percentage
# MAGIC WITH 
# MAGIC     flight_status_temp AS (
# MAGIC         SELECT Airline, CASE 
# MAGIC             WHEN Sch_dept_Time_CT IS NULL OR Actual_Dept_Time_CT IS NULL THEN 0
# MAGIC             ELSE
# MAGIC             ((unix_timestamp(Sch_dept_Time_CT)-unix_timestamp(Actual_Dept_Time_CT))/60) END AS delay_time FROM flights_schema.silver.flights_list_table_silver
# MAGIC     )
# MAGIC
# MAGIC SELECT Airline, ROUND((COUNT(CASE WHEN delay_time >=0 THEN 1 END)*100)/count(*),1) AS on_time_percentage FROM flight_status_temp
# MAGIC GROUP BY Airline
# MAGIC ORDER BY on_time_percentage DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Delayed flights numbers KPI
# MAGIC WITH 
# MAGIC     flight_status_temp AS (
# MAGIC         SELECT Airline, CASE 
# MAGIC             WHEN Sch_dept_Time_CT IS NULL OR Actual_Dept_Time_CT IS NULL THEN 0
# MAGIC             ELSE
# MAGIC             ((unix_timestamp(Sch_dept_Time_CT)-unix_timestamp(Actual_Dept_Time_CT))/60) END AS delay_time FROM flights_schema.silver.flights_list_table_silver
# MAGIC     )
# MAGIC
# MAGIC SELECT Airline, COUNT(CASE WHEN delay_time <0 THEN 1 END) AS delay_flights_count FROM flight_status_temp
# MAGIC GROUP BY Airline
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Delayed flights numbers KPI, create table
# MAGIC CREATE OR REPLACE TABLE flights_schema.gold.delay_flights_count
# MAGIC WITH 
# MAGIC     flight_status_temp AS (
# MAGIC         SELECT Airline, CASE 
# MAGIC             WHEN Sch_dept_Time_CT IS NULL OR Actual_Dept_Time_CT IS NULL THEN 0
# MAGIC             ELSE
# MAGIC             ((unix_timestamp(Sch_dept_Time_CT)-unix_timestamp(Actual_Dept_Time_CT))/60) END AS delay_time FROM flights_schema.silver.flights_list_table_silver
# MAGIC     )
# MAGIC
# MAGIC SELECT Airline, COUNT(CASE WHEN delay_time <0 THEN 1 END) AS delay_flights_count FROM flight_status_temp
# MAGIC GROUP BY Airline

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC --- number of ailines KPI
# MAGIC SELECT COUNT(DISTINCT Airline) AS total_airlines FROM flights_schema.silver.flights_list_table_silver
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC --- number of ailines KPI, create table
# MAGIC CREATE OR REPLACE TABLE flights_schema.gold.airline_count
# MAGIC SELECT COUNT(DISTINCT Airline) AS total_airlines FROM flights_schema.silver.flights_list_table_silver
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- number of aiports KPI
# MAGIC SELECT COUNT (DISTINCT Airport) AS total_airports_served
# MAGIC     FROM (
# MAGIC         SELECT Arr_Airport AS Airport FROM flights_schema.silver.flights_list_table_silver
# MAGIC
# MAGIC         UNION
# MAGIC
# MAGIC         SELECT Dept_Airport AS Airport FROM flights_schema.silver.flights_list_table_silver)
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- number of aiports KPI, CREATE TABLE
# MAGIC create or replace table flights_schema.gold.airport_count
# MAGIC SELECT COUNT (DISTINCT Airport) AS total_airports_served
# MAGIC     FROM (
# MAGIC         SELECT Arr_Airport AS Airport FROM flights_schema.silver.flights_list_table_silver
# MAGIC
# MAGIC         UNION
# MAGIC
# MAGIC         SELECT Dept_Airport AS Airport FROM flights_schema.silver.flights_list_table_silver)
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC  --- number of unique routes
# MAGIC SELECT CONCAT(Dept_Airport, ' - ', Arr_Airport) AS route, COUNT(*) AS count_routes FROM flights_schema.silver.flights_list_table_silver
# MAGIC WHERE Sch_Dept_Time_CT IS NOT NULL AND Actual_Dept_Time_CT IS NOT NULL
# MAGIC GROUP BY route
# MAGIC ORDER BY count_routes DESC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC  --- number of unique routes, create Table
# MAGIC  create or replace table flights_schema.gold.route_count
# MAGIC SELECT CONCAT(Dept_Airport, ' - ', Arr_Airport) AS route, COUNT(*) AS count_routes FROM flights_schema.silver.flights_list_table_silver
# MAGIC WHERE Sch_Dept_Time_CT IS NOT NULL AND Actual_Dept_Time_CT IS NOT NULL
# MAGIC GROUP BY route
# MAGIC ORDER BY count_routes DESC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- delayed routes KPI 
# MAGIC     WITH 
# MAGIC     flight_routes AS (
# MAGIC         SELECT concat(Dept_Airport, ' - ', Arr_Airport) AS route FROM flights_schema.silver.flights_list_table_silver
# MAGIC         WHERE Sch_Dept_Time_CT IS NOT NULL AND Actual_Dept_Time_CT IS NOT NULL AND (unix_timestamp(Sch_Dept_Time_CT)-unix_timestamp(Actual_Dept_Time_CT))/60 <0
# MAGIC     )
# MAGIC     SELECT route, COUNT(*) AS number_of_delay FROM flight_routes
# MAGIC     GROUP BY route
# MAGIC     ORDER BY number_of_delay DESC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- delayed routes KPI , create table
# MAGIC create or replace table flights_schema.gold.delayed_routes
# MAGIC     WITH 
# MAGIC     flight_routes AS (
# MAGIC         SELECT concat(Dept_Airport, ' - ', Arr_Airport) AS route FROM flights_schema.silver.flights_list_table_silver
# MAGIC         WHERE Sch_Dept_Time_CT IS NOT NULL AND Actual_Dept_Time_CT IS NOT NULL AND (unix_timestamp(Sch_Dept_Time_CT)-unix_timestamp(Actual_Dept_Time_CT))/60 <0
# MAGIC     )
# MAGIC     SELECT route, COUNT(*) AS number_of_delay FROM flight_routes
# MAGIC     GROUP BY route
# MAGIC     ORDER BY number_of_delay DESC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC --- percentage of delayed routes
# MAGIC WITH route_totals AS (
# MAGIC     SELECT
# MAGIC         Dept_Airport,
# MAGIC         Arr_Airport,
# MAGIC         COUNT(*) AS Total_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL
# MAGIC     GROUP BY Dept_Airport, Arr_Airport
# MAGIC ),
# MAGIC
# MAGIC route_delays AS (
# MAGIC     SELECT
# MAGIC         Dept_Airport,
# MAGIC         Arr_Airport,
# MAGIC         COUNT(*) AS Delayed_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL
# MAGIC       AND (
# MAGIC             unix_timestamp(Actual_Dept_Time_CT)
# MAGIC             - unix_timestamp(Sch_Dept_Time_CT)
# MAGIC           ) / 60 > 0
# MAGIC     GROUP BY Dept_Airport, Arr_Airport
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     CONCAT(t.Dept_Airport, ' - ', t.Arr_Airport) AS Route,
# MAGIC     t.Total_Flights,
# MAGIC     COALESCE(d.Delayed_Flights, 0) AS Delayed_Flights,
# MAGIC     ROUND(
# MAGIC         COALESCE(d.Delayed_Flights, 0) * 100.0 /
# MAGIC         t.Total_Flights,
# MAGIC         2
# MAGIC     ) AS Delay_Percentage
# MAGIC FROM route_totals t
# MAGIC LEFT JOIN route_delays d
# MAGIC     ON t.Dept_Airport = d.Dept_Airport
# MAGIC    AND t.Arr_Airport = d.Arr_Airport
# MAGIC ORDER BY Delay_Percentage DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC --- percentage of delayed routes, create table
# MAGIC create or replace table flights_schema.gold.delayed_routes_percentage
# MAGIC WITH route_totals AS (
# MAGIC     SELECT
# MAGIC         Dept_Airport,
# MAGIC         Arr_Airport,
# MAGIC         COUNT(*) AS Total_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL
# MAGIC     GROUP BY Dept_Airport, Arr_Airport
# MAGIC ),
# MAGIC
# MAGIC route_delays AS (
# MAGIC     SELECT
# MAGIC         Dept_Airport,
# MAGIC         Arr_Airport,
# MAGIC         COUNT(*) AS Delayed_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL
# MAGIC       AND (
# MAGIC             unix_timestamp(Actual_Dept_Time_CT)
# MAGIC             - unix_timestamp(Sch_Dept_Time_CT)
# MAGIC           ) / 60 > 0
# MAGIC     GROUP BY Dept_Airport, Arr_Airport
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     CONCAT(t.Dept_Airport, ' - ', t.Arr_Airport) AS Route,
# MAGIC     t.Total_Flights,
# MAGIC     COALESCE(d.Delayed_Flights, 0) AS Delayed_Flights,
# MAGIC     ROUND(
# MAGIC         COALESCE(d.Delayed_Flights, 0) * 100.0 /
# MAGIC         t.Total_Flights,
# MAGIC         2
# MAGIC     ) AS Delay_Percentage
# MAGIC FROM route_totals t
# MAGIC LEFT JOIN route_delays d
# MAGIC     ON t.Dept_Airport = d.Dept_Airport
# MAGIC    AND t.Arr_Airport = d.Arr_Airport
# MAGIC ORDER BY Delay_Percentage DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Best Performance score, where every delayed flight is -0.5 and every on-time flight is +1
# MAGIC WITH airline_stats AS (
# MAGIC     SELECT
# MAGIC         Airline,
# MAGIC         COUNT(*) AS Total_Flights,
# MAGIC         SUM(
# MAGIC             CASE
# MAGIC                 WHEN (unix_timestamp(Actual_Dept_Time_CT) -
# MAGIC                       unix_timestamp(Sch_Dept_Time_CT)) / 60 > 0
# MAGIC                 THEN 1
# MAGIC                 ELSE 0
# MAGIC             END
# MAGIC         ) AS Delayed_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL AND Airline IS NOT NULL
# MAGIC     GROUP BY Airline
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     Airline,
# MAGIC     Total_Flights,
# MAGIC     Delayed_Flights,
# MAGIC     ((Total_Flights)*1 - (Delayed_Flights)*0.5) AS Performance_Score
# MAGIC FROM airline_stats
# MAGIC ORDER BY Performance_Score DESC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Best Performance score, where every delayed flight is -0.5 and every on-time flight is +1, create table
# MAGIC create or replace table flights_schema.gold.best_performance
# MAGIC WITH airline_stats AS (
# MAGIC     SELECT
# MAGIC         Airline,
# MAGIC         COUNT(*) AS Total_Flights,
# MAGIC         SUM(
# MAGIC             CASE
# MAGIC                 WHEN (unix_timestamp(Actual_Dept_Time_CT) -
# MAGIC                       unix_timestamp(Sch_Dept_Time_CT)) / 60 > 0
# MAGIC                 THEN 1
# MAGIC                 ELSE 0
# MAGIC             END
# MAGIC         ) AS Delayed_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL AND Airline IS NOT NULL
# MAGIC     GROUP BY Airline
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     Airline,
# MAGIC     Total_Flights,
# MAGIC     Delayed_Flights,
# MAGIC     ((Total_Flights)*1 - (Delayed_Flights)*0.5) AS Performance_Score
# MAGIC FROM airline_stats
# MAGIC ORDER BY Performance_Score DESC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Worst Performance score, where every delayed flight is -0.5 and every on-time flight is +1
# MAGIC WITH airline_stats AS (
# MAGIC     SELECT
# MAGIC         Airline,
# MAGIC         COUNT(*) AS Total_Flights,
# MAGIC         SUM(
# MAGIC             CASE
# MAGIC                 WHEN (unix_timestamp(Actual_Dept_Time_CT) -
# MAGIC                       unix_timestamp(Sch_Dept_Time_CT)) / 60 > 0
# MAGIC                 THEN 1
# MAGIC                 ELSE 0
# MAGIC             END
# MAGIC         ) AS Delayed_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL AND Airline IS NOT NULL
# MAGIC     GROUP BY Airline
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     Airline,
# MAGIC     Total_Flights,
# MAGIC     Delayed_Flights,
# MAGIC     ((Total_Flights)*1 - (Delayed_Flights)*0.5) AS Performance_Score
# MAGIC FROM airline_stats
# MAGIC ORDER BY Performance_Score ASC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Worst Performance score, where every delayed flight is -0.5 and every on-time flight is +1, create table
# MAGIC create or replace table flights_schema.gold.worst_performance
# MAGIC WITH airline_stats AS (
# MAGIC     SELECT
# MAGIC         Airline,
# MAGIC         COUNT(*) AS Total_Flights,
# MAGIC         SUM(
# MAGIC             CASE
# MAGIC                 WHEN (unix_timestamp(Actual_Dept_Time_CT) -
# MAGIC                       unix_timestamp(Sch_Dept_Time_CT)) / 60 > 0
# MAGIC                 THEN 1
# MAGIC                 ELSE 0
# MAGIC             END
# MAGIC         ) AS Delayed_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL AND Airline IS NOT NULL
# MAGIC     GROUP BY Airline
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     Airline,
# MAGIC     Total_Flights,
# MAGIC     Delayed_Flights,
# MAGIC     ((Total_Flights)*1 - (Delayed_Flights)*0.5) AS Performance_Score
# MAGIC FROM airline_stats
# MAGIC ORDER BY Performance_Score ASC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC --- airlines prone to delay
# MAGIC WITH airline_stats AS (
# MAGIC     SELECT
# MAGIC         Airline,
# MAGIC         COUNT(*) AS Total_Flights,
# MAGIC         SUM(
# MAGIC             CASE
# MAGIC                 WHEN (unix_timestamp(Actual_Dept_Time_CT) -
# MAGIC                       unix_timestamp(Sch_Dept_Time_CT)) / 60 > 0
# MAGIC                 THEN 1
# MAGIC                 ELSE 0
# MAGIC             END
# MAGIC         ) AS Delayed_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL
# MAGIC     GROUP BY Airline
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     Airline,
# MAGIC     Total_Flights,
# MAGIC     Delayed_Flights,
# MAGIC     ROUND(Delayed_Flights * 100.0 / Total_Flights, 2) AS Delay_Percentage
# MAGIC FROM airline_stats
# MAGIC ORDER BY Delay_Percentage DESC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC --- airlines prone to delay, create table
# MAGIC create or replace table flights_schema.gold.airlines_prone_to_delay
# MAGIC WITH airline_stats AS (
# MAGIC     SELECT
# MAGIC         Airline,
# MAGIC         COUNT(*) AS Total_Flights,
# MAGIC         SUM(
# MAGIC             CASE
# MAGIC                 WHEN (unix_timestamp(Actual_Dept_Time_CT) -
# MAGIC                       unix_timestamp(Sch_Dept_Time_CT)) / 60 > 0
# MAGIC                 THEN 1
# MAGIC                 ELSE 0
# MAGIC             END
# MAGIC         ) AS Delayed_Flights
# MAGIC     FROM flights_schema.silver.flights_list_table_silver
# MAGIC     WHERE Sch_Dept_Time_CT IS NOT NULL
# MAGIC       AND Actual_Dept_Time_CT IS NOT NULL
# MAGIC     GROUP BY Airline
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     Airline,
# MAGIC     Total_Flights,
# MAGIC     Delayed_Flights,
# MAGIC     ROUND(Delayed_Flights * 100.0 / Total_Flights, 2) AS Delay_Percentage
# MAGIC FROM airline_stats
# MAGIC ORDER BY Delay_Percentage DESC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Bussiest Arrival Airport
# MAGIC SELECT Arr_Airport AS arrival_airport, COUNT(*) AS total_flights FROM flights_schema.silver.flights_list_table_silver
# MAGIC GROUP BY arrival_airport
# MAGIC ORDER BY COUNT(*) DESC
# MAGIC LIMIT 5

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Bussiest Arrival Airport, create table
# MAGIC create or replace table flights_schema.gold.busiest_arrival_airport 
# MAGIC SELECT Arr_Airport AS arrival_airport, COUNT(*) AS total_flights FROM flights_schema.silver.flights_list_table_silver
# MAGIC GROUP BY arrival_airport
# MAGIC ORDER BY COUNT(*) DESC
# MAGIC LIMIT 5

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Bussiest Departure Airport
# MAGIC SELECT Dept_Airport AS departure_airport, COUNT(*) AS total_flights FROM flights_schema.silver.flights_list_table_silver
# MAGIC GROUP BY departure_airport
# MAGIC ORDER BY COUNT(*) DESC
# MAGIC LIMIT 5

# COMMAND ----------

# MAGIC %sql
# MAGIC --- Bussiest Departure Airport, create table
# MAGIC create or replace table flights_schema.gold.busiest_departure_airport
# MAGIC SELECT Dept_Airport AS departure_airport, COUNT(*) AS total_flights FROM flights_schema.silver.flights_list_table_silver
# MAGIC GROUP BY departure_airport
# MAGIC ORDER BY COUNT(*) DESC
# MAGIC LIMIT 5

# COMMAND ----------

# MAGIC %sql
# MAGIC --- gold fact table for drilling through
# MAGIC SELECT Airline, Flight_Number, concat(Dept_Airport, " - ", Arr_Airport) AS route, Sch_Dept_Time_CT, Actual_Dept_Time_CT, (unix_timestamp(Actual_Dept_Time_CT) - unix_timestamp(Sch_Dept_Time_CT))/60 AS delayed_minutes, CASE WHEN (unix_timestamp(Actual_Dept_Time_CT) - unix_timestamp(Sch_Dept_Time_CT)) > 0 THEN 'Delayed' ELSE 'On Time' END AS Flight_Status 
# MAGIC FROM flights_schema.silver.flights_list_table_silver

# COMMAND ----------

# MAGIC %sql
# MAGIC --- gold fact table for drilling through, create table
# MAGIC create or replace table flights_schema.gold.facts_drill_through
# MAGIC SELECT Airline, Flight_Number, concat(Dept_Airport, " - ", Arr_Airport) AS route, Sch_Dept_Time_CT, Actual_Dept_Time_CT, (unix_timestamp(Actual_Dept_Time_CT) - unix_timestamp(Sch_Dept_Time_CT))/60 AS delayed_minutes, CASE WHEN (unix_timestamp(Actual_Dept_Time_CT) - unix_timestamp(Sch_Dept_Time_CT)) > 0 THEN 'Delayed' ELSE 'On Time' END AS Flight_Status 
# MAGIC FROM flights_schema.silver.flights_list_table_silver