# Project 1

## Overview
Write a Big Data Script that uses the Pandas API for Spark or Dask

## Setup
Use make to install required packages listed in ```requirements.txt```.
```bash
make
```
## Microsoft Azure and Databricks
The Databricks service is hold on Microsoft Azure.

These four secrests need to be set up to connect with Databricks.
```DATABRICKS_HOST```
```DATABRICKS_HTTP_PATH```
```DATABRICKS_SERVER_HOSTNAME```
```DATABRICKS_TOKEN```


## Test Databricks Connection
To test the connection to Databricks, run the command below. If success, the cluster information will be printed.
```
databricks clusters list --output JSON
```

## Build CLI with Click
Click is used to build a CLI interface .
To execute default query:
```
python hello_query_sql_db.py cli-query
```

## Hook up to FastAPI
To access the service hooked up by FastAPI, run the following command.

```
python fastapi-app.py
```

Add ```/query``` at the end of the url, the server will run default query and show the result.
