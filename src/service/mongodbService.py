
from src.app.appLoggerBaseClass import AppLoggerBaseClass

from pymongo import MongoClient


class MongoDBService(AppLoggerBaseClass):

    def __init__(self) -> None:
        pass

    def getMongoClient(connectionString):
        _mongoClient = MongoClient(connectionString)
        return _mongoClient

    def connectToMongoDB(self, connectionString, dbName, collectionName):
        self.appLogger.info(f"Inside {__name__} module")
        try:
            _client = MongoDBService.getMongoClient(connectionString)
            serverInfo=_client.server_info()
            db = _client[dbName]
            collection = db[collectionName]
            return collection

        except Exception as ex:
            self.appLogger.error(
                f"Exception: Module- {__name__} , Error Message - {ex}")
            raise

    def executeFindQuery(_queryModelData):
        return "executed"
    