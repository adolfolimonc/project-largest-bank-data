# Acquiring and Processing Information on the World's Largest Banks

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fadolfolimonc%2Fpython-project-for-data-engineering&label=Visitors&countColor=%230d76a8&style=flat&labelStyle=none)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-green.svg)](https://shields.io/)

## Content
This repository contains a project I developed for the course Python Project for Data Engineering, titled "Final Project: Acquiring and Processing Information on the World's Largest Banks."

### Why?
* I uploaded this to track my learning in Data Engineering.
  
### Usage
* Please  feel free to use it if you feel stuck during this practice. If so, I encourage you to try it to solve yourself first. If you can't, try to understand the code.

## The goal of this project
* Extract data from the world's largest banks by using web scraping and the Requests API.
* Transform the data to the given currencies: GBP, EUR, INR.
* Load the transformed data in a CSV file and also to a SQLite database.
* Execute queries to retrieved solicited information from the table.

## Project Scenario
You have been hired as a data engineer by research organization. Your boss has asked you to create a code that can be used to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR and INR as well, in accordance with the exchange rate information that has been made available to you as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.

Your job is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.


Particulars of the code to be made have been shared below. 

| Parameter                               | Value                                                                                                                             |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Code name                               | `banks_project.py`                                                                                                                |
| Data URL                                | `https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks`                                  |
| Exchange rate CSV path                  | `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv` |
| Table Attributes (upon Extraction only) | `Name`, `MC_USD_Billion`                                                                                                          |
| Table Attributes (final)                | `Name`, `MC_USD_Billion`, `MC_GBP_Billion`, `MC_EUR_Billion`, `MC_INR_Billion`                                                    |
| Output CSV Path                         | `./Largest_banks_data.csv`                                                                                                        |
| Database name                           | `Banks.db`                                                                                                                        |
| Table name                              | `Largest_banks`                                                                                                                   |
| Log file                                | `code_log.txt`                                                                                                                    |

## Tasks
1. Logging function: Write the function to log the progress of the code, `log_progress()`. The function accepts the message to be logged and enters it to a text file code_log.txt.
2. Extraction of data: Analyze the webpage on the given URL and identify the position of the required table under the heading By market capitalization. Write the function `extract()` to retrieve the information of the table to a Pandas data frame.
3. Transformation of data: Convert the exchange rate CSV file to a dictionary. Add three different columns to the dataframe `MC_GBP_Billion`, `MC_EUR_Billion` and `MC_INR_Billion` each containing the content of `MC_USD_Billion` scaled by the corresponding exchange rate factor. Remember to round the resulting data to 2 decimal places.
4. Loading to CSV: Write the function to load the transformed data frame to a CSV file, like `load_to_csv()`, in the path mentioned in the project scenario.
5. Loading to Database: `Write the function` to load the transformed data frame to an SQL database, like, `load_to_db()`. Use the database and table names as mentioned in the project scenario.
6. Function to Run queries on Database: Write the function run_queries() that accepts the query statement, and the SQLite3 Connection object, and generates the output of the query. The query statement should be printed along with the query output.
7. Verify log entries: After updating all the `log_progress()` function calls, you have to run the code for a final execution. However, you will first have to remove the `code_log.txt` file, that would have been created and updated throughout the multiple executions of the code in this lab. You may remove the file using the following command on a terminal.

## Follow me on LinkedIn!

[adolfolimonc](https://www.linkedin.com/in/adolfolimonc/)

## Acknoledgments
* IBM Skills Network © IBM Corporation 2025. All rights reserved.
* [Pravin Regismond](https://github.com/pregismond): inspired my README.md file ~~might have copied the structure~~:laughing:
