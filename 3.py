import MySQLdb
import json

conn = MySQLdb.connect(user='your_db_user',
                       password='your_db_password',
                       host='127.0.0.1',
                       db='sample')
query = "SELECT * FROM users;"
with conn.cursor(MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute(query)
    all_data = cursor.fetchall()

for data in all_data:
    if data['id'] == 2:
        print(json.dumps(data, indent=4))
