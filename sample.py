import MySQLdb
import json


def sample_function():
    return 'sample'


def db(database):
    return MySQLdb.connect(user='your_db_user',
                           password='your_db_password',
                           host='127.0.0.1',
                           db=database)


def get_all_data(database, table):
    conn = db(database)
    query = 'SELECT * FROM %s;' % table
    with conn.cursor(MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return data


def all_data_to_json(database, table):
    return json.dumps(get_all_data(database, table), indent=4)


def selected_data_to_json(database, table, id):
    for data in get_all_data(database, table):
        if data['id'] == id:
            return json.dumps(data, indent=4)
