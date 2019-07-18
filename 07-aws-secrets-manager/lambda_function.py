import cx_Oracle
import os
import logging
import boto3
import json
import base64
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info('begin lambda_handler')

    connectionString = json.loads(get_connection_strings())

    username = connectionString["username"]
    password = connectionString["password"]
    host = connectionString["host"]
    port = connectionString["port"]
    sid = connectionString["dbname"]

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

def get_connection_strings():

    secret_name = "prod/demo/oracle"
    region_name = "us-west-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return decoded_binary_secret
    return ""