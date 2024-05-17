import pymysql
host = 'localhost'
user = 'root'
password = 'Admin123'
database = 'vaishnavi'
connection=pymysql.connect(host=host, user=user, password=password, database=database)
cursor=connection.cursor()
cursor.execute("SELECT * FROM COLLEGE")
results=cursor.fetchall()
for row in results:
    print(row)
cursor.close()
connection.close()
