from Transform import Transform;

class Load:
    client = '';

    def __init__(self, client: str):
        self.client = client;

    def loadData(self, data):

        match self.client:
            case 'aws':
                return self.__loadDataAWS(data);
            case 'local':
                return self.__loadDataLocal(data);
