# Project 2 ETL Data Transformation

# FILES & FOLDERS

* [erd](erd)
    * [erd](erd/erd.png) - data model
    * [data dictionary](erd/data_dictionary.pdf) - data dictionary
    * [schema](erd/schema.sql) - table schema for database
    * [query](erd/query.sql) - query to select data from tables
* [Resources](Resources) - input files
* [output](output) - transformed output files
* [notebooks] - *.ipynb files used for data transformation

# STEPS
* read data from extracted csv files from [Resources](Resources) folder
* transform data to generate relational model
* save tranformed data to csv file in [output](output) folder
* create a new database named **imdb_series_db** using **pgAdmin**
* create tables in **imdb_series_db** using  [schema](erd/schema.sql) file
* import csv files from [output](output) folder to related table
* query data using [query](erd/query.sql);
