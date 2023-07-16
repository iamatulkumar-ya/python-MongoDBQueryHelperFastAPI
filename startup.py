from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
import uvicorn

from src.app.templateBaseClass import TemplateBaseClass
from src.app.appLoggerBaseClass import AppLoggerBaseClass
 

from src.handler.indexHandler import IndexHandler
from src.handler.connectToMongoHandler import ConnectToMongoHandler
from src.service.utilService import UtilClass
 
app =FastAPI()
# mounting css directory with the use of static files 
app.mount("/asset", StaticFiles(directory="src/asset"), name="asset")
app.mount("/js", StaticFiles(directory="src/js"), name="js")


utilClass = UtilClass()
 
@app.on_event("startup")
async def app_Started():
    print("FastAPI started. Initializing base classes.")
    TemplateBaseClass()
    AppLoggerBaseClass()


@app.route('/', methods=['GET'])
def welcomToPortal(request: Request):
    return IndexHandler().getIndexContent(request)


 

@app.post('/ConnectToMongo')
async def connectToMongo(request:Request):
    print(f"Inside - {__name__}")
    formJbody =await request.json()   
    resStatus, errorMessage = ConnectToMongoHandler().connectToMongo(formJbody) 

    if resStatus == "CONNECTED":
       return utilClass.generateAPIResponse(status.HTTP_200_OK,{}, resStatus,errorMessage)
    else:
       return utilClass.generateAPIResponse(status.HTTP_400_BAD_REQUEST,{},  resStatus,errorMessage)



@app.post('/findQuery')
async def findQuery(request:Request):
    print(f"Inside - {__name__}")
    queryJbody =await request.json()   
    resStatus, errorMessage = ConnectToMongoHandler().findQuery(queryJbody) 

    if resStatus == "FOUND":
       return utilClass.generateAPIResponse(status.HTTP_200_OK,{}, resStatus,errorMessage)
    else:
       return utilClass.generateAPIResponse(status.HTTP_400_BAD_REQUEST,{},  resStatus,errorMessage)







@app.on_event("shutdown")
async def app_Shutdown():
    print("FastAPI is shutting down.")
 

if __name__=="__main__":
    

    _host="localhost"
    _port=3300

    uvicorn.run("startup:app",host=_host,port=_port,reload=True)


