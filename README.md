# Purrfect Creations Dashboard

The following app utilizes the data provided in airtable and draws useful insights.

> Note: This repo is part of the interview assignement at Vorboss
## Setup Instructions

1. Convert the `.env.example` file to `.env` and add the necessary credential.
2. To run the service, simply execute the following command:
```
    $ sudo docker-compose up -d
```
Visit http://127.0.0.1:8000/ in your browser. The app should be up & running.

3. To stop the container:
```
    $ sudo docker-compose up -d
```

## Implementation Specifics 

1. Django-based application.
2. Used `pyairtable` (a Python Client for the Airtable Api) to Retrieve data from Airtable table.
   For more info : [Link](https://pyairtable.readthedocs.io/en/latest/getting-started.html)
3. Key Figures implemented on the dashboard:
   ```
    - Total Orders

    - Total Orders this month

    - Number of orders in progress

    - Revenue

    - A list of the most recent few orders
    
    - Product popularity chart - BarGraph

    - Order Status Summary - PieChart
   ```
