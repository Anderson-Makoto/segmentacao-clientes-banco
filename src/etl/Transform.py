import boto3;
import psycopg2;
from Extract import Extract;

class Transform:

    client = '';

    def __init__(self, client: str):
        self.client = client;

    def transformData(self, data):

        match self.client:
            case 'aws':
                return self.__getFromSourceAWS(data);
            case 'local':
                return self.__getFromSourceLocal(data);

    def __transformDataAWS(self, data):
        glue = boto3.client('glue');


    def __transformDataLocal(self, data):
        extract = Extract(self.client);
        rawData = extract.getFromSource();
        print(rawData);
        # conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
        # conn = psycopg2.connect(conn_string)

transform = Transform('local');