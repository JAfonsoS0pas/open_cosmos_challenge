# DataCosmos Backend Challenge Project

## Introduction

This is my solution to the DataCosmos backend challenge in this README you can find how to set up the project, how to test it for yourself and some final considerations

## Setup

This project is completely dockerized to run it simply
1. **Clone the repository:**

   ```bash
   git clone git clone git@github.com:JAfonsoS0pas/open_cosmos_challenge.git
   cd yourproject
   ```
2. **Build and run the Docker containers:**
   ```bash
   docker-compose up -d --build
   ```
3. **Run Migrations:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```
4. **Create a superuser:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## Objective

Create a service which can 

- fetch the data exposed by the server included as a binary with the project files - see below for details on how to run the server
- store this in a persistent data store - there are no requirements on which type of data store to use, you may choose
- implement and apply the business rules around these data which are described below
- allow access to the stored data from the service with some filters described below - there are no requirements around the method of access, you may choose

Create a solution that you consider as close to production-ready as possible. Focus on quality rather than quantity.

## Business Rules

Data whose timestamp is "too old" should be treated as invalid and discarded. "Too old" means the data are timestamped more than 1 hour previous to the current time.

The server does some basic analysis on the data, and adds tags which both describe the data & possibly the outcomes of the analysis. Data internal to the system are tagged
with "system" and should be discarded. If the server believes the data to be inaccurate, it will tag those data points with "suspect". 
Potentially inaccurate data should be discarded.

It must be possible for an administrator of the service, but not necessarily the end user of the service (/API), to discover which data points have been discarded and why they were discarded

## Data Filtering

Users of the service who access the data must be able to filter the data by start and/or end times. All of these filters must be optional.

In other words, users must be able to access

- all data points
- data points generated after a certain datetime
- data points generated before a certain datetime
- data points generated within a set datetime range

## The API
 You can find the API by going to localhost:8000/api/ and from there you can use the rest_framework interface to explore it.
 As an alternative by going to localhost:8000/swagger/ you can find all the available endpoints and filters. These endpoints complete all simple data retrieval requirements, to find all data points within a certain range of time simply use a combination of the available filter, for example:
    
    ```http
    values/?timestamp__gte=2024-02-19T10:00:00&timestamp__lte=2024-02-19T11:00:00
    ```

## Final Consideration

To fulfill the requirement that stated that discard data could be evaluated by a user such as an administrator there are two ways, firstly you can check the docker logs for the worker that output a warning every time data is marked as discarded, however since this process is not very user friendly another aproach was added, data that is marked as to be deleted is also stored in the database, this data can be reviewed and deleted in the admin dashboard (localhost:8000/admin) by the admin user.

Along with the base project you can find some tests created to ensure some quality of the produced code. Tu run these tests follow these steps:
1. **Access the Django container:**

   ```bash
   docker-compose exec web bash
   ```
2. **Inside the container run the tests:**
   ```bash
   coverage run manage.py test
   ```
3. **Check Coverage (optional):**
   ```bash
   coverage report
   ```

At the moment of delivery a coverage of 98% was ensured.
