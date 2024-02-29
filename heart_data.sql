USE heart_prediction;

CREATE TABLE heart_data (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    age FLOAT,
    anaemia BOOLEAN,
    creatinine_phosphokinase INT,
    diabetes BOOLEAN,
    ejection_fraction INT,
    high_blood_pressure BOOLEAN,
    platelets FLOAT,
    serum_creatinine FLOAT,
    serum_sodium INT,
    sex BOOLEAN,  -- Assuming 1 for male and 0 for female
    smoking BOOLEAN,
    time INT,
    death_event BOOLEAN
);

LOAD DATA LOCAL INFILE 'C:\\Users\\olehs\\Desktop\\heart_failure_clinical_records_dataset.csv'
INTO TABLE heart_data
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time, death_event);

SELECT * FROM heart_data

# --

# Identifying missing values

SELECT 'missing_age_count' AS missing_type, COUNT(*) AS count FROM heart_data WHERE age IS NULL
UNION ALL
SELECT 'missing_anaemia_count', COUNT(*) FROM heart_data WHERE anaemia IS NULL
UNION ALL
SELECT 'missing_creatinine_count', COUNT(*) FROM heart_data WHERE creatinine_phosphokinase IS NULL
UNION ALL
SELECT 'missing_diabetes_count', COUNT(*) FROM heart_data WHERE diabetes IS NULL
UNION ALL
SELECT 'missing_ejection_count', COUNT(*) FROM heart_data WHERE ejection_fraction IS NULL
UNION ALL
SELECT 'missing_blood_count', COUNT(*) FROM heart_data WHERE high_blood_pressure IS NULL
UNION ALL
SELECT 'missing_platelets_count', COUNT(*) FROM heart_data WHERE platelets IS NULL
UNION ALL
SELECT 'missing_serumcrea_count', COUNT(*) FROM heart_data WHERE serum_creatinine IS NULL
UNION ALL
SELECT 'missing_serumsodium_count', COUNT(*) FROM heart_data WHERE serum_sodium IS NULL
UNION ALL
SELECT 'missing_sex_count', COUNT(*) FROM heart_data WHERE sex IS NULL
UNION ALL
SELECT 'missing_smoking_count', COUNT(*) FROM heart_data WHERE smoking IS NULL
UNION ALL
SELECT 'missing_time_count', COUNT(*) FROM heart_data WHERE time IS NULL
UNION ALL
SELECT 'missing_death_count', COUNT(*) FROM heart_data WHERE death_event IS NULL;

# Handling missing values (there are none on this dataset but would look something like:)

UPDATE heart_data SET age = (SELECT AVG(age) FROM heart_data WHERE age IS NOT NULL) WHERE age IS NULL;

# Identifying outliers

SET @rowindex := -1;

SELECT
    patient_id,
    platelets,
    CASE
        WHEN platelets < (@Q1 - 1.5 * (@Q3 - @Q1)) OR platelets > (@Q3 + 1.5 * (@Q3 - @Q1)) THEN 'Outlier'
        ELSE 'Normal'
    END AS outlier_status
FROM
    (SELECT
        patient_id,
        platelets,
        @Q1 := (SELECT platelets FROM (SELECT @rownum:=@rownum+1 AS `row_number`, d.platelets FROM heart_prediction.heart_data d, (SELECT @rownum:=0) r ORDER BY d.platelets) AS sorted WHERE `row_number` = FLOOR(0.25 * @rowindex)) AS Q1,
        @Q3 := (SELECT platelets FROM (SELECT @rownum:=@rownum+1 AS `row_number`, d.platelets FROM heart_prediction.heart_data d, (SELECT @rownum:=0) r ORDER BY d.platelets) AS sorted WHERE `row_number` = CEIL(0.75 * @rowindex)) AS Q3
    FROM heart_prediction.heart_data, (SELECT @rowindex:=COUNT(*) FROM heart_prediction.heart_data) AS rowCount) AS withQuartiles;

# Checking for inconsistencies (there can be many different ones, depends on what kind of data we are look at, the industry, laws, etc etc, this case I will just look for a underaged people that should not be in the dataset due to privacy laws)

SELECT * FROM heart_data WHERE age < 18;

# --

# Average Values by Outcome / Mean values of key metrics grouped by the 'death_event' outcome

SELECT 
    death_event,
    AVG(age) AS avg_age,
    AVG(creatinine_phosphokinase) AS avg_cpk,
    AVG(ejection_fraction) AS avg_ejection_fraction,
    AVG(platelets) AS avg_platelets,
    AVG(serum_creatinine) AS avg_serum_creatinine,
    AVG(serum_sodium) AS avg_serum_sodium
FROM 
    heart_data
GROUP BY 
    death_event;
    
# Correlation between age, serum creatinine and ejection fraction with mortality

SELECT 
    CONCAT(age_group, ' ', serum_creatinine_level) AS age_and_creatinine_group,
    ejection_fraction_status,
    AVG(death_event) AS mortality_rate
FROM 
    (SELECT 
        CASE 
            WHEN age < 50 THEN 'Under 50'
            WHEN age BETWEEN 50 AND 70 THEN '50-70'
            ELSE 'Over 70'
        END AS age_group,
        CASE 
            WHEN serum_creatinine <= 1.0 THEN 'Low'
            WHEN serum_creatinine > 1.0 AND serum_creatinine <= 1.5 THEN 'Moderate'
            ELSE 'High'
        END AS serum_creatinine_level,
        CASE 
            WHEN ejection_fraction < 40 THEN 'Reduced EF'
            ELSE 'Normal EF'
        END AS ejection_fraction_status,
        death_event
    FROM 
        heart_data) AS derived_table
GROUP BY 
    age_and_creatinine_group, ejection_fraction_status
ORDER BY 
    FIELD(age_and_creatinine_group, 'Under 50 High', 'Under 50 Moderate', 'Under 50 Low', '50-70 High', '50-70 Moderate', '50-70 Low', 'Over 70 High', 'Over 70 Moderate', 'Over 70 Low'),
    ejection_fraction_status;

    













