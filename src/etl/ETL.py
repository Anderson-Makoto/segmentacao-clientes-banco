from Extract import Extract;

class ETL:

    extract = None;
    client = 'local';

    def __init__(self):
        self.extract = Extract(self.client);

etl = ETL();
etl.extract.getFromSource('../resources/Customer-Churn-Record.csv');