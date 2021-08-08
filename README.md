# python-web-spark-sql

We will use PySpark and flask to enable to run spark sql queries via rest api call. We won't be including having a UI for users to input their queries on.but just enable running query directly

## Getting Started

You must first set up installation of flask in your local machine using below command

```shell
pip install flask
```

Run the following to kick off flash

```shell
export FLASK_APP=web_spark_sql
export FLASK_ENV=development
flask run
```

Run the following script and you should expect the proper row count

```shell
# select count(1) from test_schema.residential_property_transaction_parquet
curl -s "http://localhost:5000/run_query?query=select%20count%281%29%20from%20test_schema%2Eresidential_property_transactions"
# select * from  test_schema.residential_property_transaction_parquet limit 5
curl -s "http://localhost:5000/run_query?query=select%20%2a%20from%20test_schema%2Eresidential_property_transactions%20limit%205"
```

