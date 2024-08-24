# Pizza Runner

All information regarding the case study has been sourced from the following link: [link](https://8weeksqlchallenge.com/case-study-2/)

# Background Information and Task

Danny is expanding his new Pizza Empire and at the same time he wants to Uberize it, so Pizza Runner was launched!
<br><br>
Danny is very aware that data collection was going to be critical for his business’ growth.
<br><br>
Given the collected data, Danny want:
-  assistance to clean the data
-  apply some basic calculations

So he can **better direct his "runners"** (employees who deliver pizza) and **optimise Pizza Runner’s operations**.

# Importing Required Libraries


```python
!pip3 install PyMySQL
```

    Requirement already satisfied: PyMySQL in /opt/anaconda3/lib/python3.11/site-packages (1.1.1)



```python
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os
from IPython.display import Image
```


```python
load_dotenv(find_dotenv())
```




    True



# Obtaining Database Connection


```python
db_pwd = os.getenv("MySQL_PWD")
db_name = 'pizza_runner'
```


```python
db_connection_str = f'mysql+pymysql://root:{db_pwd}@localhost/{db_name}'
db_connection = create_engine(db_connection_str)
```


```python

```

# ER Diagram


```python
Image(filename='./resources/Pizza Runner ER Diagram.png')
```




    
![png](output_13_0.png)
    




```python

```

# Helper Function


```python
def execute_query(query_str):
    return pd.read_sql_query(query_str, con=db_connection)
```


```python

```

# Overview of Tables

## runners


```python
execute_query("select * from runners")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>runner_id</th>
      <th>registration_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2021-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2021-01-03</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2021-01-08</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2021-01-15</td>
    </tr>
  </tbody>
</table>
</div>




```python
execute_query("desc runners")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Field</th>
      <th>Type</th>
      <th>Null</th>
      <th>Key</th>
      <th>Default</th>
      <th>Extra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>runner_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>registration_date</td>
      <td>date</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



## customer_orders


```python
execute_query("select * from customer_orders")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order_id</th>
      <th>customer_id</th>
      <th>pizza_id</th>
      <th>exclusions</th>
      <th>extras</th>
      <th>order_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>101</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>2020-01-01 18:05:02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>101</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>2020-01-01 19:00:52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>102</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>2020-01-02 23:51:23</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>102</td>
      <td>2</td>
      <td></td>
      <td>None</td>
      <td>2020-01-02 23:51:23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>103</td>
      <td>1</td>
      <td>4</td>
      <td></td>
      <td>2020-01-04 13:23:46</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>103</td>
      <td>1</td>
      <td>4</td>
      <td></td>
      <td>2020-01-04 13:23:46</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4</td>
      <td>103</td>
      <td>2</td>
      <td>4</td>
      <td></td>
      <td>2020-01-04 13:23:46</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5</td>
      <td>104</td>
      <td>1</td>
      <td>null</td>
      <td>1</td>
      <td>2020-01-08 21:00:29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6</td>
      <td>101</td>
      <td>2</td>
      <td>null</td>
      <td>null</td>
      <td>2020-01-08 21:03:13</td>
    </tr>
    <tr>
      <th>9</th>
      <td>7</td>
      <td>105</td>
      <td>2</td>
      <td>null</td>
      <td>1</td>
      <td>2020-01-08 21:20:29</td>
    </tr>
    <tr>
      <th>10</th>
      <td>8</td>
      <td>102</td>
      <td>1</td>
      <td>null</td>
      <td>null</td>
      <td>2020-01-09 23:54:33</td>
    </tr>
    <tr>
      <th>11</th>
      <td>9</td>
      <td>103</td>
      <td>1</td>
      <td>4</td>
      <td>1, 5</td>
      <td>2020-01-10 11:22:59</td>
    </tr>
    <tr>
      <th>12</th>
      <td>10</td>
      <td>104</td>
      <td>1</td>
      <td>null</td>
      <td>null</td>
      <td>2020-01-11 18:34:49</td>
    </tr>
    <tr>
      <th>13</th>
      <td>10</td>
      <td>104</td>
      <td>1</td>
      <td>2, 6</td>
      <td>1, 4</td>
      <td>2020-01-11 18:34:49</td>
    </tr>
  </tbody>
</table>
</div>




```python
execute_query("desc customer_orders")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Field</th>
      <th>Type</th>
      <th>Null</th>
      <th>Key</th>
      <th>Default</th>
      <th>Extra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>order_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>customer_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>pizza_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>exclusions</td>
      <td>varchar(4)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>extras</td>
      <td>varchar(4)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>order_time</td>
      <td>timestamp</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



## runner_orders


```python
execute_query("select * from runner_orders")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order_id</th>
      <th>runner_id</th>
      <th>pickup_time</th>
      <th>distance</th>
      <th>duration</th>
      <th>cancellation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2020-01-01 18:15:34</td>
      <td>20km</td>
      <td>32 minutes</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>2020-01-01 19:10:54</td>
      <td>20km</td>
      <td>27 minutes</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>2020-01-03 00:12:37</td>
      <td>13.4km</td>
      <td>20 mins</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2</td>
      <td>2020-01-04 13:53:03</td>
      <td>23.4</td>
      <td>40</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3</td>
      <td>2020-01-08 21:10:57</td>
      <td>10</td>
      <td>15</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>3</td>
      <td>null</td>
      <td>null</td>
      <td>null</td>
      <td>Restaurant Cancellation</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>2</td>
      <td>2020-01-08 21:30:45</td>
      <td>25km</td>
      <td>25mins</td>
      <td>null</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>2</td>
      <td>2020-01-10 00:15:02</td>
      <td>23.4 km</td>
      <td>15 minute</td>
      <td>null</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>2</td>
      <td>null</td>
      <td>null</td>
      <td>null</td>
      <td>Customer Cancellation</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2020-01-11 18:50:20</td>
      <td>10km</td>
      <td>10minutes</td>
      <td>null</td>
    </tr>
  </tbody>
</table>
</div>




```python
execute_query("desc runner_orders")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Field</th>
      <th>Type</th>
      <th>Null</th>
      <th>Key</th>
      <th>Default</th>
      <th>Extra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>order_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>runner_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>pickup_time</td>
      <td>varchar(19)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>distance</td>
      <td>varchar(7)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>duration</td>
      <td>varchar(10)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>cancellation</td>
      <td>varchar(23)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



## pizza_names


```python
execute_query("select * from pizza_names")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pizza_id</th>
      <th>pizza_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Meatlovers</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Vegetarian</td>
    </tr>
  </tbody>
</table>
</div>



## pizza_recipes


```python
execute_query("select * from pizza_recipes")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pizza_id</th>
      <th>toppings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1, 2, 3, 4, 5, 6, 8, 10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4, 6, 7, 9, 11, 12</td>
    </tr>
  </tbody>
</table>
</div>




```python
execute_query("desc pizza_recipes")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Field</th>
      <th>Type</th>
      <th>Null</th>
      <th>Key</th>
      <th>Default</th>
      <th>Extra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>pizza_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>toppings</td>
      <td>text</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



## pizza_toppings


```python
execute_query("select * from pizza_toppings")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>topping_id</th>
      <th>topping_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bacon</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>BBQ Sauce</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Beef</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Cheese</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Chicken</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Mushrooms</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Onions</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Pepperoni</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Peppers</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Salami</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Tomatoes</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Tomato Sauce</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

## Observations

```customer_orders``` and ```runner_orders``` tables require data type modifications and cleaning before proceeding with analysis.

customer_orders:
- exclusions ```missing/blank spaces "" and null values```
- extras ```missing/blank spaces "" and null values```

runner_orders:
- pickup_time ```wrong data type and null values```
- distance ```wrong data type and null values```
- duration ```wrong data type and null values```
- cancellation ```missing/blank spaces "" and null values```


```python

```


```python

```

# Data Cleaning

Data cleaning was done directly in MySQLWorkbench. Commandas used are shown below.

## customer_orders

```sql
CREATE TEMPORARY TABLE cleaned_customer_orders
SELECT * FROM customer_orders;

-- exclusions column
UPDATE cleaned_customer_orders
SET exclusions = NULL
WHERE exclusions IN ("","null");

-- extras column
UPDATE cleaned_customer_orders
SET extras = NULL
WHERE extras IN ("","null");

-- modify original table with cleaned data
TRUNCATE TABLE customer_orders; -- use this command with caution

INSERT INTO customer_orders
SELECT * FROM cleaned_customer_orders;
```


```python
execute_query("select * from customer_orders") # cleaned customer_orders table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order_id</th>
      <th>customer_id</th>
      <th>pizza_id</th>
      <th>exclusions</th>
      <th>extras</th>
      <th>order_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>101</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-01 18:05:02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>101</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-01 19:00:52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>102</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-02 23:51:23</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>102</td>
      <td>2</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-02 23:51:23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>103</td>
      <td>1</td>
      <td>4</td>
      <td>None</td>
      <td>2020-01-04 13:23:46</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>103</td>
      <td>1</td>
      <td>4</td>
      <td>None</td>
      <td>2020-01-04 13:23:46</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4</td>
      <td>103</td>
      <td>2</td>
      <td>4</td>
      <td>None</td>
      <td>2020-01-04 13:23:46</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5</td>
      <td>104</td>
      <td>1</td>
      <td>None</td>
      <td>1</td>
      <td>2020-01-08 21:00:29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6</td>
      <td>101</td>
      <td>2</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-08 21:03:13</td>
    </tr>
    <tr>
      <th>9</th>
      <td>7</td>
      <td>105</td>
      <td>2</td>
      <td>None</td>
      <td>1</td>
      <td>2020-01-08 21:20:29</td>
    </tr>
    <tr>
      <th>10</th>
      <td>8</td>
      <td>102</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-09 23:54:33</td>
    </tr>
    <tr>
      <th>11</th>
      <td>9</td>
      <td>103</td>
      <td>1</td>
      <td>4</td>
      <td>1, 5</td>
      <td>2020-01-10 11:22:59</td>
    </tr>
    <tr>
      <th>12</th>
      <td>10</td>
      <td>104</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>2020-01-11 18:34:49</td>
    </tr>
    <tr>
      <th>13</th>
      <td>10</td>
      <td>104</td>
      <td>1</td>
      <td>2, 6</td>
      <td>1, 4</td>
      <td>2020-01-11 18:34:49</td>
    </tr>
  </tbody>
</table>
</div>




```python
execute_query("desc customer_orders") 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Field</th>
      <th>Type</th>
      <th>Null</th>
      <th>Key</th>
      <th>Default</th>
      <th>Extra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>order_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>customer_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>pizza_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>exclusions</td>
      <td>varchar(4)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>extras</td>
      <td>varchar(4)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>order_time</td>
      <td>timestamp</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python

```

## runner_orders

```sql
CREATE TEMPORARY TABLE cleaned_runner_orders
SELECT * FROM runner_orders;

-- cancellation column
UPDATE cleaned_runner_orders
SET cancellation = NULL
WHERE cancellation IN ("","null");

-- duration column
UPDATE cleaned_runner_orders
SET duration = NULL
WHERE duration IN ("","null");

UPDATE cleaned_runner_orders
SET duration = (SELECT REPLACE(REPLACE(REPLACE(duration,"minutes",""),"mins",""),"minute",""));

ALTER TABLE cleaned_runner_orders
MODIFY duration INTEGER;

-- distance column
UPDATE cleaned_runner_orders
SET distance = NULL
WHERE distance IN ("","null");

UPDATE cleaned_runner_orders
SET distance = (SELECT REPLACE(distance,"km",""));

ALTER TABLE cleaned_runner_orders
MODIFY distance FLOAT;

-- pickup_time column
UPDATE cleaned_runner_orders
SET pickup_time = NULL
WHERE pickup_time IN ("","null");

ALTER TABLE cleaned_runner_orders
MODIFY pickup_time TIMESTAMP;

-- modify origial table with cleaned data
TRUNCATE runner_orders;

ALTER TABLE runner_orders
MODIFY duration INTEGER;

ALTER TABLE runner_orders
MODIFY distance FLOAT;

ALTER TABLE runner_orders
MODIFY pickup_time TIMESTAMP;

INSERT INTO runner_orders
SELECT * FROM cleaned_runner_orders;



```


```python
execute_query("select * from runner_orders") # cleaned runner_orders table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order_id</th>
      <th>runner_id</th>
      <th>pickup_time</th>
      <th>distance</th>
      <th>duration</th>
      <th>cancellation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2020-01-01 18:15:34</td>
      <td>20.0</td>
      <td>32.0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>2020-01-01 19:10:54</td>
      <td>20.0</td>
      <td>27.0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>2020-01-03 00:12:37</td>
      <td>13.4</td>
      <td>20.0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2</td>
      <td>2020-01-04 13:53:03</td>
      <td>23.4</td>
      <td>40.0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3</td>
      <td>2020-01-08 21:10:57</td>
      <td>10.0</td>
      <td>15.0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>3</td>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Restaurant Cancellation</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>2</td>
      <td>2020-01-08 21:30:45</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>2</td>
      <td>2020-01-10 00:15:02</td>
      <td>23.4</td>
      <td>15.0</td>
      <td>None</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>2</td>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Customer Cancellation</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2020-01-11 18:50:20</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
execute_query("desc runner_orders") 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Field</th>
      <th>Type</th>
      <th>Null</th>
      <th>Key</th>
      <th>Default</th>
      <th>Extra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>order_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>runner_id</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>pickup_time</td>
      <td>timestamp</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>distance</td>
      <td>float</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>duration</td>
      <td>int</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>cancellation</td>
      <td>varchar(23)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```

# Questions

## Pizza Metrics

***

```1. How many pizzas were ordered?```


```python
query_str = (
    """
    select count(*) as total_orders
    from customer_orders
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_orders</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**: Total of 14 pizzas were ordered

***

```2. How many unique customer orders were made?```


```python
query_str = (
    """
    select count(distinct order_id) as unique_orders
    from customer_orders
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>unique_orders</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**: Total of 10 unique orders were made

***

```3. How many successful orders were delivered by each runner?```


```python
query_str = (
    """
    select runner_id, count(duration) as successful_orders
    from runner_orders
    group by runner_id
    order by successful_orders desc
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>runner_id</th>
      <th>successful_orders</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



***

```4. How many of each type of pizza was delivered?```


```python
query_str = (
    """
    select pizza_name, count(*) as number_delivered
    from 
        runner_orders r
        join
        customer_orders c
        on r.order_id = c.order_id
        join 
        pizza_names p
        on c.pizza_id = p.pizza_id
    where r.duration IS NOT NULL
    group by p.pizza_name
    order by 2 desc
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pizza_name</th>
      <th>number_delivered</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Meatlovers</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Vegetarian</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**: 9 Meatlovers and 3 Vegetarian pizzas were successfully delivered

***

```5. How many Vegetarian and Meatlovers were ordered by each customer?```


```python
query_str = (
    """
    select
       c.customer_id,
       SUM(
           CASE
               WHEN p.pizza_name = "Meatlovers" THEN 1
               ELSE 0
           END
       ) as Meatlovers,
       SUM(
           CASE
               WHEN p.pizza_name = "Vegetarian" THEN 1
               ELSE 0
           END
       ) as Vegetarian
    from 
        customer_orders c
        join 
        pizza_names p 
        on c.pizza_id = p.pizza_id
    group by 1
    order by c.customer_id
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>customer_id</th>
      <th>Meatlovers</th>
      <th>Vegetarian</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>102</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103</td>
      <td>3.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>104</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>105</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



***

```6. What was the maximum number of pizzas delivered in a single order?```


```python
query_str = (
    """
    with items_per_order as (
        select 
            c.order_id, 
            count(*) number_of_items 
        from 
            customer_orders c 
            join 
            runner_orders r 
            on c.order_id = r.order_id 
        where r.duration is not null
        group by c.order_id
        order by 2 desc
    )

    select max(number_of_items) "Maximum number of pizza in single order"
    from items_per_order
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Maximum number of pizza in single order</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



***

```7. For each customer, how many delivered pizzas had at least 1 change and how many had no changes?```


```python
query_str = (
    """
    select 
        customer_id,
        SUM(
            CASE
                WHEN exclusions is not null or extras is not null then 1
                ELSE 0
            END
        ) as "Atlease 1 change",
        SUM(
            CASE
                WHEN exclusions is null and extras is null then 1
                ELSE 0
            END
        ) as "No changes"
    from 
        customer_orders c
        join 
        runner_orders r
        on c.order_id = r.order_id
    where r.duration is not null
    group by customer_id
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>customer_id</th>
      <th>Atlease 1 change</th>
      <th>No changes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>0.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>102</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>104</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>105</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**:
- customer 101 and 102 like the pizzas as per the original recipes
- customers 103,104 and 105 perfer slight changes from the original recipie to suit their taste.

***

```8. How many pizzas were delivered that had both exclusions and extras?```


```python
query_str = (
    """
     select 
        count(*) as "pizza count with exclusions and extras"
    from
        customer_orders c
        join 
        runner_orders r
        on c.order_id = r.order_id
    where 
        r.duration is not null
        and
        c.exclusions is not null
        and
        c.extras is not null
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pizza count with exclusions and extras</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**: only 1 pizza delivered has both exclusion and extra toppings.

***

```9. What was the total volume of pizzas ordered for each hour of the day?```


```python
query_str = (
     """
    select
        HOUR(order_time) as hour_of_day,
        count(*) as total_vvolume
    from customer_orders
    group by 1
    order by 1
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hour_of_day</th>
      <th>total_vvolume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>19</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>23</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**:
- Highest Volume of orders at 1:00 pm, 6:00 pm, 9:00 pm and 11:00 pm
- Lowest Volume of orders at 11:00 am and 7:00 pm

***

```10. What was the volume of orders for each day of the week?```


```python
query_str = (
    """
    select
       DAYNAME(order_time) as "day_of_week",
       count(order_id) as total_volume
    from customer_orders
    group by 1
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day_of_week</th>
      <th>total_volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Wednesday</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Thursday</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Saturday</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Friday</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**:
- Wednesday and Saturday have the most amount of orders (5) closely followed by Thursday (3), least amount of orders on Friday (1)


```python

```

## Runner and Customer Experience

***

```1. How many runners signed up for each 1 week period? (i.e. week starts 2021-01-01)```


```python
query_str = (
    """
    select 
    FLOOR(DATEDIFF(registration_date,'2021-01-01')/7)+1 as registration_week,
    count(*) runner_signup
    from runners
    group by 1
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>registration_week</th>
      <th>runner_signup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



**Observation**: 
- 1st week of JAN 2021 there were 2 new runner signups
- 2nd and 3rd week JAN 2021 there were 1 new runner signups

***

```2. What was the average time in minutes it took for each runner to arrive at the Pizza Runner HQ to pickup the order?```


```python
query_str = (
    """
    select
        r.runner_id,
        ROUND(AVG(TIMESTAMPDIFF(MINUTE, c.order_time,r.pickup_time)),2) as avg_arrival_time
    from 
        customer_orders c
        join
        runner_orders r
        on c.order_id = r.order_id
    where r.pickup_time IS NOT NULL
    group by r.runner_id
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>runner_id</th>
      <th>avg_arrival_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>15.33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>23.40</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>10.00</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**:
- runner 3 has the fastest average arrival time at 10 minutes
- runner 1 has the 2nd fastest average arrival time at around 15 minutes
- runner 2 has a comparatively high average arrival time at 23 minutes 

***

```3. Is there any relationship between the number of pizzas and how long the order takes to prepare?```


```python
query_str = (
    """
    with prep_time as (
        select
            c.order_id,
            count(*) as number_of_pizzas,
            AVG(TIMESTAMPDIFF(MINUTE, c.order_time, r.pickup_time)) as preparation_time
        from
            customer_orders c
            join
            runner_orders r
            on c.order_id = r.order_id
        where r.pickup_time is not null
        group by c.order_id
    )

    select
        number_of_pizzas,
        AVG(preparation_time) as avg_prep_time
    from prep_time
    group by number_of_pizzas
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>number_of_pizzas</th>
      <th>avg_prep_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>29.0</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**: From the above table we see a direct relationship between the number of pizzas per order and the prep time.

***

```4. What was the average distance travelled for each customer?```


```python
query_str = (
    """
    select 
        c.customer_id,
        ROUND(AVG(r.distance),2) as avg_distance
    from 
        customer_orders c 
        join
        runner_orders r
        on c.order_id = r.order_id
    where r.duration is not null
    group by c.customer_id
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>customer_id</th>
      <th>avg_distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>20.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>102</td>
      <td>16.73</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103</td>
      <td>23.40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>104</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>105</td>
      <td>25.00</td>
    </tr>
  </tbody>
</table>
</div>



***

```5. What was the difference between the longest and shortest delivery times for all orders?```


```python
query_str = (
    """
    select 
        MAX(duration) - MIN(duration) as difference
    from runner_orders
    where duration is not null
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>difference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>



***

```6. What was the average speed for each runner for each delivery and do you notice any trend for these values?```


```python
query_str = (
    """
    select 
        order_id,
        runner_id,
        ROUND(distance / (duration/60),2) as avg_speed_kmh
    from 
        runner_orders r
    where r.duration is not null
    order by 3 asc
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order_id</th>
      <th>runner_id</th>
      <th>avg_speed_kmh</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>2</td>
      <td>35.10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>37.50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>3</td>
      <td>40.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>40.20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>1</td>
      <td>44.44</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>2</td>
      <td>60.00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>10</td>
      <td>1</td>
      <td>60.00</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>2</td>
      <td>93.60</td>
    </tr>
  </tbody>
</table>
</div>



***

```7. What is the successful delivery percentage for each runner?```


```python
query_str = (
    """
    select 
        runner_id,
        (1 - (COUNT(cancellation)/COUNT(*))) * 100 as successful_delivery_pct
    from 
        runner_orders r
    group by  runner_id
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>runner_id</th>
      <th>successful_delivery_pct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>50.0</td>
    </tr>
  </tbody>
</table>
</div>



**Observations**: note that the low successful_delivery_pct is due to order cancellation by the restaurant or the customer with is not in the hands of the runner. A different metric should be used to gauge the effectiveness of a runner.


```python

```

## Ingredient Optimisation

**REVISIT AFTER MORE EXPERIENCE WITH HANDLING STRINGS (6 questions)**


```python

```

## Pricing and Ratings

***

```1. If a Meat Lovers pizza costs $12 and Vegetarian costs $10 and there were no charges for changes - how much money has Pizza Runner made so far if there are no delivery fees?```


```python
query_str = (
    """
    select 
        SUM(
            CASE
                when pizza_name like "meatlovers" then 12
                else 10
            END
        ) as total_revenue
    from 
        customer_orders c
        join
        runner_orders r
        on c.order_id = r.order_id
        join
        pizza_names p
        on p.pizza_id = c.pizza_id
    where duration is not null
    """
)
```


```python
execute_query(query_str)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>138.0</td>
    </tr>
  </tbody>
</table>
</div>



***

```5. If a Meat Lovers pizza was $12 and Vegetarian $10 fixed prices with no cost for extras and each runner is paid $0.30 per kilometre traveled - how much money does Pizza Runner have left over after these deliveries?```


```python
execute_query(
    """
    with costs_cte as (
        select 
            CASE
                when pizza_name like "meatlovers" then 12
                else 10
            END as revenue,
            distance * 0.30 as runner_charges
        from 
            customer_orders c
            join
            runner_orders r
            on c.order_id = r.order_id
            join
            pizza_names p
            on p.pizza_id = c.pizza_id
        where duration is not null
    )

    select 
        ROUND(SUM(revenue - runner_charges),2)
    from costs_cte
    """
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ROUND(SUM(revenue - runner_charges),2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>73.38</td>
    </tr>
  </tbody>
</table>
</div>



**Suggestions**: Pizza runner should charge for extras or apply a delivery fee to compensate for the runner_charges and other expenses in the future


```python

```

**REVISIT AFTER MORE EXPERIENCE (3 questions)**


```python

```
