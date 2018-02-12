import unittest
import MySQLdb
import json
import sample


class TestSample(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        before = Before()
        before.prepare_db()
        before.insert_data()

    @classmethod
    def tearDownClass(self):
        after = After()
        after.drop_db()

    def test_sample_function(self):
        self.assertEqual(sample.sample_function(), 'sample')

    def test_db(self):
        self.assertTrue(sample.db('test_db'))

    def test_get_all_data(self):
        response = ({'id': 1, 'old': 18, 'name': 'Satou'},
                    {'id': 2, 'old': 20, 'name': 'Yamada'})
        self.assertEqual(sample.get_all_data('test_db', 'test_tbl'), response)

    def test_all_data_to_json(self):
        response = [{'id': 1, 'old': 18, 'name': 'Satou'},
                    {'id': 2, 'old': 20, 'name': 'Yamada'}]
        self.assertEqual(sample.all_data_to_json('test_db', 'test_tbl'),
                         json.dumps(response, indent=4))

    def test_selected_data_to_json(self):
        response = {'id': 1, 'old': 18, 'name': 'Satou'}
        self.assertEqual(sample.selected_data_to_json('test_db',
                         'test_tbl', 1),
                         json.dumps(response, indent=4))


class Before():
    def prepare_db(self):
        conn = MySQLdb.connect(user='your_db_user',
                               password='your_db_password',
                               host='127.0.0.1')
        query = """
        CREATE DATABASE test_db;
        USE test_db;
        CREATE TABLE test_tbl (
            id INT,
            old INT,
            name VARCHAR(255));
        """
        ope = DbOperation()
        ope.operater(conn, query)

    def insert_data(self):
        conn = MySQLdb.connect(user='your_db_user',
                               password='your_db_password',
                               host='127.0.0.1',
                               db='test_db')
        query = """
        INSERT INTO test_tbl (id, old, name)
        VALUES (1, 18, 'Satou'),
               (2, 20, 'Yamada');
        """
        ope = DbOperation()
        ope.operater(conn, query)


class After():
    def drop_db(self):
        conn = MySQLdb.connect(user='your_db_user',
                               password='your_db_password',
                               host='127.0.0.1')
        query = """
        DROP DATABASE test_db;
        """
        ope = DbOperation()
        ope.operater(conn, query)


class DbOperation():
    def operater(self, conn, query):
        cursor = conn.cursor()
        cursor.execute(query)
        if 'INSERT' in query:
            conn.commit()
        cursor.close()
        conn.close()
