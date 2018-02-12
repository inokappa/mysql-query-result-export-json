import MySQLdb
import json

conn = MySQLdb.connect(user='your_db_user',
                       password='your_db_password',
                       host='127.0.0.1',
                       db='sample')
query = 'SELECT * FROM users;'

cursor = conn.cursor(MySQLdb.cursors.DictCursor)
cursor.execute(query)
data = cursor.fetchone()
conn.close()
print(json.dumps(data, indent=4))
