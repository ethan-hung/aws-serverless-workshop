import cx_Oracle
import os
import logging
import boto3
from botocore.exceptions import ClientError

username = os.environ["ORACLE_USER"]
password = os.environ['ORACLE_PASSWORD']
host = os.environ['ORACLE_HOST']
port = os.environ['ORACLE_PORT']
sid = os.environ['ORACLE_SID']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info('begin lambda_handler')

    dsn = cx_Oracle.makedsn(host, port, sid)
    con = cx_Oracle.connect(username, password, dsn)
    cur = con.cursor()

    sql = """SELECT COUNT(*) AS TEST_COUNT FROM DUAL"""

    cur.execute(sql)
    columns = [i[0] for i in cur.description]
    rows = [dict(zip(columns, row)) for row in cur]
    logger.info(rows)

    con.close()
    logger.info('end lambda_handler')
    return "Successfully connected to oracle."