from flask import Flask
from markupsafe import escape
from flask import jsonify, request
import pyspark
from pyspark.sql import SparkSession

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome!</h1><h2>Please go to /run_query to run a query</h2>'

@app.route('/run_query')
def projects():
    query = request.args.get('query')
    spark = SparkSession.builder.config("spark.sql.warehouse.dir", "/user/hive/warehouse/").enableHiveSupport().appName("SparkWebApp").getOrCreate()
    print ("Completed running SQL")
    dataframe = (spark.sql(query)).toPandas()
    return dataframe.to_json(orient="records")

@app.route('/about')
def about():
    return jsonify('The about page')

