import os
from application import simple_db
import sqlite3
import unittest


class TestMusicDatabase(unittest.TestCase):
    """
    Test the music database
    """

    def setUp(self):
        """
        Setup a temporary database
        """
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()

        # create a table
        cursor.execute("""CREATE TABLE employees
                                 (name text, position text, arrival_date text,
                                  service text, salary text)
                              """)
        # insert some data
        cursor.execute("INSERT INTO employees VALUES "
                       "('Dupont', 'engineer', '7/24/2012',"
                       "'DSI', '2000')")

        # save data to database
        conn.commit()

        # insert multiple records using the more secure "?" method
        employees = [('Deghdegh', 'HR', '7/9/2002',
                      'HR', '3000'),
                     ('Dridi', 'CISO', '2/1/2011',
                      'DSI', '100'),
                     ('Zhu', 'HR2',
                      '4/17/2012', 'HR1', '2000'),
                     ('Firpion', 'DSI', '4/10/2012',
                      'engineer', '3000')]
        cursor.executemany("INSERT INTO employees VALUES (?,?,?,?,?)",
                           employees)
        conn.commit()

    def tearDown(self):
        """
        Delete the database
        """
        os.remove("employees.db")


    def test_updating_artist(self):
        """
        Tests that we can successfully update an artist's name
        """
        simple_db.update_position('HR', 'DIRECTOR')
        actual = simple_db.select_all_employees('DIRECTOR')
        expected = [('Deghdegh', 'DIRECTOR', '7/9/2002',
                      'HR', '3000')]
        self.assertListEqual(expected, actual)


    def test_artist_does_not_exist(self):

        result = simple_db.select_all_employees('DIRECTOR')
        self.assertFalse(result)