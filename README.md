# Dashboard Project
---
Capstone Project: Data Pipeline Project for Data Engineering Course

## Overview
1. Select a Dataset (see [examples](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_7_project/datasets.md))
1. Pipeline to DataLake
1. Pipeline to Data Warehouse
1. Transform the Data
1. Create a Dashboard

## Select a Dataset
Select a dataset that you're interested in (see [examples](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_7_project/datasets.md))


## Pipeline to DataLake
Create a pipeline for processing this dataset and putting it to a datalake

## Pipeline to Data Warehouse
Create a pipeline for moving the data from the lake to a data warehouse

## Transform the Data
Transform the data in the data warehouse: prepare it for the dashboard

## Create a Dashboard
You can build a dashboard with any of the tools shown in the course (Data Studio or Metabase) or any other BI tool of your choice. If you do use another tool, please specify and make sure that the dashboard is somehow accessible to your peers.

Your dashboard should contain at least two tiles, we suggest you include:
1. graph that shows the distribution of some categorical data
1. graph that shows the distribution of the data across a temporal line

Make sure that your graph is clear to understand by adding references and titles.

---

## Technologies
- Cloud Platform:
    - AWS
    - GCP
    - Azure
    - ...
- Infrastructure as Code (IaC): 
    - Terraform
    - Pulumi
    - Cloud Formation
    - ...
- Workflow Orchestration:
    - Airflow
    - Prefect
    - Luigi
    - ...
- Data Wareshouse:
    - BigQuery
    - Synapse Analytics
    - Snowflake
    - Redshift
    - ...
- Batch Processing:
    - Spark
    - Flink
    - AWS Batch
    - ...
- Stream Processing:
    - Kafka
    - Pulsar
    - Kinesis
    - ...

---

## Peer review criteria
Problem description
- 0 points: Problem is not described
- 1 point: Problem is described but shortly or not clearly
- 2 points: Problem is well described and it's clear what the problem the project solves

Cloud
- 0 points: Cloud is not used, things run only locally
- 2 points: The project is developed on the cloud
- 4 points: The project is developed on the clound and IaC tools are used

Data ingestion (choose either batch or stream)
- Batch / Workflow orchestration
    - 0 points: No workflow orchestration
    - 2 points: Partial workflow orchestration: some steps are orchestrated, some run manually
    - 4 points: End-to-end pipeline: multiple steps in the DAG, uploading data to data lake
- Stream
    - 0 points: No streaming system (like Kafka, Pulsar, etc)
    - 2 points: A simple pipeline with one consumer and one producer
    - 4 points: Using consumer/producers and streaming technologies (like Kafka streaming, Spark streaming, Flink, etc)

Data warehouse
- 0 points: No DWH is used
- 2 points: Tables are created in DWH, but not optimized
- 4 points: Tables are partitioned and clustered in a way that makes sense for the upstream queries (with explanation)

Transformations (dbt, spark, etc)
- 0 points: No tranformations
- 2 points: Simple SQL transformation (no dbt or similar tools)
- 4 points: Tranformations are defined with dbt, Spark or similar technologies

Dashboard
- 0 points: No dashboard
- 2 points: A dashboard with 1 tile
- 4 points: A dashboard with 2 tiles

Reproducibility
- 0 points: No instructions how to run code at all
- 2 points: Some instructions are there, but they are not complete
- 4 points: Instructions are clear, it's easy to run the code, and the code works

---
---
---
