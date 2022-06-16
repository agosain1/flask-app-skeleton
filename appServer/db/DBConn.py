#The following example is withour SQLAlchemy. If you are using SQLAlchemy disregard this file.
import psycopg2
import psycopg2.extras
from dbconfig import config
import time

class DBConn():
    def __init__(self):
        self.conn = None

    def close(self):
        if self.conn:
            self.conn.close()
            print('{} Database connection closed'.format(time.time()))

    def connect(self):
        """ Connect to the PostgreSQL database server """
        #conn = None
        ret_val=False
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            #print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)
            print('{} Connected to the PostgreSQL database'.format(time.time()))
            ret_val=True
            # # create a cursor
            # cur = self.conn.cursor()
            #
            # # execute a statement
            # print('PostgreSQL database version:')
            # cur.execute('SELECT version()')
            #
            # # display the PostgreSQL database server version
            # db_version = cur.fetchone()
            # print(db_version)
            #
            # # close the communication with the PostgreSQL
            # cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        #finally:
            #print("====finally make sure to close db connection when done!")
            # if self.conn is not None:
            #     self.conn.close()
            #     print('Database connection closed.')
        return ret_val

    def do_query(self, q):
        cursor = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        #q = "SELECT server, data, report_date FROM kw_server_raw WHERE processed = FALSE"
        cursor.execute(q)
        results = cursor.fetchall()
        cursor.close()
        return results