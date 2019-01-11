-- Creating our database for project2
create database Health_Trend_Project_db;
use Health_Trend_Project_db;

-- creating National Health Expenditures table for data to be loaded into
Create Table National_Health_Expenditures_Data (
Year int primary key,
National_health_expenditures Numeric,
Health_consumption_expenditures Numeric,
Personal_health_care Numeric,
Hospital_care Numeric,
Professional_services Numeric,
Physician_and_clinical_services Numeric, 
Other_professional_services Numeric,
Dental_services Numeric, 
Other_health_residential_and_personal_care Numeric,
Home_health_care1 Numeric,
Nursing_care_facilities_and_care_retirement_communities1 Numeric,
Retail_outlet_sales_of_medical_products Numeric,
Prescription_drugs Numeric,
Durable_medical_equipment Numeric,
Other_nondurable_medical_products Numeric,
Government_administration2 Numeric, 
Net_cost_of_health_insurance3 Numeric,
Government_public_health_activities4 Numeric, 
Investment Numeric, 
Research5 Numeric,
Structures_and_equipment Numeric
);

Drop table if exists National_Health_Expenditures_Data;
select * from National_Health_Expenditures_Data;

-- creating the US_Chronic_Disease_Indicators_Data table for data to be loaded into
Create Table US_Chronic_Disease_Indicators_Data (
id INT AUTO_INCREMENT NOT NULL,
YearStart int,
YearEnd int,
LocationAbbr text,
LocationDesc text,
DataSource text,
Topic text,
Question text,
DataValueUnit text,
DataValueType text,
DataValue Numeric,
DataValueAlt Numeric, --
DatavalueFootnote text,
LowConfidenceLimit Numeric,
HighConfidenceLimit Numeric,
StratificationCategory1 text,
Stratification1 text,
Geo_Lat float,
Geo_Lon float,
ResponseID text,
LocationID int,
TopicID text,
QuestionID text,
DataValueTypeID text,
StratificationCategoryID1 text,
StratificationID1 text,
PRIMARY KEY (id)
);

Drop table if exists US_Chronic_Disease_Indicators_Data;
select * from US_Chronic_Disease_Indicators_Data;

