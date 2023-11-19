# Project 2 ETL Data Transformation

# FILES & FOLDERS

* 1. [erd](erd)
    * [erd](erd/erd.png) - data model
    * [data dictionary](erd/data_dictionary.pdf) - data dictionary
    * [schema](erd/schema.sql) - table schema for database
    * [query](erd/query.sql) - query to select data from tables
* 2. [Resources](Resources) - input files
* 3. [output](output) - transformed output files
* 4. [notebooks] - *.ipynb files used for data transformation

# STEPS
* 1. read data from extracted csv files from [Resources](Resources) folder
* 2. transform data to generate relational model
* 3. save tranformed data to csv file in [output](output) folder
* 4. create a new database named **imdb_series_db** using **pgAdmin**
* 5. create tables in **imdb_series_db** using  [schema](erd/schema.sql) file
* 6. import csv files from [output](output) folder to related table
* 7. query data using [query](erd/query.sql);
