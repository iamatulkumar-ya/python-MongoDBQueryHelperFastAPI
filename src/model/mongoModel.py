from pydantic import BaseModel

class ConnectionModel(BaseModel):
    connectionString: str
    dbName: str
    collectionName: str

class QueryModel(BaseModel):
    propertyName: str
    clause: str
    valueToBeSerached: str