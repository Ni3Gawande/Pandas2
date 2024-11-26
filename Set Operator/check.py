import pandas as pd
from sqlalchemy import create_engine

engine_server = create_engine('mssql+pyodbc://LAPTOP-J82A4UMN/fun?driver=SQL+Server+Native+Client+11.0&trusted_connection=yes')
connection_server=engine_server.connect()
hostname='localhost'
username='root'
password = 'system'
port='3306'
database='fun'
engine_mysql=create_engine('mysql+pymysql://'+username+':'+password+'@'+hostname+':'+port+'/'+database)
connection_mysql=engine_mysql.connect()

source_schema='dbo'
target_schema='fun'
source_table='employees'
target_table='employees'
