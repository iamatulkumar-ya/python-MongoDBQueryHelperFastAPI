from src.app.templateBaseClass import TemplateBaseClass
from src.app.appLoggerBaseClass import AppLoggerBaseClass
from src.service.mongodbService import MongoDBService
from src.model.mongoModel import ConnectionModel, QueryModel


class ConnectToMongoHandler(TemplateBaseClass, AppLoggerBaseClass):

    def __init__(self) -> None:
        super().__init__()

    def connectToMongo(self, formJbody):

        self.appLogger.info(f"Inside {__name__} module")
        try:
            _connectionModelData = ConnectionModel(**formJbody)

            _mongoDB = MongoDBService()
            _mongoDB.connectToMongoDB(_connectionModelData.connectionString,
                                      _connectionModelData.dbName, _connectionModelData.collectionName)

            return "CONNECTED", ""

        except Exception as ex:
            self.appLogger.error(
                f"Exception: Module- {__name__} , Error Message - {ex}")
            return "ERROR", str(ex)



    def findQuery(self, queryJbody):

        self.appLogger.info(f"Inside {__name__} module")
        try:
            _queryModelData = QueryModel(**queryJbody)

            _mongoDB = MongoDBService()
            _mongoDB.executeFindQuery(_queryModelData)
            return "FOUND", ""

        except Exception as ex:
            self.appLogger.error(
                f"Exception: Module- {__name__} , Error Message - {ex}")
            return "ERROR", str(ex)





