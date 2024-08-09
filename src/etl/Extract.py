import boto3;
import pandas as pd;

class Extract:

    client = '';

    def __init__(self, client: str):
        self.client = client;

    def getFromSource(self, file: str):
        match self.client:
            case 'aws':
                return self.__getFromSourceAWS(file);
            case 'local':
                return self.__getFromSourceLocal(file);

    def __getFromSourceAWS(self, file):
        s3 = boto3.client('s3');
        obj = s3.get_object(Bucket='AWS_BUCKET', Key='Customer-Churn-Records.csv');
        return pd.read_csv(obj['Body']);

    def __getFromSourceLocal(self, file):
        return pd.read_csv('../resources/Customer-Churn-Records.csv');