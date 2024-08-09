import boto3;
import psycopg2;

class Transform:

    client = '';

    def __init__(self, client: str):
        self.client = client;

    def transformData(self, dataFrame):

        match self.client:
            case 'aws':
                return self.__getFromSourceAWS(dataFrame);
            case 'local':
                return self.__getFromSourceLocal(dataFrame);

    def __transformDataAWS(self, dataFrame):
        glue = boto3.client('glue');


    def __transformDataLocal(self, dataFrame):
        conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
        conn = psycopg2.connect(conn_string)
