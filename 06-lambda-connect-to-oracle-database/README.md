# AWS Lambda connect to Oracle Database
##Prepare
1. EC2 with Ubuntu 16.04
2. Download the following files from [github](http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html)
> instantclient-basiclite-linux.x64-12.1.0.2.0.zip
> instantclient-sdk-linux.x64-12.1.0.2.0.zip

Step:
    1. Log in to Ubuntu server and install: zip, unzip, python2.7, pip, make
        > apt-get install -y zip unzip make git
        > apt-get install -y python-minimal
        > curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
        > python get-pip.py
        > pip --version
        > sudo apt-get install -y libaio1

    2. Put the download file into /tmp/instantclient/
        > mkdir /tmp/instantclient/
    
    3. Clone the repo
        > git clone https://github.com/landrey21/aws-lambda-python-oracle.git
        > cd aws-lambda-python-oracle
    
    4. Let create some Lambda code
        > rm -y lambda_function.py
        > vim lambda_function.py

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

            #logger.info('username: ' + username)
            #logger.info('host: ' + host)

            sql = """SELECT COUNT(*) AS TEST_COUNT FROM DUAL"""

            cur.execute(sql)
            columns = [i[0] for i in cur.description]
            rows = [dict(zip(columns, row)) for row in cur]
            logger.info(rows)

            con.close()
            logger.info('end lambda_handler')
        return "Successfully connected to oracle."

    5. Compile the instantclient and cx_Oracle
        > make
        > make package

    6. You will see the zip file named "lambda.zip", upload this zip file to S3 by using awscli
    
    7. Create a Lambda and set the runtime to python2.7, Set the Lambda in same VPC and subnet which is your oracle rds located, and set the environment variable.
        > ORACLE_SID
        > ORACLE_PORT
        > ORACLE_HOST
        > ORACLE_USER
        > ORACLE_PASSWORD

    8. Crate any test template and click test。
